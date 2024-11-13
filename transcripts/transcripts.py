import os
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
#from dotenv import load_dotenv
from slugify import slugify
import json

#load_dotenv()

# Set up your YouTube API key
# This is inherited from .env
API_KEY = os.environ.get('API_KEY')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def get_channel_videos(channel_id, start_date, end_date):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
    
    videos = []
    next_page_token = None

    while True:
        request = youtube.search().list(
            part='snippet',
            channelId=channel_id,
            maxResults=10,
            order='date',
            publishedAfter=start_date,
            publishedBefore=end_date,
            type='video',
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            videos.append(item)            

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break
    
    return videos

def fetch_transcripts(videos):
    processed = []
    for video in videos:
        video_id = video['id']['videoId']

        if os.path.isfile(file_for_video(video)):
            print("Skipping video {video_id} because it already has a transcript.")
            continue

        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            full_text = ' '.join([entry['text'] for entry in transcript])
            video['transcript'] = full_text
            processed.append(video)
        except Exception as e:
            print(f"Could not fetch transcript for video {video_id}: {e}")
    
    return processed

def file_for_video(video):
    published = video['snippet']['publishTime'] 
    title = video['snippet']['title']
    slug = slugify(title)
    filename = f"{published}-{slug}.md"
    return filename

def write_markdown(video):
    video_id = video['id']['videoId']
    published = video['snippet']['publishTime'] 
    title = video['snippet']['title']
    description = video['snippet']['description']
    transcript = video.get('transcript', '')

    if transcript == '':
        print(f"Skipping video {video_id} / {title} because it has no transcript.")
        return 

    url = f"https://www.youtube.com/watch?v={video_id}"

    filename = file_for_video(video)
    with open(filename, "w") as file:
        file.write(f"# {title}\n\n")
        file.write(f"{description}\n\n")
        file.write(f"Published on {published}\n\n")
        file.write(f"URL: {url}\n\n")
        file.write(f"Transcript: {transcript}\n\n")

    print(f"Successfully wrote transcript for video {video_id} to {filename}")

def main():
    channel_id = 'UCYCwgQAMm9sTJv0rgwQLCxw'  # Replace with the target channel's ID
    start_date = '2024-01-01T00:00:00Z'  # Replace with your start date in ISO 8601 format
    end_date = '2024-11-07T00:00:00Z'  # Replace with your end date in ISO 8601 format

    videos = get_channel_videos(channel_id, start_date, end_date)
    print(f"Found {len(videos)} videos in the specified date range.")

    videos = fetch_transcripts(videos)

    for video in videos:
        write_markdown(video)

if __name__ == "__main__":
    main()