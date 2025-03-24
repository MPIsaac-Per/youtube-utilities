# YouTube Utilities

A collection of Python utilities for fetching and extracting YouTube video transcripts.

## Setup

1. Create a virtual environment:
   ```
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - Windows:
     ```
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```
     source .venv/bin/activate
     ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Scripts

### 1. extract_transcript.py

**Description:** Extracts transcripts from YouTube videos and saves them as markdown files.

**Usage:**
```
python extract_transcript.py <youtube_url> [channel_name] [video_date]
```

**Parameters:**
- `youtube_url`: URL of the YouTube video (required)
- `channel_name`: Name of the YouTube channel (optional)
- `video_date`: Date of the video in YYYY-MM-DD format (optional)

**Example:**
```
python extract_transcript.py https://www.youtube.com/watch?v=dQw4w9WgXcQ IndyDevDan 2023-01-01
```

**Output:**
Generates a markdown file in the `output` directory with the transcript formatted as:
```
URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ

0.00s: First line of transcript
2.50s: Second line of transcript
...
```

### 2. fetch_and_extract.py

**Description:** Fetches recent videos from a YouTube channel and extracts their transcripts.

**Usage:**
```
python fetch_and_extract.py <channel_name> <max_videos>
```

**Parameters:**
- `channel_name`: Name of the YouTube channel (required)
- `max_videos`: Maximum number of videos to fetch (required)

**Example:**
```
python fetch_and_extract.py indydevdan 10
```

**Output:**
Generates markdown files in the `output` directory for each video's transcript.

**Note:** This script requires a YouTube Data API key, which should be set in the script.

## Requirements

- Python 3.6+
- youtube-transcript-api>=0.6.1
- google-api-python-client>=2.0.0

## API Key

The `fetch_and_extract.py` script requires a YouTube Data API key. You can obtain one from the [Google Cloud Console](https://console.cloud.google.com/).

Replace the `DEVELOPER_KEY` value in `fetch_and_extract.py` with your actual API key.
