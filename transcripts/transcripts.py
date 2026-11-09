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

load_dotenv()

# Env var setup
# If this first one is missing, run fails, which is good.
youtube_key = os.environ.get('API_KEY')
# Second one is optional, but if it's missing, we'll skip the summary and cleanup.
openai_key = os.environ.get("OPENAI_API_KEY","")

def get_playlist_videos(playlist_id):
    youtube = build('youtube', 'v3', developerKey=youtube_key)
    
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
                part='snippet',
                id=','.join(batch_ids)
            )
            response = request.execute()
            
            for item in response['items']:
                print(f"Found video: {item['snippet']['title']}")
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
    youtube = build('youtube', 'v3', developerKey=youtube_key)
    
    videos = []
    next_page_token = None
    page_count = 0
    max_pages = 20  # Safety limit: 20 pages of 50 videos

    while page_count < max_pages:
        try:
            # Build request parameters
            request_params = {
                'part': 'snippet',
                'channelId': channel_id,
                'maxResults': 50,
                'order': 'date',
                'type': 'video',
                'publishedAfter': start_date,
                'publishedBefore': end_date
            }
            
            # Only add pageToken if it's not None
            if next_page_token:
                request_params['pageToken'] = next_page_token
                
            request = youtube.search().list(**request_params)
            print(f"Making API request with params: {request_params}")
            response = request.execute()
            print(f"API request successful, got {len(response.get('items', []))} videos")

            for item in response['items']:
                videos.append(item)            

            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break
                
            # Rate limiting between pagination requests
            delay = random.uniform(5, 15)  # Random delay between 5-15 seconds
            print(f"Waiting {delay:.1f} seconds before next page...")
            time.sleep(delay)
            page_count += 1
            
        except HttpError as e:
            if e.resp.status == 403 and 'quota' in str(e).lower():
                print("Quota exceeded while searching channel videos. Waiting before retry...")
                time.sleep(60)  # Wait 1 minute
                continue
            else:
                print(f"Error searching channel videos: {e}")
                raise
    
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

def fetch_transcripts(args, videos):
    processed = []
    for i, video in enumerate(videos):
        video_id = get_id(video)
        
        if video_id == '':
            print(f"Could not find video ID for video ")
            print(json.dumps(video, indent=2))
            continue

        if os.path.isfile(file_for_video(args, video)):
            print(f"Skipping video {video_id} because it already has a transcript.")
            continue

        print(f"Processing video {i+1}/{len(videos)}: {video_id}")
        
        # Use improved transcript fetching with retry logic
        transcript_text, timestamped_text = get_video_transcript_with_retry(video_id)
        
        if transcript_text:
            video['transcript'] = transcript_text
            video['timestamped'] = timestamped_text
            processed.append(video)
            write_markdown(args, video)
        else:
            print(f"Skipping video {video_id} due to transcript issues.")
            
        # Rate limiting between transcript fetches
        if i < len(videos) - 1:  # Don't sleep after the last video
            delay = random.uniform(10, 30)  # Random delay between 10-30 seconds
            print(f"Waiting {delay:.1f} seconds before next video...")
            time.sleep(delay)
    
    return processed

def file_for_video(args, video):
    """Determines a reasonable local filename for a given video.
    @param args: The command line arguments/user preferences
    @param video: The video object
    @return: A string containing a path to a slugified and dated filename
    """
    published = get_publish(video)
    
    if published == '':
        raise Exception("Could not find publish time for video")

    title = video['snippet']['title']
    slug = slugify(title)
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
Use the video title and description (given below the instructions) for the show name, date and the
spelling of speaker names. Never guess a spelling that is not in the title or description; if a
name is uncertain, leave it as it is heard.
"""

# Keep each cleanup request well inside the model's output limit.
CLEANUP_CHUNK_CHARS = 8000
# A cleanup that returns much less text than it was given has probably been truncated or summarised.
MIN_CLEANUP_RATIO = 0.6
# Put a [HH:MM:SS] marker in the chapter input at least this often.
TIMESTAMP_INTERVAL_SECONDS = 45


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
        f"Video title: {snippet['title']}\n"
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
    You will be given the transcript of a Grafana Labs community call, livestream or talk.
    Write a summary of 3 to 5 sentences that names the show and its date, the speakers with their
    roles (only where the transcript, title or description gives them), the Grafana and open source
    projects and features discussed, and the key takeaways. Then add a final line starting with
    "Topics:" followed by a comma-separated list of the main topics.
    {CONTEXT_RULES}
    {GLOSSARY}
    {context}
    """

    print(f"Summarizing transcript for video {video_id}")
    summary = chat(client, summarize_pls, transcript, temperature=0.3)

    cleanup_transcript_prompt = f"""
    You will be given part of a messy transcript of a Grafana Labs community call, livestream or
    talk. It has few sentence breaks, indications of music, and filler words. Clean it up into
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
                print(f"WARNING: cleanup of a chunk of {video_id} is much shorter than its input.")
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
    if openai_key == "":
        print("No OpenAI API key found in .env file; skipping chapter creation.")
        return "Chapters not available"

    client = openai.OpenAI(api_key=openai_key)

    markers = re.findall(r"\[(\d\d):(\d\d):(\d\d)\]", timestamped)
    hours = (int(markers[-1][0]) * 3600 + int(markers[-1][1]) * 60 + int(markers[-1][2])) / 3600 if markers else 0
    count = max(3, round(10 * hours))

    chapter_prompt = f"""
    This is one part of a transcript of a Grafana Labs community call, livestream or talk. It
    contains [HH:MM:SS] markers. Write the title of ONE YouTube chapter for the main topic of this
    part, and the timestamp where that topic starts.

    Rules:
    - The timestamp must be one of the [HH:MM:SS] markers in this part. Never invent one.
    - The title is a short, searchable sentence-case phrase that says what is being discussed.
    - Output one line only, in the form: HH:MM:SS Title
    {CONTEXT_RULES}
    {GLOSSARY}
    {video_context(video)}
    """

    print(f"Creating chapters for video {video_id}")
    lines = []
    for index, (first_marker, text) in enumerate(split_windows(timestamped, count)):
        line = None
        for attempt in range(2):
            candidate = valid_chapters(chat(client, chapter_prompt, text, temperature=0.1), text)
            if candidate:
                line = candidate.splitlines()[0]
                break
        if line is None:
            line = f"{first_marker} Discussion"
        # The first chapter always starts at 00:00:00 for YouTube.
        if index == 0:
            line = "00:00:00" + line[8:]
        lines.append(line)
    chapters = valid_chapters("\n".join(lines), timestamped)
    return chapters or "Chapters not available"


def write_markdown(args, video):
    video_id = get_id(video)
    
    if video_id == '':
        print(f"Could not write markdown for video")
        print(json.dumps(video, indent=2))
        return 

    published = get_publish(video)
    title = video['snippet']['title']
    description = video['snippet']['description']
    transcript = video.get('transcript', '')

    if transcript == '':
        print(f"Skipping video {video_id} / {title} because it has no transcript.")
        print(json.dumps(video, indent=2))
        return 

    url = f"https://www.youtube.com/watch?v={video_id}"

    filename = file_for_video(args, video)
    [summary, cleaned_up] = openai_cleanup(video, transcript, video_id)
    chapters = create_chapters(video, video.get('timestamped', transcript), video_id)

    with open(filename, "w") as file:
        file.write(f"# {title}\n\n")
        file.write(f"Published on {published}\n\n")
        file.write(f"## Description\n\n{description}\n\n")
        file.write(f"URL: {url}\n\n")
    
        file.write("## Summary\n\n") 
        file.write(f"{summary}\n\n")
        
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

def have_transcript_file(args, video):
    return os.path.isfile(file_for_video(args, video))

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
                        if text and text not in ['[Music]', '[Applause]', '[Laughter]']:
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

    videos_to_transcribe = [v for v in videos_to_transcribe if not have_transcript_file(args, v)]
    print(f"Found {len(videos_to_transcribe)} videos to transcribe, after filtering out those that already have transcripts.")

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
    args = parser.parse_args()

    main(args)
