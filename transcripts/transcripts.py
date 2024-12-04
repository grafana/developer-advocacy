import os
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
from slugify import slugify
import json
import sys

load_dotenv()

# Set up your YouTube API key
# This is inherited from .env
API_KEY = os.environ.get('API_KEY')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def get_playlist_videos(playlist_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
    
    video_ids = []
    next_page_token = None

    # This returns a list of youtube:playlistItem
    while True:
        request = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=10,
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            video_ids.append(item['snippet']['resourceId']['videoId'])
        
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    # This gets all of the details of each video by ID
    videos = []
    next_page_token = None
    while True:
        request = youtube.videos().list(
            part='snippet',
            id=','.join(video_ids),
            pageToken=next_page_token
        )

        response = request.execute()
        for item in response['items']:
            print("Found detail")
            print(json.dumps(item, indent=2))
            videos.append(item)
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return videos

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

def get_publish(video):
    snippet = video['snippet']

    if 'publishTime' in snippet:
        return snippet['publishTime']
    return snippet['publishedAt']

def get_id(video):
    if type(video['id']) == str:
        return video['id']
    
    return video['id']['videoId']

def fetch_transcripts(videos):
    processed = []
    for video in videos:
        video_id = get_id(video)
        
        if video_id == '':
            print(f"Could not find video ID for video ")
            print(json.dumps(video, indent=2))
            continue

        if os.path.isfile(file_for_video(video)):
            print(f"Skipping video {video_id} because it already has a transcript.")
            continue

        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=('en','es', 'fr', 'de'))
            full_text = ' '.join([entry['text'] for entry in transcript])
            video['transcript'] = full_text
            processed.append(video)
        except Exception as e:
            print(f"Could not fetch transcript for video {video_id}: {e}")
    
    return processed

def file_for_video(video):
    published = get_publish(video)
    
    if published == '':
        raise Exception("Could not find publish time for video")

    title = video['snippet']['title']
    slug = slugify(title)
    filename = f"{published}-{slug}.md"
    return filename

def write_markdown(video):
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

playlists = ['PLDGkOdUX1UjrEOz4fOB4UZW8m-hx8_mtb']

def have_transcript_file(video):
    return os.path.isfile(file_for_video(video))

def main():
    channel_id = 'UCYCwgQAMm9sTJv0rgwQLCxw'  # Replace with the target channel's ID
    start_date = '2024-01-01T00:00:00Z'  # Replace with your start date in ISO 8601 format
    end_date = '2025-12-31T00:00:00Z'  # Replace with your end date in ISO 8601 format

    videos_to_transcribe = []

    for playlist in playlists:
        playlist_videos = get_playlist_videos(playlist)
        videos_to_transcribe = videos_to_transcribe + playlist_videos
        print(f"Found {len(playlist_videos)} videos in plalyst %s" % playlist)

    channel_videos = get_channel_videos(channel_id, start_date, end_date)
    videos_to_transcribe = videos_to_transcribe + channel_videos
    print(f"Found {len(channel_videos)} videos in the specified date range.")

    videos_to_transcribe = [v for v in videos_to_transcribe if not have_transcript_file(v)]
    print(f"Found {len(videos_to_transcribe)} videos to transcribe, after filtering out those that already have transcripts.")

    videos = fetch_transcripts(videos_to_transcribe)

    for video in videos:
       write_markdown(video)

if __name__ == "__main__":
    main()
