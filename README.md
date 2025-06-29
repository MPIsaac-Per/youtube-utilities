# YouTube Transcript Extractor

A modern web application for extracting and managing YouTube video transcripts with both CLI and web interfaces.

## Features

- 🎥 Extract transcripts from YouTube videos
- 📺 Bulk fetch transcripts from channels
- 📄 Multiple export formats (Markdown, Text, SRT, JSON)
- 🌐 Modern React web interface with dark mode
- 🚀 FastAPI backend with async processing
- 🐳 Docker support for easy deployment
- 🔑 Environment-based configuration
- 🔄 API key rotation support

## Architecture

- **Backend**: FastAPI with Python 3.11+
- **Frontend**: React with Vite and Tailwind CSS
- **CLI Tools**: Original Python scripts preserved

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- YouTube Data API key ([Get one here](https://console.cloud.google.com/))

### Environment Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/youtube-utilities.git
   cd youtube-utilities
   ```

2. Configure environment:
   ```bash
   cp .env.example .env
   # Edit .env and add your YouTube API key
   ```

### Option 1: Docker (Recommended)

```bash
docker-compose up
```

Access the application at:
- Frontend: http://localhost:5173
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Option 2: Manual Setup

#### Backend Setup
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r backend/requirements.txt

# Run the API server
cd backend
uvicorn app:app --reload
```

#### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## Usage

### Web Interface
1. Open http://localhost:5173 in your browser
2. Enter a YouTube URL
3. Select export format (Markdown, Text, SRT, JSON)
4. Click "Extract Transcript"
5. View, copy, or download transcripts

### CLI Tools

#### Extract Single Video
```bash
python extract_transcript.py <youtube_url> [channel_name] [video_date]

# Example
python extract_transcript.py https://www.youtube.com/watch?v=dQw4w9WgXcQ "Rick Astley" "2009-10-25"
```

#### Fetch Channel Videos
```bash
python fetch_and_extract.py <channel_name> <max_videos>

# Example
python fetch_and_extract.py "TED" 10
```

### API Endpoints

- `POST /api/extract` - Extract transcript from a video
- `POST /api/fetch-channel` - Fetch videos from a channel
- `GET /api/transcripts` - List saved transcripts
- `GET /api/transcript/{video_id}` - Download specific transcript
- `GET /api/status/{job_id}` - Check job status

Full API documentation with interactive examples: http://localhost:8000/docs

## Configuration Options

Edit `.env` file for customization:

```env
# YouTube API Configuration
YOUTUBE_API_KEY=your_api_key_here
YOUTUBE_API_KEYS=key1,key2,key3  # For rotation

# Output Configuration
OUTPUT_DIR=output
DEFAULT_CHANNEL_NAME=unknown_channel

# API Settings
MAX_RESULTS_PER_PAGE=50
API_TIMEOUT=30
```

## Output Format

Transcripts are saved in the `output/` directory:
- Filename: `{channel_name}-{video_date}-{video_id}.{format}`
- Formats: `.md`, `.txt`, `.srt`, `.json`

## Development

### Project Structure
```
youtube-utilities/
├── backend/
│   ├── app.py              # FastAPI application
│   ├── api_models.py       # Pydantic models
│   └── requirements.txt    # Backend dependencies
├── frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── services/       # API integration
│   │   └── App.jsx        # Main application
│   └── package.json
├── extract_transcript.py   # CLI tool
├── fetch_and_extract.py   # CLI tool
├── config.py              # Configuration module
├── docker-compose.yml
└── README.md
```

### Running Tests
```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## Troubleshooting

### Common Issues

1. **"YouTube API key not found"**
   - Ensure `.env` file exists with valid `YOUTUBE_API_KEY`

2. **"No transcript available"**
   - Video may not have captions enabled
   - Try a different video or channel

3. **API Rate Limits**
   - Use multiple API keys with `YOUTUBE_API_KEYS`
   - Keys will rotate automatically

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- UI powered by [React](https://react.dev/) and [Tailwind CSS](https://tailwindcss.com/)
- Transcript extraction via [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/)