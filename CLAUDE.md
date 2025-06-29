# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

YouTube Utilities is a Python-based tool for extracting and managing YouTube video transcripts. It provides both command-line utilities and a web interface (frontend only) for transcript extraction.

## Commands

### Setup
```bash
# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env file and add your YouTube API key
```

### Usage
```bash
# Extract transcript from a single video
python extract_transcript.py <youtube_url> [channel_name] [video_date]

# Fetch and extract transcripts from recent videos
python fetch_and_extract.py <channel_name> <max_videos>
```

## Architecture

### Core Components

1. **Transcript Extraction** (`extract_transcript.py`):
   - Accepts YouTube URL, optional channel name, and video date
   - Uses `youtube-transcript-api` to fetch transcripts
   - Saves output as Markdown files in `output/` directory
   - Naming convention: `{channel_name}-{video_date}-{video_id}.md`

2. **Bulk Fetching** (`fetch_and_extract.py`):
   - Fetches recent videos from a YouTube channel
   - Uses YouTube Data API v3 to get video listings
   - Calls `extract_transcript.py` for each video
   - Uses API key from environment configuration

3. **Web Interface** (incomplete):
   - `index.html`, `styles.css`, `script.js` provide frontend
   - No backend implementation currently exists
   - Would need API endpoint to connect frontend to Python scripts

### Key Implementation Details

- **API Integration**: Uses Google's YouTube Data API v3 and youtube-transcript-api
- **Output Format**: Transcripts saved as Markdown with video metadata
- **Cross-Platform**: Now uses platform-agnostic Python executable detection
- **Dependencies**: `youtube-transcript-api`, `google-api-python-client`, and `python-dotenv`
- **Configuration**: Centralized in `config.py` module with environment variable support

### Configuration Options

4. **Environment Configuration** (`config.py`):
   - Loads settings from `.env` file or environment variables
   - Supports single API key or multiple keys for rotation
   - Configurable output directory and default values
   - See `.env.example` for all available options

## Development Notes

- Always activate the virtual environment before running scripts
- Copy `.env.example` to `.env` and add your YouTube API key before running
- Web interface backend needs implementation if web functionality is desired
- Output files are saved in the `output/` directory (gitignored)
- API key rotation is supported by setting `YOUTUBE_API_KEYS` with comma-separated values