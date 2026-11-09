"""Fetch transcripts through the official YouTube captions API (captions.list + captions.download).

YouTube blocks cloud runners (GitHub Actions and similar) from fetching transcripts the way
youtube_transcript_api does, so scheduled runs use this module instead. It needs OAuth
credentials of a channel manager, because captions.download only works for videos the signed-in
user can edit. See README.md ("How this runs") and get_refresh_token.py for the one-time setup.

The functions that choose a track, parse captions and count quota are plain Python with no network
access so they can be unit tested; only CaptionsClient talks to YouTube.

Environment variables read by credentials_from_env():
    YOUTUBE_OAUTH_CLIENT_ID, YOUTUBE_OAUTH_CLIENT_SECRET, YOUTUBE_OAUTH_REFRESH_TOKEN
    YOUTUBE_QUOTA_BUDGET   optional, units this run may spend (default 9000 of the 10,000/day)
"""
import os
import re

SCOPE = "https://www.googleapis.com/auth/youtube.force-ssl"
TOKEN_URI = "https://oauth2.googleapis.com/token"

# YouTube Data API quota costs, in units. The default project quota is 10,000 units per day.
COST_CAPTIONS_LIST = 50
COST_CAPTIONS_DOWNLOAD = 200
COST_SEARCH_LIST = 100
DAILY_QUOTA = 10000
# Leave headroom below the daily limit for other users of the same Google Cloud project.
DEFAULT_QUOTA_BUDGET = 9000

# Preferred caption languages, most preferred first. Matches the unofficial fetcher's list.
LANGUAGE_PREFERENCE = ("en", "es", "fr", "de", "ja")


class QuotaExhausted(Exception):
    """The daily quota (or this run's budget) cannot cover the next request."""


class CaptionsAuthError(Exception):
    """The OAuth credentials are missing, revoked or expired; a person has to sign in again."""


class QuotaTracker:
    """Counts the quota units spent in this run and refuses requests that would pass the budget."""

    def __init__(self, budget=DEFAULT_QUOTA_BUDGET):
        self.budget = budget
        self.used = 0

    def remaining(self):
        return self.budget - self.used

    def can_afford(self, cost):
        return self.used + cost <= self.budget

    def spend(self, cost):
        """Record `cost` units, or raise QuotaExhausted without recording if over budget."""
        if not self.can_afford(cost):
            raise QuotaExhausted(
                f"Stopping to stay under the YouTube API quota: {self.used} of {self.budget} units "
                f"used in this run (the daily limit is {DAILY_QUOTA}) and the next request costs "
                f"{cost}. Run again after the quota resets (midnight Pacific time)."
            )
        self.used += cost


def credentials_from_env(env=None):
    """Return (client_id, client_secret, refresh_token) if all three are set, else None."""
    env = os.environ if env is None else env
    values = tuple(env.get(name, "").strip() for name in (
        "YOUTUBE_OAUTH_CLIENT_ID", "YOUTUBE_OAUTH_CLIENT_SECRET", "YOUTUBE_OAUTH_REFRESH_TOKEN"))
    return values if all(values) else None


def budget_from_env(env=None):
    env = os.environ if env is None else env
    raw = env.get("YOUTUBE_QUOTA_BUDGET", "").strip()
    if not raw:
        return DEFAULT_QUOTA_BUDGET
    try:
        return max(0, min(int(raw), DAILY_QUOTA))
    except ValueError:
        raise ValueError(f"YOUTUBE_QUOTA_BUDGET must be a whole number, got {raw!r}")


def _language_rank(language):
    """Position of a language code in LANGUAGE_PREFERENCE, or None. "en-GB" counts as "en"."""
    base = (language or "").lower().split("-")[0]
    return LANGUAGE_PREFERENCE.index(base) if base in LANGUAGE_PREFERENCE else None


def choose_track(tracks):
    """Pick the caption track to download from captions.list items, or None.

    Order of preference: a manually uploaded track in the best language, then the auto-generated
    (ASR) track in the best language, with English first. Forced tracks (foreign-parts-only
    subtitles) and drafts are never used. Within a kind, a language earlier in LANGUAGE_PREFERENCE
    wins, and for one language a plain "en" beats "en-GB".
    """
    candidates = []
    for track in tracks:
        snippet = track.get("snippet", {})
        # The API returns "standard", "asr" and "forced" in lower case (the docs say "ASR").
        kind = snippet.get("trackKind", "standard").lower()
        if kind not in ("standard", "asr") or snippet.get("isDraft"):
            continue
        rank = _language_rank(snippet.get("language"))
        if rank is None:
            continue
        # English first: an English auto track beats a manual track in another language.
        # Within the same language a manual track beats an auto one.
        exact = 0 if (snippet.get("language") or "").lower() == LANGUAGE_PREFERENCE[rank] else 1
        candidates.append(((rank, 0 if kind == "standard" else 1, exact), track))
    if not candidates:
        return None
    return min(candidates, key=lambda c: c[0])[1]


_SRT_TIME = re.compile(r"(\d+):(\d\d):(\d\d)[,.](\d{1,3})")
_TAG = re.compile(r"<[^>]+>")


def _srt_seconds(stamp):
    match = _SRT_TIME.fullmatch(stamp.strip())
    if not match:
        return None
    h, m, s, ms = match.groups()
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms.ljust(3, "0")) / 1000


def parse_srt(content):
    """Parse SRT caption text into [{"text": ..., "start": seconds}, ...] in time order.

    This is the entry format transcripts.py already uses for the unofficial fetcher, so the rest
    of the pipeline (filtering, timestamps, cleanup, chapters) does not care where it came from.
    Markup tags are removed and a cue that spans several lines is joined with spaces.
    """
    if isinstance(content, bytes):
        content = content.decode("utf-8-sig", errors="replace")
    content = content.lstrip("﻿").replace("\r\n", "\n").replace("\r", "\n")
    entries = []
    for block in re.split(r"\n\s*\n", content.strip()):
        lines = [line for line in block.split("\n") if line.strip()]
        for i, line in enumerate(lines):
            if "-->" in line:
                start = _srt_seconds(line.split("-->")[0])
                text = " ".join(_TAG.sub("", l).strip() for l in lines[i + 1:])
                text = re.sub(r"\s+", " ", text).strip()
                if start is not None and text:
                    entries.append({"text": text, "start": start})
                break
    return entries


def _http_status(error):
    resp = getattr(error, "resp", None)
    return getattr(resp, "status", None)


def _error_reasons(error):
    """The machine-readable reasons in a googleapiclient HttpError, such as quotaExceeded."""
    try:
        import json
        body = json.loads(error.content.decode("utf-8"))
        return [e.get("reason", "") for e in body.get("error", {}).get("errors", [])]
    except Exception:
        return []


class CaptionsClient:
    """Downloads caption tracks with an authenticated YouTube client.

    `youtube` is the object returned by googleapiclient.discovery.build(...).
    """

    def __init__(self, youtube, quota=None, log=print):
        self.youtube = youtube
        self.quota = quota or QuotaTracker()
        self.log = log

    def _execute(self, request, cost):
        from googleapiclient.errors import HttpError
        self.quota.spend(cost)
        try:
            return request.execute()
        except HttpError as error:
            reasons = _error_reasons(error)
            if any(r in ("quotaExceeded", "dailyLimitExceeded", "rateLimitExceeded") for r in reasons):
                raise QuotaExhausted(
                    "YouTube reports the API quota is used up for today. Run again after it "
                    "resets (midnight Pacific time).") from error
            raise
        except Exception as error:
            # google.auth.exceptions.RefreshError is raised when the refresh token is revoked.
            if type(error).__name__ == "RefreshError":
                raise CaptionsAuthError(
                    "YouTube rejected the OAuth refresh token (it was revoked or expired). A channel "
                    "manager needs to sign in again with get_refresh_token.py and the refresh "
                    "token in Vault must be replaced. See README.md.") from error
            raise

    def list_tracks(self, video_id):
        response = self._execute(
            self.youtube.captions().list(part="snippet", videoId=video_id), COST_CAPTIONS_LIST)
        return response.get("items", [])

    def fetch_entries(self, video_id):
        """Return caption entries [{"text", "start"}] for a video, or None if it has no usable track.

        Raises QuotaExhausted when the quota is spent and CaptionsAuthError when the credentials
        no longer work. Any other failure for one video returns None so the run continues.
        """
        from googleapiclient.errors import HttpError
        try:
            tracks = self.list_tracks(video_id)
            track = choose_track(tracks)
            if track is None:
                self.log(f"No usable caption track for video {video_id} ({len(tracks)} tracks listed).")
                return None
            snippet = track["snippet"]
            self.log(f"Downloading {snippet.get('trackKind')} {snippet.get('language')} captions for {video_id}")
            content = self._execute(
                self.youtube.captions().download(id=track["id"], tfmt="srt"), COST_CAPTIONS_DOWNLOAD)
        except HttpError as error:
            status = _http_status(error)
            if status == 404:
                self.log(f"Video {video_id} was not found or has no captions.")
            elif status == 403:
                self.log(f"Not allowed to download captions for video {video_id} (is the signed-in "
                         f"account a manager of the channel that owns it?): {error}")
            else:
                self.log(f"Could not fetch captions for video {video_id}: {error}")
            return None
        entries = parse_srt(content)
        return entries or None


def build_youtube_client(client_id, client_secret, refresh_token):
    """An authenticated YouTube Data API client that refreshes its access token automatically."""
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    credentials = Credentials(
        token=None, refresh_token=refresh_token, client_id=client_id,
        client_secret=client_secret, token_uri=TOKEN_URI, scopes=[SCOPE])
    return build("youtube", "v3", credentials=credentials, cache_discovery=False)
