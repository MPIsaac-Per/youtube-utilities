import os
import subprocess
import sys
import googleapiclient.discovery

# Initialize the YouTube API client
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyCnr4HOnuDCoUv0jJ7TMy9zZ5TwWsVnrc8"  # Replace with your actual API key

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

# Function to get channel ID from channel name
def get_channel_id_from_name(channel_name):
    request = youtube.search().list(
        part="snippet",
        q=channel_name,
        type="channel",
        maxResults=1
    )
    response = request.execute()

    for item in response.get("items", []):
        if item["id"].get("channelId"):
            return item["id"]["channelId"]
    return None

# Function to get video URLs and dates from a channel
def get_video_urls_and_dates_from_channel(channel_id, max_videos):
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=max_videos,  # Use the max_videos parameter
        order="date"  # Sort by newest first
    )
    response = request.execute()

    video_data = []
    for item in response.get("items", []):
        if item["id"].get("videoId"):
            video_id = item["id"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            video_date = item["snippet"]["publishedAt"][:10]  # Extract date part
            video_data.append((video_url, video_date))

    return video_data

# Main function to process videos
def main(channel_name, max_videos):
    channel_id = get_channel_id_from_name(channel_name)
    if not channel_id:
        print(f"Channel not found for name: {channel_name}")
        return

    video_data = get_video_urls_and_dates_from_channel(channel_id, max_videos)
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    python_executable = os.path.join('.venv', 'Scripts', 'python.exe')

    for url, video_date in video_data:
        subprocess.run([python_executable, "extract_transcript.py", url, channel_name, video_date])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fetch_and_extract.py channelname max_videos")
    else:
        channel_name = sys.argv[1]
        max_videos = int(sys.argv[2])
        main(channel_name, max_videos)
