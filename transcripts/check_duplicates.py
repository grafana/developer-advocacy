"""Fail when a new transcript is for a YouTube video that already has a transcript file.

The weekly refresh names files after publish time + title slug, so a video that was retitled or
republished can slip in as a second file. The video ID on the `URL:` line is what identifies a video.

Usage (from the repository root or transcripts/):
    python check_duplicates.py --base origin/main     # new files vs. a git ref (used on pull requests)
    python check_duplicates.py                        # every file against every other (informational)
"""
import argparse
import glob
import os
import re
import subprocess
import sys

URL_LINE = re.compile(r"^URL:\s*https?://(?:www\.)?youtube\.com/watch\?v=([A-Za-z0-9_-]+)", re.MULTILINE)
HERE = os.path.dirname(os.path.abspath(__file__))


def video_ids(path):
    with open(path, encoding="utf-8") as file:
        return set(URL_LINE.findall(file.read()))


def find_duplicates(directory, new_files=None):
    """Return {video_id: [filenames...]} for IDs that appear in more than one transcript file.

    With `new_files` (names relative to `directory`), only IDs of those files are checked, against
    every other file in the directory; without it, every ID is."""
    owners = {}
    for path in sorted(glob.glob(os.path.join(directory, "*.md"))):
        name = os.path.basename(path)
        for video_id in video_ids(path):
            owners.setdefault(video_id, []).append(name)
    new = set(new_files) if new_files is not None else None
    return {
        video_id: names for video_id, names in owners.items()
        if len(names) > 1 and (new is None or new.intersection(names))
    }


def git_new_files(base, directory):
    """Transcript files added since `base` (committed, staged or untracked)."""
    def run(*cmd):
        return subprocess.run(cmd, cwd=directory, check=True, capture_output=True, text=True).stdout.split("\n")
    added = run("git", "diff", "--name-only", "--diff-filter=A", "--relative", f"{base}...HEAD", "--", "*.md")
    untracked = run("git", "ls-files", "--others", "--exclude-standard", "--", "*.md")
    return sorted({os.path.basename(n) for n in added + untracked if n.endswith(".md")})


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--base", help="git ref to compare against; only files added since it are checked")
    parser.add_argument("--path", default=HERE, help="directory of transcript .md files")
    args = parser.parse_args(argv)

    new_files = git_new_files(args.base, args.path) if args.base else None
    duplicates = find_duplicates(args.path, new_files)
    if not duplicates:
        checked = f"{len(new_files)} new" if new_files is not None else "all"
        print(f"OK: no duplicate YouTube videos among {checked} transcript file(s).")
        return 0
    for video_id, names in sorted(duplicates.items()):
        print(f"DUPLICATE: https://www.youtube.com/watch?v={video_id} is in {len(names)} files:")
        for name in names:
            print(f"  - {name}")
    print("Remove the newer duplicate(s): the video was retitled or republished.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
