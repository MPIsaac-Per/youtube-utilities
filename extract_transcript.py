import sys
import os
from youtube_transcript_api import YouTubeTranscriptApi


def extract_transcript(youtube_url, channel_name, output_dir):
    try:
        video_id = youtube_url.split('v=')[-1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Convert transcript to markdown format
        md_content = f"URL: {youtube_url}\n\n"
        for entry in transcript:
            md_content += f"{entry['start']:.2f}s: {entry['text']}\n"

        # Write to markdown file with channel name and video ID
        output_path = os.path.join(output_dir, f"{channel_name}-{video_id}.md")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"Transcript saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_transcript.py <youtube_url> <channel_name>")
    else:
        youtube_url = sys.argv[1]
        channel_name = sys.argv[2]
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        extract_transcript(youtube_url, channel_name, output_dir)