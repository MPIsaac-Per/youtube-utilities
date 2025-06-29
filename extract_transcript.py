import sys
import os
from youtube_transcript_api import YouTubeTranscriptApi
from datetime import datetime
from config import config


def extract_transcript(youtube_url, output_dir=None, channel_name=None, video_date=None, include_metadata=True):
    try:
        video_id = youtube_url.split('v=')[-1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Get video title if requested
        video_title = None
        if include_metadata:
            try:
                # Import here to avoid circular dependency
                import googleapiclient.discovery
                youtube = googleapiclient.discovery.build(
                    "youtube", "v3", developerKey=config.get_current_api_key()
                )
                
                request = youtube.videos().list(
                    part="snippet",
                    id=video_id
                )
                response = request.execute()
                
                if response.get("items"):
                    video_title = response["items"][0]["snippet"]["title"]
                    channel_name = channel_name or response["items"][0]["snippet"]["channelTitle"]
                    video_date = video_date or response["items"][0]["snippet"]["publishedAt"][:10]
            except Exception as e:
                print(f"Could not fetch video metadata: {e}")

        # Convert transcript to markdown format
        md_content = f"# {video_title or 'Transcript'}\n\n" if video_title else ""
        md_content += f"URL: {youtube_url}\n"
        if video_title:
            md_content += f"Title: {video_title}\n"
        if channel_name:
            md_content += f"Channel: {channel_name}\n"
        if video_date:
            md_content += f"Date: {video_date}\n"
        md_content += "\n---\n\n"
        
        for entry in transcript:
            md_content += f"{entry['start']:.2f}s: {entry['text']}\n"

        # Create filename based on available information
        # Use defaults from config if parameters are not provided
        channel_name = channel_name or config.default_channel_name
        video_date = video_date or datetime.now().strftime("%Y-%m-%d")
        output_dir = output_dir or config.output_dir
        
        # Write to markdown file with channel name, video date, and video ID
        output_path = os.path.join(output_dir, f"{channel_name}-{video_date}-{video_id}.md")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"Transcript saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_transcript.py <youtube_url> [channel_name] [video_date]")
        print("Note: channel_name and video_date are optional")
    else:
        youtube_url = sys.argv[1]
        channel_name = sys.argv[2] if len(sys.argv) > 2 else None
        video_date = sys.argv[3] if len(sys.argv) > 3 else None
        config.ensure_output_dir()
        extract_transcript(youtube_url, config.output_dir, channel_name, video_date)