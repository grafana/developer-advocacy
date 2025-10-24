# YouTube Transcript GitHub Action Setup

This guide explains how to set up the automated YouTube transcript fetching using GitHub Actions.

## Required GitHub Secrets

You need to add the following secrets to your GitHub repository:

### 1. Go to Repository Settings
- Navigate to your repository on GitHub
- Click on **Settings** tab
- Click on **Secrets and variables** → **Actions**

### 2. Add Required Secrets

#### `YOUTUBE_API_KEY`
- **Value**: Your YouTube Data API v3 key
- **How to get**: 
  1. Go to [Google Cloud Console](https://console.cloud.google.com/)
  2. Create a new project or select existing one
  3. Enable YouTube Data API v3
  4. Create credentials (API Key)
  5. Copy the API key

#### `OPENAI_API_KEY`
- **Value**: Your OpenAI API key
- **How to get**:
  1. Go to [OpenAI Platform](https://platform.openai.com/)
  2. Sign in or create account
  3. Go to API Keys section
  4. Create new secret key
  5. Copy the key

## Workflow Configuration

### Single Workflow (`fetch-transcripts.yml`)
- **Schedule**: Every Friday at 8 PM UTC
- **Manual Trigger**: Yes, with limit parameter
- **Channel**: Fixed to UCYCwgQAMm9sTJv0rgwQLCxw (Grafana)
- **Default Limit**: 10 videos
- **Timeout**: 60 minutes
- **Features**: 
  - Better error handling and logging
  - Workflow summaries
  - Automatic commit and push
  - Dependency caching

## Usage

### Automatic Execution
The workflow runs automatically every Friday at 8 PM UTC.

### Manual Execution
1. Go to **Actions** tab in your repository
2. Select **Fetch YouTube Transcripts** workflow
3. Click **Run workflow**
4. Optionally set the **Limit** parameter (default: 10 videos)

## Output

- Transcript files are saved in the `transcripts/` directory
- Files are automatically committed and pushed to the repository
- Each file includes:
  - Video title and description
  - AI-generated summary
  - YouTube-style chapters with timestamps
  - Cleaned-up transcript
  - Raw YouTube transcript

## Troubleshooting

### Common Issues

1. **API Key Errors**
   - Verify secrets are correctly set in repository settings
   - Check that API keys are valid and have proper permissions

2. **Rate Limiting**
   - The workflow includes built-in delays to handle rate limiting
   - If you hit quotas, wait for the next scheduled run

3. **No New Videos**
   - The script skips videos that already have transcripts
   - Check the workflow logs to see how many videos were processed

### Monitoring

- Check the **Actions** tab to see workflow execution history
- View logs for each run to debug issues
- The advanced workflow includes a summary of each run

## Customization

### Changing Schedule
Edit the `cron` expressions in the workflow files:
```yaml
schedule:
  - cron: '0 9 * * 1'  # Every Monday at 9 AM UTC
```

### Adding More Channels
Modify the workflow to include additional channels or playlists.

### Adjusting Rate Limits
Modify the delays in `transcripts.py` if you need different timing.
