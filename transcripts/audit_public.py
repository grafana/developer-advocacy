"""Fail when a transcript in this (public) repository is for a YouTube video that is not public.

The generator only writes transcripts of public videos, but a file can still be added by hand, or a
video can be made private or unlisted after its transcript was committed. This asks the YouTube Data API
(plain API key, no OAuth) for the privacy status of every video ID found in the transcript files.

A video the API does not return for an API key (private, deleted, or an invalid ID) counts as not public.

The output is meant for public CI logs: it prints COUNTS ONLY, never IDs, titles or file names of
non-public videos. To see which files are affected, run it locally with --details:

    YOUTUBE_API_KEY=... python audit_public.py --details

Exit codes: 0 all public, 1 at least one transcript is not public, 2 the audit could not run.
"""
import argparse
import glob
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

from check_duplicates import HERE, video_ids

API_URL = "https://www.googleapis.com/youtube/v3/videos"
BATCH_SIZE = 50  # the API's limit of IDs per videos.list call


class AuditError(Exception):
    """The audit could not be completed (API or network problem). Never carries the API key."""


def transcript_videos(directory):
    """{video_id: [file names]} for every transcript file in `directory`."""
    owners = {}
    for path in sorted(glob.glob(os.path.join(directory, "*.md"))):
        for video_id in video_ids(path):
            owners.setdefault(video_id, []).append(os.path.basename(path))
    return owners


def fetch_privacy(video_ids_, api_key, urlopen=urllib.request.urlopen):
    """{video_id: privacyStatus} for the videos the API returns. Missing IDs are not in the result."""
    found = {}
    ids = list(video_ids_)
    for start in range(0, len(ids), BATCH_SIZE):
        query = urllib.parse.urlencode({"part": "status", "id": ",".join(ids[start:start + BATCH_SIZE]),
                                        "maxResults": BATCH_SIZE})
        # The key goes in a header, not the URL, so it can never end up in an error message.
        request = urllib.request.Request(f"{API_URL}?{query}", headers={"x-goog-api-key": api_key})
        try:
            with urlopen(request, timeout=30) as response:
                body = json.load(response)
        except urllib.error.HTTPError as error:
            raise AuditError(f"the YouTube API answered HTTP {error.code}") from None
        except (urllib.error.URLError, TimeoutError, ValueError) as error:
            raise AuditError(f"the YouTube API request failed ({type(error).__name__})") from None
        for item in body.get("items", []):
            found[item["id"]] = (item.get("status") or {}).get("privacyStatus")
    return found


def find_not_public(directory, api_key, urlopen=urllib.request.urlopen):
    """(total number of videos checked, {video_id: [file names]} of those that are not public)."""
    owners = transcript_videos(directory)
    privacy = fetch_privacy(owners, api_key, urlopen)
    return len(owners), {vid: names for vid, names in owners.items() if privacy.get(vid) != "public"}


def main(argv=None, urlopen=urllib.request.urlopen):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--path", default=HERE, help="directory of transcript .md files")
    parser.add_argument("--details", action="store_true",
                        help="also list the affected file names and video IDs; only for a private terminal")
    args = parser.parse_args(argv)

    api_key = os.environ.get("YOUTUBE_API_KEY") or os.environ.get("API_KEY")
    if not api_key:
        print("Cannot audit: set YOUTUBE_API_KEY (a YouTube Data API key).")
        return 2
    try:
        total, not_public = find_not_public(args.path, api_key, urlopen)
    except AuditError as error:
        print(f"Cannot audit: {error}.")
        return 2

    if not not_public:
        print(f"OK: all {total} transcript video(s) are public.")
        return 0
    files = sum(len(names) for names in not_public.values())
    print(f"NOT PUBLIC: {len(not_public)} of {total} transcript video(s) ({files} file(s)) are not public.")
    if args.details:
        for video_id, names in sorted(not_public.items()):
            print(f"  {video_id}: {', '.join(names)}")
    else:
        print("Details are left out because the logs of this repository are public. "
              "Run `YOUTUBE_API_KEY=... python transcripts/audit_public.py --details` locally to list them.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
