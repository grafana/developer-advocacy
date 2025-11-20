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