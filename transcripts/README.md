# YouTube Transcripts

This directory contains a script that automatically fetches transcripts from YouTube videos, processes them with AI, and generates comprehensive markdown files with summaries, chapters, and cleaned-up content.

## What the Script Does

The `transcripts.py` script performs the following operations:

1. **Fetches Video Metadata**: Retrieves video information from the YouTube Data API v3
2. **Downloads Transcripts**: Gets raw transcripts from YouTube's automatic captions
3. **AI Processing**: Uses OpenAI to:
   - Generate concise summaries of each video
   - Clean up and improve transcript readability
   - Create YouTube-style chapters with timestamps
4. **Rate Limiting**: Includes built-in delays to respect API limits:
   - 5-15 second random delays between pagination requests
   - 10-30 second random delays between video processing
   - Initial 5-15 second delay before starting
5. **Smart Skipping**: Automatically skips videos that already have transcript files
6. **Markdown Generation**: Creates comprehensive markdown files with:
   - Video title, description, and URL
   - AI-generated summary
   - YouTube-style chapters with timestamps
   - Cleaned-up transcript
   - Raw YouTube transcript

## How this runs

The transcripts are refreshed automatically every week by the GitHub Actions workflow
[`.github/workflows/refresh-transcripts.yml`](../.github/workflows/refresh-transcripts.yml).

- **Owners:** [@nicolevanderhoeven](https://github.com/nicolevanderhoeven) and [@moxious](https://github.com/moxious) (David Allen), listed in `.github/CODEOWNERS`.
- **Schedule:** Mondays at 06:17 UTC.
- **What it does:** fetches transcripts of videos published in the last 14 days (the official YouTube captions API; auto-generated English captions are used when there is no manual track), writes summaries, chapters and cleaned-up text with OpenAI, regenerates `recurring-shows.md` and `community-calls.md`, and opens a pull request labelled `devrel`. It never commits directly. Review the PR (skim the new transcripts) and merge it.
- **Secrets:** none are stored in GitHub. The workflow reads them from Vault (`ci/repo/grafana/developer-advocacy/`) at run time with `grafana/shared-workflows/actions/get-vault-secrets` and GitHub OIDC: `youtube-transcripts` (`client_id`, `client_secret`, `refresh_token`) and `openai` (`api_key`).
- **Why the official API:** YouTube blocks cloud runners (and now many home connections) from the unofficial `youtube_transcript_api` the script used before. The official `captions.list` + `captions.download` calls cost 250 quota units per video, so a normal week (about 10 videos) uses roughly 2,700 of the 10,000 daily units. The run stops cleanly with a message when it nears the budget (`YOUTUBE_QUOTA_BUDGET`, default 9000); the videos left over are picked up next week.

### Run it manually

Actions tab, "Refresh YouTube transcripts", "Run workflow". Set `days` to go further back and tick `dry_run` to fetch and regenerate without opening a PR. Or from a terminal: `gh workflow run refresh-transcripts.yml -f days=30`.

### If it fails

GitHub emails the people who last changed the schedule or triggered the run when a scheduled run fails. Check the run log:

- **`YouTube rejected the OAuth refresh token`**: the token was revoked (the channel manager who signed in left, changed their password or removed the app). Sign in again with the steps below and replace `refresh_token` in Vault.
- **`Stopping to stay under the YouTube API quota`**: normal after a large backfill. Re-run after midnight Pacific time.
- **Vault errors**: check the secrets still exist under `ci/repo/grafana/developer-advocacy/` and ask the platform team.
- **PR step fails**: the repo setting "Allow GitHub Actions to create and approve pull requests" must be on, and the `devrel` label must exist.
- **Not allowed to download captions for video ...**: the signed-in account must be a manager of the channel that owns the video.

### One-time OAuth setup (channel manager)

The OAuth consent screen of the Google Cloud project is "In production" (checked 2026-11-09), so refresh tokens do not expire after 7 days.

1. In the Google Cloud project (YouTube Data API v3 enabled), create an OAuth client of type **Desktop app**. Note the client ID and secret.
2. As a person who can edit the channel's videos, run `python3 get_refresh_token.py` in this directory (standard library only). It asks for the client ID and secret, opens your browser, and prints a refresh token to the terminal. Nothing is written to disk.
3. Give the client ID, client secret and refresh token to the platform team to store in Vault (never in the repo, an issue, chat or a GitHub secret).
4. Run the workflow manually with `dry_run` ticked to check it works.

To use the official API locally, set `YOUTUBE_OAUTH_CLIENT_ID`, `YOUTUBE_OAUTH_CLIENT_SECRET` and `YOUTUBE_OAUTH_REFRESH_TOKEN` in `.env`. Without them the script falls back to the unofficial API, which only works from some home or office connections. Use `python3 transcripts.py --days 14` for the same window as the weekly run, and `python3 -m unittest discover -s tests` for the tests.

## Quickstart

The easiest way to get started is to use the provided setup script:

```bash
cd transcripts
./run.sh
```

This script will automatically:
- Verify all required files exist (requirements.txt, transcripts.py, .env)
- Create and activate a virtual environment
- Install dependencies
- Run the transcripts script

If any required files are missing, the script will provide helpful instructions.

## Local Setup (Manual)

If you prefer to set things up manually or want more control:

### 1. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### 2. Configure Environment Variables
```bash
# Copy the example environment file
cp env.example .env

# Edit .env and add your API keys
nano .env
```

Required environment variables:
- `API_KEY`: Your YouTube Data API v3 key
- `OPENAI_API_KEY`: Your OpenAI API key (for AI processing)

### 3. Get API Keys

#### YouTube Data API v3 Key:
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable YouTube Data API v3
4. Create credentials (API Key)
5. Copy the API key to your `.env` file

#### OpenAI API Key:
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign in or create account
3. Go to API Keys section
4. Create new secret key
5. Copy the key to your `.env` file

## Running the Script Locally

### Basic Usage
```bash
# Process up to 10 videos from the Grafana channel
python3 transcripts.py

# Process a specific number of videos
python3 transcripts.py -l 5

# Process videos from a specific date range
python3 transcripts.py -s 2025-01-01T00:00:00Z -e 2025-12-31T23:59:59Z

# Process videos from a specific playlist
python3 transcripts.py -p PLAYLIST_ID
```

### Command Line Options
- `-l, --limit`: Limit number of videos to process
- `-c, --channel`: YouTube channel ID (default: UCYCwgQAMm9sTJv0rgwQLCxw)
- `-p, --playlist`: YouTube playlist ID
- `-s, --start`: Start date (ISO 8601 format)
- `-e, --end`: End date (ISO 8601 format)

## Output Files

Transcript files are saved in the `transcripts/` directory with the format:
`YYYY-MM-DDTHH:MM:SSZ-video-title.md`

Each file contains:
- Video metadata (title, description, URL, publish date)
- AI-generated summary
- YouTube-style chapters with timestamps
- Cleaned-up transcript
- Raw YouTube transcript

## Recurring Shows Index

`recurring-shows.md` is a single index of every recurring show on the channel: all community calls (Loki, Tempo, Mimir, Alloy, Beyla, Pyroscope, OnCall, OpenTelemetry and Campfire), Office Hours, The Context Window, Grafana for Beginners, Zero to Hero: Loki, Café con Grafana and other series. Shows are grouped by show, episodes are listed newest first, and each line has the date, title, a one-line topic and the YouTube link. The file is generated from the transcript files and should not be edited by hand. `community-calls.md` is a short generated file that points to the community call sections.

The show-detection rules (title patterns) are listed at the top of `recurring_shows_index.py`. A title containing "community call" is a community call; other series are recognised by title patterns such as "Office Hours" or "The Context Window". To add a new show, add a pattern to `SERIES_SHOWS` (or a product to `COMMUNITY_CALL_SHOWS`). The script prints any title that looks like an episode of an unknown series ("Ep 3", "#12", "Part 2") on stderr so new shows are noticed.

After fetching new transcripts, regenerate the index (standard library only, no API keys or virtual environment needed):

```bash
python3 recurring_shows_index.py
```

## Troubleshooting

### Common Issues
1. **API Key Errors**: Verify your API keys are correct and have proper permissions
2. **Rate Limiting**: The script includes built-in delays, but you may need to wait if you hit quotas
3. **No New Videos**: The script skips videos that already have transcripts
4. **Network Issues**: Check your internet connection and try again

### Rate Limiting
The script includes aggressive rate limiting to handle API quotas:
- Random delays between 5-15 seconds for pagination
- Random delays between 10-30 seconds between videos
- Initial delay of 5-15 seconds before starting

If you still encounter rate limiting issues, try reducing the limit or waiting between runs.