import os
import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
from dotenv import load_dotenv
from slugify import slugify
import json
import openai
import sys
import time
import random
import re
from datetime import datetime, timedelta, timezone

import captions_api

load_dotenv()

# Env var setup
# If this first one is missing, run fails, which is good.
youtube_key = os.environ.get('API_KEY')
# Second one is optional, but if it's missing, we'll skip the summary and cleanup.
openai_key = os.environ.get("OPENAI_API_KEY","")
# Optional. With OAuth credentials of a channel manager (see README.md, "How this runs") transcripts
# come from the official captions API, which works from cloud runners. Without them the unofficial
# youtube_transcript_api is used, which only works from a normal home or office connection.
oauth_credentials = captions_api.credentials_from_env()

_captions_client = None


def get_captions_client():
    """The shared official-API client, or None when no OAuth credentials are configured."""
    global _captions_client
    if oauth_credentials and _captions_client is None:
        _captions_client = captions_api.CaptionsClient(
            captions_api.build_youtube_client(*oauth_credentials),
            captions_api.QuotaTracker(captions_api.budget_from_env()))
    return _captions_client


def build_youtube():
    """A YouTube Data API client: the OAuth one when configured (no API_KEY needed), else the key."""
    client = get_captions_client()
    if client:
        return client.youtube
    return build('youtube', 'v3', developerKey=youtube_key)

def get_playlist_videos(playlist_id):
    youtube = build_youtube()
    
    video_ids = []
    next_page_token = None

    # This returns a list of youtube:playlistItem with rate limiting
    while True:
        try:
            # Build request parameters
            request_params = {
                'part': 'snippet',
                'playlistId': playlist_id,
                'maxResults': 50
            }
            
            # Only add pageToken if it's not None
            if next_page_token:
                request_params['pageToken'] = next_page_token
                
            request = youtube.playlistItems().list(**request_params)
            response = request.execute()

            for item in response['items']:
                video_ids.append(item['snippet']['resourceId']['videoId'])
            
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break
                
            # Rate limiting between pagination requests
            delay = random.uniform(3, 8)  # Random delay between 3-8 seconds
            print(f"Waiting {delay:.1f} seconds before next page...")
            time.sleep(delay)
            
        except HttpError as e:
            if e.resp.status == 403 and 'quota' in str(e).lower():
                print("Quota exceeded while fetching playlist items. Waiting before retry...")
                time.sleep(60)  # Wait 1 minute
                continue
            else:
                print(f"Error fetching playlist items: {e}")
                raise

    # Fetch video details in batches with rate limiting
    videos = []
    batch_size = 50  # YouTube API allows up to 50 IDs per request
    
    for i in range(0, len(video_ids), batch_size):
        batch_ids = video_ids[i:i + batch_size]
        
        try:
            request = youtube.videos().list(
                part='snippet,status',
                id=','.join(batch_ids)
            )
            response = request.execute()
            
            for item in response['items']:
                # The ID only: this runs before the public check and logs are visible.
                print(f"Found video: {item['id']}")
                videos.append(item)
                
            # Rate limiting between batches
            time.sleep(0.2)  # 200ms delay between batches
            
        except HttpError as e:
            if e.resp.status == 403 and 'quota' in str(e).lower():
                print(f"Quota exceeded on video details batch {i//batch_size + 1}. Waiting before retry...")
                time.sleep(60)
                continue
            else:
                print(f"Error fetching video details batch {i//batch_size + 1}: {e}")
                continue

    return videos

def get_channel_videos(channel_id, start_date, end_date):
    """Videos published between start_date and end_date (ISO 8601), newest first.

    Reads the channel's uploads playlist (1 quota unit per page of 50) instead of search.list
    (100 units per page), and stops paging once it is past start_date. Full video details,
    including the whole description, come from videos.list.
    """
    youtube = build_youtube()
    # A channel's uploads playlist ID is its channel ID with the "UC" prefix replaced by "UU".
    uploads = "UU" + channel_id[2:]
    videos = []
    next_page_token = None
    page_count = 0
    max_pages = 40  # Safety limit: 40 pages of 50 videos
    done = False

    while not done and page_count < max_pages:
        try:
            params = {'part': 'snippet,contentDetails', 'playlistId': uploads, 'maxResults': 50}
            if next_page_token:
                params['pageToken'] = next_page_token
            print(f"Listing uploads page {page_count + 1}")
            response = youtube.playlistItems().list(**params).execute()
        except HttpError as e:
            if e.resp.status == 403 and 'quota' in str(e).lower():
                print("Quota exceeded while listing channel uploads. Waiting before retry...")
                time.sleep(60)
                continue
            print(f"Error listing channel uploads: {e}")
            raise

        ids = []
        for item in response['items']:
            published = item['contentDetails'].get('videoPublishedAt') or item['snippet']['publishedAt']
            if published < start_date:
                done = True  # Uploads are newest first, so everything after this is older.
                continue
            if published <= end_date:
                ids.append(item['contentDetails']['videoId'])

        if ids:
            details = youtube.videos().list(part='snippet,status', id=','.join(ids)).execute()
            videos.extend(details['items'])

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break
        page_count += 1

    print(f"Found {len(videos)} videos between {start_date} and {end_date}")
    return videos

def get_publish(video):
    snippet = video['snippet']

    if 'publishTime' in snippet:
        return snippet['publishTime']
    return snippet['publishedAt']

def get_id(video):
    if type(video['id']) == str:
        return video['id']
    
    return video['id']['videoId']

URL_LINE = re.compile(r"^URL:\s*https?://(?:www\.)?youtube\.com/watch\?v=([A-Za-z0-9_-]+)", re.MULTILINE)


def video_ids_in_file(path):
    """The YouTube video ID of a transcript file: its last `URL:` line, because the generator writes
    its own URL line after the description, which can contain a `URL:` line of its own."""
    try:
        with open(path, encoding="utf-8") as file:
            matches = URL_LINE.findall(file.read())
        return {matches[-1]} if matches else set()
    except OSError:
        return set()


def existing_video_ids(directory):
    """The YouTube video IDs of every transcript already written to `directory`.

    The ID is stable when a channel retitles or republishes a video, unlike the
    publish time + title slug in the filename."""
    ids = set()
    for name in os.listdir(directory):
        if name.endswith(".md"):
            ids |= video_ids_in_file(os.path.join(directory, name))
    return ids


# An unfilled YouTube description template, e.g. "[INSTRUCTIONS: EDIT ANY AREA...]",
# "[INSERT DESCRIPTION ...]" or "[Add Pyroscope/GCX docs and blog links]".
# Uppercase INSTRUCTIONS / INSERT / ADD, as in YouTube's own template ("[INSERT DESCRIPTION - ...]"), or a
# title-case/lowercase form with at least three more words ("[Add Pyroscope/GCX docs and blog links]").
# "[Add-on]" and "[Insert coin]" are ordinary text.
PLACEHOLDER = re.compile(
    r"\[\s*(?:(?:INSTRUCTIONS|INSERT|ADD)\b(?!-)|(?i:instructions|insert|add)(?:\s+[^\s\]]+){3,})[^\]]*\]?")


def find_placeholder(description):
    """The first template placeholder left in a video description, or None."""
    match = PLACEHOLDER.search(description or "")
    return match.group(0) if match else None


def not_public_reason(video):
    """Why a video must not be published, or None when it is public and already aired.

    The repository is public, and with a channel manager's OAuth credentials the uploads list also
    holds private and unlisted videos and livestreams that have not started yet."""
    privacy = (video.get('status') or {}).get('privacyStatus')
    if privacy != 'public':
        return f"it is not public (privacy status: {privacy or 'unknown'})"
    broadcast = video['snippet'].get('liveBroadcastContent')
    if broadcast in ('upcoming', 'live'):
        return f"it is a livestream or premiere that has not finished ({broadcast})"
    return None


def should_skip(args, video, known_ids):
    """Why this video should not be transcribed now, or None. Logs the reason."""
    video_id = get_id(video)
    # Check this first and log the ID only: titles of non-public videos must not reach public logs.
    reason = not_public_reason(video)
    if reason:
        print(f"Skipping video {video_id} because {reason}.")
        return "not_public"
    if video_id in known_ids:
        print(f"Skipping video {video_id} because it already has a transcript.")
        return "duplicate"
    if os.path.isfile(file_for_video(args, video)):
        print(f"Skipping video {video_id} because it already has a transcript.")
        return "duplicate"
    placeholder = find_placeholder(video['snippet'].get('description', ''))
    if placeholder:
        print(f"Skipping video {video_id} ({video_title(video)}) because its "
              f"description still has a template placeholder: {placeholder[:60]}. "
              f"It will be picked up once the metadata is filled in.")
        return "placeholder"
    return None


def fetch_transcripts(args, videos):
    processed = []
    # Dedupe on the video ID, including videos handled earlier in this same run.
    known_ids = existing_video_ids(args.path)
    for i, video in enumerate(videos):
        video_id = get_id(video)
        
        if video_id == '':
            print(f"Could not find video ID for video ")
            print(json.dumps(video, indent=2))
            continue

        if should_skip(args, video, known_ids):
            continue

        print(f"Processing video {i+1}/{len(videos)}: {video_id}")
        
        # Use improved transcript fetching with retry logic
        try:
            transcript_text, timestamped_text = get_transcript(video_id)
        except captions_api.QuotaExhausted as e:
            print(f"STOPPING EARLY: {e}")
            print(f"{len(processed)} transcripts written; the remaining videos will be picked up on the next run.")
            break
        
        if transcript_text:
            video['transcript'] = transcript_text
            video['timestamped'] = timestamped_text
            processed.append(video)
            write_markdown(args, video)
            known_ids.add(video_id)
        else:
            print(f"Skipping video {video_id} due to transcript issues.")
            
        # Rate limiting between transcript fetches
        if i < len(videos) - 1:  # Don't sleep after the last video
            delay = random.uniform(10, 30)  # Random delay between 10-30 seconds
            print(f"Waiting {delay:.1f} seconds before next video...")
            time.sleep(delay)
    
    return processed

# YouTube cuts titles at 100 characters, so a longer title is stored (and returned by the API) truncated.
YOUTUBE_TITLE_LIMIT = 100
# A title completed from the description is cut here (at a word boundary), and the filename slug is
# capped separately, so the filename always stays well under the 255 byte limit.
MAX_COMPLETED_TITLE_CHARS = 150
MAX_SLUG_CHARS = 120
# Added to a title that is cut at the limit and cannot be completed.
TRUNCATION_MARK = "\u2026"
# Videos whose truncated title has already been warned about in this run.
_warned_truncated_titles = set()


def video_title(video):
    """The clean title of a video. YouTube's stored title can be cut at its 100 character limit
    ("...AI Driven Operatio"); when it is, the first line of the description is used if it starts with
    the title and continues it. Otherwise the title is marked with an ellipsis, so a reader can see it is
    cut, and a warning is logged once per video (the title is read many times per video)."""
    raw = video['snippet']['title'] or ""
    title = clean_title(raw)
    if len(raw) < YOUTUBE_TITLE_LIMIT:
        return title
    first_line = next((clean_title(line) for line in (video['snippet'].get('description') or "").splitlines()
                       if line.strip()), "")
    if len(first_line) > len(title) and first_line.lower().startswith(title.lower()):
        return truncate_at_word(first_line, MAX_COMPLETED_TITLE_CHARS)
    video_id = get_id(video)
    if video_id not in _warned_truncated_titles:
        _warned_truncated_titles.add(video_id)
        print(f"WARNING: the title of video {video_id} is {len(raw)} characters, YouTube's limit, so it is "
              f"probably truncated and no first line of the description completes it: {title}")
    return title if title.endswith(TRUNCATION_MARK) else title + TRUNCATION_MARK


def truncate_at_word(text, limit):
    """`text` cut to at most `limit` characters at a word boundary."""
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].rstrip(" ,;:-\u2013\u2014") or text[:limit]


REPEATABLE_LINE_MIN_CHARS = 10


def dedupe_description(description):
    """Drop lines that repeat an earlier line of the description (YouTube's default footer often
    repeats a "Thanks for watching!" the author already wrote). Short lines, such as "---" or
    "0:00 Intro", lines with no letter or digit, and blank lines are kept."""
    seen, kept = set(), []
    for line in (description or "").splitlines():
        key = " ".join(line.split())
        # Lines without a letter or digit (markdown rules such as "----------") are layout, not text.
        if len(key) >= REPEATABLE_LINE_MIN_CHARS and any(ch.isalnum() for ch in key):
            if key in seen:
                continue
            seen.add(key)
        kept.append(line)
    # Removing a line can leave a run of blank lines behind.
    return re.sub(r"\n{3,}", "\n\n", "\n".join(kept))


def clean_title(title):
    """Collapse the runs of spaces YouTube titles can carry ("02   Grafana   ObservabilityCON")."""
    return re.sub(r"\s+", " ", title or "").strip()


def file_for_video(args, video):
    """Determines a reasonable local filename for a given video.
    @param args: The command line arguments/user preferences
    @param video: The video object
    @return: A string containing a path to a slugified and dated filename
    """
    published = get_publish(video)
    
    if published == '':
        raise Exception("Could not find publish time for video")

    title = video_title(video)
    slug = slugify(title, max_length=MAX_SLUG_CHARS, word_boundary=True)
    filename = f"{args.path}/{published}-{slug}.md"
    return filename

MODEL = "gpt-4o-mini"

# Used by the summary, cleanup and chapter prompts so product names are spelled consistently.
GLOSSARY = """
Glossary of correct spellings (fix only obvious mishearings of these, for example "O Tel" or
"otel" -> OpenTelemetry/OTel, "Loci" -> Loki):
OpenTelemetry (OTel), OpAmp, Grafana, Grafana Alloy, Grafana Agent, Grafana Cloud, Grafana Labs,
Loki, Tempo, Mimir, Pyroscope, Beyla, OnCall, k6, Faro, Fleet Management, Prometheus, PromQL,
LogQL, TraceQL, Grafana Assistant, Grafana Mimir, Kubernetes, eBPF, GrafanaCON, ObservabilityCON,
Drilldown, Explore Logs, Alertmanager, Grafana Incident, Grafana Machine Learning, LGTM stack.
"""

CONTEXT_RULES = """
Use the video title and description (given below the instructions) for the show name, event date and the
spelling of speaker names. Never guess a spelling that is not in the title or description; if a
name is uncertain, leave it as it is heard.
"""

# The summary must not call a customer talk or a fireside chat a "community call", or invent a date.
EVENT_TYPE_RULES = """
Take the type of the event (for example community call, livestream, webinar, customer talk, fireside
chat, conference session) from the video title and description only. If they do not say what type of
event it is, do not name one: call it a video or a talk. Never state an event date, a show name or an
episode number that is not in the title or description; the published date is not the event date.
"""

# Keep each cleanup request well inside the model's output limit.
CLEANUP_CHUNK_CHARS = 8000
# A cleanup that returns much less text than it was given has probably been truncated or summarised.
MIN_CLEANUP_RATIO = 0.6
# Put a [HH:MM:SS] marker in the chapter input at least this often.
TIMESTAMP_INTERVAL_SECONDS = 45
# Videos whose last [HH:MM:SS] marker is earlier than this are about a minute or two long: chapters
# and a cleaned-up copy would only repeat the raw transcript, so they are left out.
SHORT_VIDEO_SECONDS = 120
# Chapter titles that say nothing; the model is asked again and the chapter is dropped if it persists.
GENERIC_CHAPTER_TITLES = {"discussion", "conversation", "talk", "chat", "intro", "introduction",
                          "overview", "q&a", "qa", "outro", "conclusion"}


def format_timestamp(seconds):
    seconds = int(seconds)
    return f"{seconds // 3600:02d}:{(seconds % 3600) // 60:02d}:{seconds % 60:02d}"


def build_timestamped_text(entries, interval=TIMESTAMP_INTERVAL_SECONDS):
    """Join caption entries into text with a [HH:MM:SS] marker at least every `interval` seconds."""
    parts = []
    last_marker = None
    for entry in entries:
        text, start = entry["text"], entry["start"]
        if last_marker is None or start - last_marker >= interval:
            parts.append(f"\n[{format_timestamp(start)}] ")
            last_marker = start
        parts.append(text + " ")
    return "".join(parts).strip()


def chunk_text(text, limit=CLEANUP_CHUNK_CHARS):
    """Split text into chunks of at most `limit` characters, breaking on word boundaries."""
    chunks, current, size = [], [], 0
    for word in text.split():
        if size + len(word) + 1 > limit and current:
            chunks.append(" ".join(current))
            current, size = [], 0
        current.append(word)
        size += len(word) + 1
    if current:
        chunks.append(" ".join(current))
    return chunks


def video_context(video):
    snippet = video["snippet"]
    return (
        f"Video title: {video_title(video)}\n"
        f"Published: {get_publish(video)}\n"
        f"Description: {snippet['description']}"
    )


def chat(client, system, user, temperature):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        temperature=temperature,
    )
    return response.choices[0].message.content


def openai_cleanup(video, transcript, video_id):
    """
    Take a messy raw YouTube transcript and return a summary + a cleaned up version.
    This only works if OPENAI_API_KEY is set in the environment.
    @param video: The video object (title, date and description give context)
    @param transcript: The raw transcript of a YouTube video, as plain text
    @return: A list containing the summary of the video and the cleaned up transcript
    """
    if openai_key == "":
        print("No OpenAI API key found in .env file; skipping summary and cleanup.")
        return ["Summary not available", None]

    client = openai.OpenAI(api_key=openai_key)
    context = video_context(video)

    summarize_pls = f"""
    You will be given the transcript of a Grafana Labs video.
    Write a summary of 3 to 5 sentences that names the show or event when the title or description
    does, the speakers with their roles (only where the transcript, title or description gives them),
    the Grafana and open source projects and features discussed, and the key takeaways. Then add a
    final line starting with "Topics:" followed by a comma-separated list of the main topics.
    {EVENT_TYPE_RULES}
    {CONTEXT_RULES}
    {GLOSSARY}
    {context}
    """

    print(f"Summarizing transcript for video {video_id}")
    summary = chat(client, summarize_pls, transcript, temperature=0.3)

    cleanup_transcript_prompt = f"""
    You will be given part of a messy transcript of a Grafana Labs video. It has few sentence breaks, indications of music, and filler words. Clean it up into
    logical sentences and paragraphs.

    Output markdown text; you may use markdown formatting for emphasis, bold, bulleting, and so on.

    Stay as close to the original transcript as possible but make it more readable. Do not
    interpret, summarise, add, or remove any words unless they are filler words. Fix only obvious
    mishearings of product and project names. Output the whole part you were given and nothing else.
    {CONTEXT_RULES}
    {GLOSSARY}
    {context}
    """

    print(f"Cleaning up transcript for video {video_id}")
    cleaned_chunks = []
    for chunk in chunk_text(transcript):
        cleaned = chat(client, cleanup_transcript_prompt, chunk, temperature=0.1)
        if len(cleaned) < MIN_CLEANUP_RATIO * len(chunk):
            print(f"Cleanup of a chunk of {video_id} looks truncated; retrying once.")
            cleaned = chat(client, cleanup_transcript_prompt, chunk, temperature=0.1)
            if len(cleaned) < MIN_CLEANUP_RATIO * len(chunk):
                # Summarised text must not be presented as the verbatim transcript.
                print(f"WARNING: cleanup of a chunk of {video_id} is still much shorter than its input; "
                      f"falling back to the raw transcript only.")
                return [summary, None]
        cleaned_chunks.append(cleaned.strip())

    return [summary, "\n\n".join(cleaned_chunks)]


def valid_chapters(chapters, timestamped):
    """Keep only chapter lines whose timestamp appears in the input and that strictly increase."""
    allowed = set(re.findall(r"\[(\d\d:\d\d:\d\d)\]", timestamped))
    allowed.add("00:00:00")
    kept, last = [], -1
    for line in chapters.splitlines():
        line = re.sub(r"^\s*\[(\d\d:\d\d:\d\d)\]", r"\1", line)
        match = re.match(r"^\s*(\d\d):(\d\d):(\d\d)\s+\S", line)
        if not match:
            continue
        stamp = ":".join(match.groups())
        seconds = int(match.group(1)) * 3600 + int(match.group(2)) * 60 + int(match.group(3))
        if stamp in allowed and seconds > last:
            kept.append(line.strip())
            last = seconds
    return "\n".join(kept) or None


def split_windows(timestamped, count):
    """Split marker-annotated text into `count` windows of roughly equal duration.
    Returns a list of (first marker in the window, window text)."""
    pieces = re.split(r"(?=\[\d\d:\d\d:\d\d\] )", timestamped)
    pieces = [p for p in pieces if p.strip()]
    marked = [(p[1:9], p) for p in pieces if p.startswith("[")]
    if not marked:
        return []
    def secs(stamp):
        h, m, s = stamp.split(":")
        return int(h) * 3600 + int(m) * 60 + int(s)
    total = secs(marked[-1][0]) + 1
    windows = [[] for _ in range(count)]
    for stamp, text in marked:
        windows[min(count - 1, secs(stamp) * count // total)].append((stamp, text))
    return [(w[0][0], " ".join(t for _, t in w)) for w in windows if w]


def timestamp_seconds(stamp):
    parts = [int(p) for p in stamp.split(":")]
    seconds = 0
    for part in parts:
        seconds = seconds * 60 + part
    return seconds


def last_marker_seconds(timestamped):
    markers = re.findall(r"\[(\d\d:\d\d:\d\d)\]", timestamped or "")
    return timestamp_seconds(markers[-1]) if markers else 0


def is_short_video(timestamped):
    if not re.search(r"\[\d\d:\d\d:\d\d\]", timestamped or ""):
        return False  # No timing information, so no way to tell.
    return last_marker_seconds(timestamped) < SHORT_VIDEO_SECONDS


def chapter_key(title):
    """Compare chapter titles ignoring case, spacing and punctuation, but keeping letters of any script."""
    return re.sub(r"[\W_]+", "", title.casefold())


def is_generic_title(title):
    return re.sub(r"[^a-z&]", "", title.lower()) in GENERIC_CHAPTER_TITLES


DESCRIPTION_CHAPTER = re.compile(
    r"^\s*(?:[-*\u2022]\s*)?[\[(]?((?:\d{1,2}:)?\d{1,2}:\d\d)[\])]?\s*[-\u2013\u2014:|]?\s*(\S.*?)\s*$")


def description_chapters(description):
    """Human-written chapters from a video description, as "HH:MM:SS Title" lines, or None.

    Follows YouTube's own rules for chapters: at least three, starting at 0:00, increasing."""
    entries, last = [], -1
    for line in (description or "").splitlines():
        match = DESCRIPTION_CHAPTER.match(line)
        if not match:
            continue
        seconds = timestamp_seconds(match.group(1))
        if seconds <= last:
            continue
        entries.append((seconds, match.group(2)))
        last = seconds
    if len(entries) < 3 or entries[0][0] != 0:
        return None
    return "\n".join(f"{format_timestamp(sec)} {title}" for sec, title in entries)


def create_chapters(video, timestamped, video_id):
    """
    Create timestamps and chapters for a YouTube video transcript.
    The transcript is split into equal time windows (about 10 per hour, at least 3) and the model
    names one chapter per window, so the chapters cover the whole video.
    @param video: The video object (title, date and description give context)
    @param timestamped: The transcript with [HH:MM:SS] markers
    @param video_id: The YouTube video ID
    @return: A string containing formatted timestamps and chapters
    """
    if is_short_video(timestamped):
        print(f"Video {video_id} is very short; skipping chapters.")
        return None

    human = description_chapters(video['snippet'].get('description', ''))
    if human:
        print(f"Using the chapters from the description of video {video_id}.")
        return human

    if openai_key == "":
        print("No OpenAI API key found in .env file; skipping chapter creation.")
        return "Chapters not available"

    client = openai.OpenAI(api_key=openai_key)

    markers = re.findall(r"\[(\d\d):(\d\d):(\d\d)\]", timestamped)
    hours = (int(markers[-1][0]) * 3600 + int(markers[-1][1]) * 60 + int(markers[-1][2])) / 3600 if markers else 0
    count = max(3, round(10 * hours))

    chapter_prompt = f"""
    This is one part of a transcript of a Grafana Labs video. It
    contains [HH:MM:SS] markers. Write the title of ONE YouTube chapter for the main topic of this
    part, and the timestamp where that topic starts.

    Rules:
    - The timestamp must be one of the [HH:MM:SS] markers in this part. Never invent one.
    - The title is a short, searchable sentence-case phrase that says what is being discussed.
    - Never use a generic title such as "Discussion", "Introduction" or "Overview"; name the topic.
    - Never repeat the title of an earlier chapter; name what is different in this part.
    - Output one line only, in the form: HH:MM:SS Title
    {CONTEXT_RULES}
    {GLOSSARY}
    {video_context(video)}
    """

    print(f"Creating chapters for video {video_id}")
    lines = []
    used = {}
    first_window_kept = False
    for index, (first_marker, text) in enumerate(split_windows(timestamped, count)):
        line = None
        for attempt in range(2):
            prompt = chapter_prompt
            if used:
                prompt += "\nTitles of the earlier chapters (do not repeat any): " + "; ".join(used.values())
            candidate = valid_chapters(chat(client, prompt, text, temperature=0.1), text)
            if candidate:
                first = candidate.splitlines()[0]
                title = first.split(" ", 1)[1]
                if not is_generic_title(title) and chapter_key(title) not in used:
                    line = first
                    used[chapter_key(title)] = title
                    break
        # No usable title: drop the chapter rather than write "Discussion" or repeat an earlier title
        # (the earlier chapter then simply runs on over this part).
        if line is not None:
            lines.append(line)
            if index == 0:
                first_window_kept = True
    if lines and first_window_kept:
        # The first chapter always starts at 00:00:00 for YouTube.
        lines[0] = "00:00:00" + lines[0][8:]
    chapters = valid_chapters("\n".join(lines), timestamped)
    return chapters or "Chapters not available"


def write_markdown(args, video):
    video_id = get_id(video)
    
    if video_id == '':
        print(f"Could not write markdown for video")
        print(json.dumps(video, indent=2))
        return 

    published = get_publish(video)
    title = video_title(video)
    description = dedupe_description(video['snippet']['description'])
    transcript = video.get('transcript', '')

    if transcript == '':
        print(f"Skipping video {video_id} / {title} because it has no transcript.")
        print(json.dumps(video, indent=2))
        return 

    url = f"https://www.youtube.com/watch?v={video_id}"

    filename = file_for_video(args, video)
    timestamped = video.get('timestamped', transcript)
    short = is_short_video(timestamped)
    [summary, cleaned_up] = openai_cleanup(video, transcript, video_id)
    if short:
        cleaned_up = None  # A cleaned copy of a one-minute video just repeats the raw transcript.
    chapters = create_chapters(video, timestamped, video_id)

    with open(filename, "w") as file:
        file.write(f"# {title}\n\n")
        file.write(f"Published on {published}\n\n")
        file.write(f"## Description\n\n{description}\n\n")
        file.write(f"URL: {url}\n\n")
    
        file.write("## Summary\n\n") 
        file.write(f"{summary}\n\n")
        
        if chapters:
            file.write("## Chapters\n\n")
            file.write(f"{chapters}\n\n")
        
        if cleaned_up:
            # Don't write a heading because OpenAI was instructed to output markdown.
            file.write(f"{cleaned_up}\n\n")

        # TODO: if we're happy with OpenAI output, this is extraneous and can go.
        # The YouTube transcripts are uhm ah well excessively uhm ah accurate.
        file.write("## Raw YouTube Transcript\n\n")
        file.write(f"{transcript}\n\n")

    print(f"Successfully wrote transcript for video {video_id} to {filename}")

SKIPPED_CAPTION_TEXT = ['[Music]', '[Applause]', '[Laughter]']


def entries_to_transcript(transcript, video_id):
    """Turn caption entries ([{"text", "start"}, ...]) from either source into the plain transcript
    text and the text with [HH:MM:SS] markers, or (None, None) if there is too little usable text."""
    # Validate transcript structure
    if not transcript or not isinstance(transcript, list):
        print(f"Invalid transcript format for video {video_id}")
        return None, None

    # Safely extract and clean text
    text_parts = []
    kept_entries = []
    for entry in transcript:
        if isinstance(entry, dict) and 'text' in entry:
            text = entry['text']
            if text and isinstance(text, str):
                text = text.strip()
                # Filter out common non-content entries
                if text and text not in SKIPPED_CAPTION_TEXT:
                    text_parts.append(text)
                    kept_entries.append({'text': text, 'start': float(entry.get('start', 0))})

    if not text_parts:
        print(f"No valid text found in transcript for video {video_id}")
        return None, None

    full_text = ' '.join(text_parts)

    # Minimum length validation
    if len(full_text.strip()) < 50:
        print(f"Transcript too short for video {video_id}: {len(full_text)} characters")
        return None, None

    return full_text, build_timestamped_text(kept_entries)


def get_transcript(video_id):
    """Fetch a transcript from the official captions API when OAuth credentials are configured,
    otherwise from the unofficial youtube_transcript_api. Returns (text, timestamped) or (None, None).
    Raises captions_api.QuotaExhausted when the official API's quota budget is spent."""
    client = get_captions_client()
    if client is None:
        return get_video_transcript_with_retry(video_id)
    entries = client.fetch_entries(video_id)
    if entries is None:
        return None, None
    return entries_to_transcript(entries, video_id)


def get_video_transcript_with_retry(video_id, max_retries=3):
    """
    Fetch transcript with retry logic and exponential backoff.
    Uses the new youtube-transcript-api 1.x API with fallback to deprecated static methods.
    Returns a tuple of the plain transcript text and the text with [HH:MM:SS] markers,
    or (None, None) if unavailable.
    """
    for attempt in range(max_retries):
        try:
            # Try new API first (youtube-transcript-api 1.x)
            try:
                transcript_api = YouTubeTranscriptApi()
                fetched_transcript = transcript_api.fetch(
                    video_id, 
                    languages=['en', 'es', 'fr', 'de', 'ja']  # Fixed 'jp' to 'ja'
                )
                # Convert to the old format (list of dicts)
                transcript = fetched_transcript.to_raw_data()
                
            except (AttributeError, TypeError):
                # Fallback to deprecated static method if new API isn't available
                print(f"Using deprecated static API for video {video_id}")
                transcript = YouTubeTranscriptApi.get_transcript(
                    video_id, 
                    languages=('en', 'es', 'fr', 'de', 'ja')
                )
            
            return entries_to_transcript(transcript, video_id)

        except TranscriptsDisabled:
            print(f"Transcripts are disabled for video {video_id}")
            return None, None
        except NoTranscriptFound:
            print(f"No transcript found for video {video_id}")
            return None, None
        except VideoUnavailable:
            print(f"Video {video_id} is unavailable")
            return None, None
        except Exception as e:
            if attempt < max_retries - 1:
                # Exponential backoff with jitter
                wait_time = (2 ** attempt) + random.uniform(0, 1)
                print(f"Attempt {attempt + 1} failed for video {video_id}. Retrying in {wait_time:.1f}s... Error: {str(e)}")
                time.sleep(wait_time)
            else:
                print(f"All {max_retries} attempts failed for video {video_id}: {str(e)}")
                return None, None
    
    return None, None

def main(args):
    # Add initial delay to let API "cool down"
    initial_delay = random.uniform(5, 15)
    print(f"Starting with {initial_delay:.1f} second delay to avoid rate limiting...")
    time.sleep(initial_delay)
    
    videos_to_transcribe = []

    if args.playlist:
        print("Fetching playlist videos")
        playlist_videos = get_playlist_videos(args.playlist)
        videos_to_transcribe = videos_to_transcribe + playlist_videos
        print(f"Found {len(playlist_videos)} videos in playlist %s" % args.playlist)
        
        # Add delay between different API calls
        if args.channel:
            delay = random.uniform(10, 20)
            print(f"Waiting {delay:.1f} seconds before fetching channel videos...")
            time.sleep(delay)

    if args.channel:
        print("Fetching channel videos")
        channel_videos = get_channel_videos(args.channel, args.start, args.end)
        videos_to_transcribe = videos_to_transcribe + channel_videos
        print(f"Found {len(channel_videos)} videos in the specified date range.")

    known_ids = existing_video_ids(args.path)
    videos_to_transcribe = [v for v in videos_to_transcribe if not should_skip(args, v, known_ids)]
    print(f"Found {len(videos_to_transcribe)} videos to transcribe, after filtering out those that already have transcripts.")

    # The same video can come from both the playlist and the channel; it must not count twice toward --limit.
    seen_ids, unique = set(), []
    for v in videos_to_transcribe:
        if get_id(v) not in seen_ids:
            seen_ids.add(get_id(v))
            unique.append(v)
    videos_to_transcribe = unique

    if args.limit:
        videos_to_transcribe = videos_to_transcribe[:args.limit]
        print(f"Limiting to {args.limit} videos.")

    videos = fetch_transcripts(args, videos_to_transcribe)
    print("Done")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog='transcripts',
            description='Extracts Transcripts from YouTube and writes them as local markdown files')
    parser.add_argument('-c', '--channel', required=False,
                        help='YouTube Channel ID; defaults to Grafana', 
                        default='UCYCwgQAMm9sTJv0rgwQLCxw')
    parser.add_argument('-p', '--playlist', required=False,
                        help='YouTube Playlist ID; defaults to Grafana obscon playlist',
                        default=None)
                        # default='PLDGkOdUX1UjrEOz4fOB4UZW8m-hx8_mtb')
    parser.add_argument('-s', '--start', required=False,
                        help='Start date for videos; Must be in ISO 8601 format. defaults to 2025-01-01T00:00:00Z',
                        default='2025-01-01T00:00:00Z')
    parser.add_argument('-e', '--end', required=False,
                        help='End date for videos; Must be in ISO 8601 format. defaults to 2025-12-31T00:00:00Z',
                        default='2025-12-31T00:00:00Z')
    parser.add_argument('-d', '--path', 
                        help='Path to write markdown files to; defaults to current directory',
                        required=False, default='.')
    parser.add_argument('-l', '--limit', 
                        help='Limit the number of videos to transcribe; defaults to no limit',
                        required=False, default=None, type=int)
    parser.add_argument('--days', type=int, required=False, default=None,
                        help='Only videos published in the last N days (overrides --start and --end); '
                             'used by the weekly GitHub Actions run')
    args = parser.parse_args()

    if args.days is not None:
        now = datetime.now(timezone.utc)
        args.start = (now - timedelta(days=args.days)).strftime('%Y-%m-%dT%H:%M:%SZ')
        # A day ahead so a video published just now is included.
        args.end = (now + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')

    try:
        main(args)
    except captions_api.CaptionsAuthError as e:
        sys.exit(f"ERROR: {e}")
    except captions_api.QuotaExhausted as e:
        # Raised while listing videos, before any transcript was fetched.
        sys.exit(f"ERROR: {e}")
