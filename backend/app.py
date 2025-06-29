import os
import sys
import re
from pathlib import Path
from typing import Dict, Optional
import uuid
from datetime import datetime
import asyncio

from fastapi import FastAPI, HTTPException, BackgroundTasks, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
import uvicorn

# Add parent directory to path to import existing modules
sys.path.append(str(Path(__file__).parent.parent))

from config import config
from extract_transcript import extract_transcript
from fetch_and_extract import get_channel_id_from_name, get_video_urls_and_dates_from_channel
from backend.api_models import (
    ExtractRequest, ChannelFetchRequest, TranscriptResponse, 
    JobResponse, JobStatus, ErrorResponse, TranscriptListResponse,
    ExportFormat
)

app = FastAPI(
    title="YouTube Transcript Extractor API",
    description="Extract transcripts from YouTube videos and channels",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Vite default ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory job storage (replace with Redis in production)
jobs: Dict[str, JobResponse] = {}


def format_transcript(transcript_data: list, format_type: ExportFormat) -> str:
    """Convert transcript data to requested format"""
    if format_type == ExportFormat.MARKDOWN:
        return "\n".join([f"{entry['start']:.2f}s: {entry['text']}" for entry in transcript_data])
    elif format_type == ExportFormat.TEXT:
        return " ".join([entry['text'] for entry in transcript_data])
    elif format_type == ExportFormat.SRT:
        srt_content = []
        for i, entry in enumerate(transcript_data, 1):
            start_time = entry['start']
            end_time = entry.get('duration', 0) + start_time
            srt_content.append(f"{i}")
            srt_content.append(f"{format_srt_time(start_time)} --> {format_srt_time(end_time)}")
            srt_content.append(entry['text'])
            srt_content.append("")
        return "\n".join(srt_content)
    elif format_type == ExportFormat.JSON:
        import json
        return json.dumps(transcript_data, indent=2)
    return ""


def format_srt_time(seconds: float) -> str:
    """Format seconds to SRT timestamp"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:06.3f}".replace('.', ',')


async def process_single_video(job_id: str, request: ExtractRequest):
    """Background task to process a single video"""
    try:
        jobs[job_id].status = JobStatus.PROCESSING
        
        # Extract video ID from URL
        url_str = str(request.youtube_url)
        video_id = url_str.split('v=')[-1].split('&')[0]
        
        # Import here to access the functions
        from youtube_transcript_api import YouTubeTranscriptApi
        import googleapiclient.discovery
        
        # Get video metadata
        video_title = None
        channel_name = request.channel_name
        video_date = request.video_date
        
        try:
            youtube = googleapiclient.discovery.build(
                "youtube", "v3", developerKey=config.get_current_api_key()
            )
            
            video_request = youtube.videos().list(
                part="snippet",
                id=video_id
            )
            video_response = video_request.execute()
            
            if video_response.get("items"):
                snippet = video_response["items"][0]["snippet"]
                video_title = snippet["title"]
                channel_name = channel_name or snippet["channelTitle"]
                video_date = video_date or snippet["publishedAt"][:10]
        except Exception as e:
            print(f"Could not fetch video metadata: {e}")
        
        # Get transcript
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Format transcript
        formatted_transcript = format_transcript(transcript_data, request.export_format)
        
        # Calculate duration
        duration = sum(entry.get('duration', 0) for entry in transcript_data)
        
        # Create response
        result = TranscriptResponse(
            video_id=video_id,
            video_url=url_str,
            video_title=video_title,
            channel_name=channel_name or config.default_channel_name,
            video_date=video_date or datetime.now().strftime("%Y-%m-%d"),
            transcript_text=formatted_transcript,
            duration_seconds=duration,
            format=request.export_format
        )
        
        jobs[job_id].status = JobStatus.COMPLETED
        jobs[job_id].result = result
        jobs[job_id].progress = 100
        
    except Exception as e:
        jobs[job_id].status = JobStatus.FAILED
        jobs[job_id].message = str(e)


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "YouTube Transcript Extractor API", "version": "1.0.0"}


@app.post("/api/extract", response_model=JobResponse)
async def extract_transcript_endpoint(
    request: ExtractRequest,
    background_tasks: BackgroundTasks
):
    """Extract transcript from a single YouTube video"""
    job_id = str(uuid.uuid4())
    
    # Create job entry
    jobs[job_id] = JobResponse(
        job_id=job_id,
        status=JobStatus.PENDING,
        progress=0
    )
    
    # Start background processing
    background_tasks.add_task(process_single_video, job_id, request)
    
    return jobs[job_id]


async def process_channel_videos(job_id: str, channel_name: str, max_videos: int):
    """Background task to process multiple videos from a channel"""
    try:
        jobs[job_id].status = JobStatus.PROCESSING
        
        # Get channel ID
        channel_id = get_channel_id_from_name(channel_name)
        if not channel_id:
            jobs[job_id].status = JobStatus.FAILED
            jobs[job_id].message = f"Channel '{channel_name}' not found"
            return
        
        # Get videos
        videos = get_video_urls_and_dates_from_channel(channel_id, max_videos)
        total_videos = len(videos)
        
        if total_videos == 0:
            jobs[job_id].status = JobStatus.COMPLETED
            jobs[job_id].message = "No videos found"
            jobs[job_id].progress = 100
            return
        
        # Process each video
        successful = 0
        failed = 0
        failed_videos = []
        
        for i, (video_url, video_date) in enumerate(videos):
            try:
                # Update progress
                progress = int((i / total_videos) * 100)
                jobs[job_id].progress = progress
                jobs[job_id].message = f"Processing video {i+1} of {total_videos}"
                
                # Extract transcript
                video_id = video_url.split('v=')[-1]
                extract_transcript(video_url, config.output_dir, channel_name, video_date)
                successful += 1
                
            except Exception as e:
                failed += 1
                failed_videos.append(f"{video_url} - {str(e)}")
                print(f"Failed to extract transcript for {video_url}: {e}")
        
        # Final status
        jobs[job_id].status = JobStatus.COMPLETED
        jobs[job_id].progress = 100
        
        if failed > 0:
            jobs[job_id].message = f"Completed: {successful} transcripts extracted, {failed} failed. Failed videos: {'; '.join(failed_videos[:3])}"
        else:
            jobs[job_id].message = f"Success! All {successful} transcripts extracted"
        
    except Exception as e:
        jobs[job_id].status = JobStatus.FAILED
        jobs[job_id].message = str(e)


@app.post("/api/fetch-channel", response_model=JobResponse)
async def fetch_channel_videos(
    request: ChannelFetchRequest,
    background_tasks: BackgroundTasks
):
    """Fetch recent videos from a YouTube channel and extract all transcripts"""
    job_id = str(uuid.uuid4())
    
    # Create job entry
    jobs[job_id] = JobResponse(
        job_id=job_id,
        status=JobStatus.PENDING,
        message=f"Starting to fetch videos from '{request.channel_name}'",
        progress=0
    )
    
    # Start background processing
    background_tasks.add_task(
        process_channel_videos, 
        job_id, 
        request.channel_name, 
        request.max_videos
    )
    
    return jobs[job_id]


@app.get("/api/status/{job_id}", response_model=JobResponse)
async def get_job_status(job_id: str):
    """Get the status of a transcript extraction job"""
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    
    return jobs[job_id]


@app.get("/api/transcripts", response_model=TranscriptListResponse)
async def list_transcripts(
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100)
):
    """List all saved transcripts"""
    # Get all markdown files from output directory
    output_path = Path(config.output_dir)
    if not output_path.exists():
        return TranscriptListResponse(transcripts=[], total=0, page=page, per_page=per_page)
    
    # Get files sorted by modification time (newest first)
    transcript_files = sorted(
        output_path.glob("*.md"), 
        key=lambda x: x.stat().st_mtime, 
        reverse=True
    )
    total = len(transcript_files)
    
    # Pagination
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    page_files = transcript_files[start_idx:end_idx]
    
    transcripts = []
    for file_path in page_files:
        # Parse filename to extract metadata
        filename = file_path.stem
        
        # Handle different filename formats
        # Format 1: @ChannelName-YYYY-MM-DD-videoId
        # Format 2: channel_name-YYYY-MM-DD-videoId
        
        # Find the last occurrence of a dash followed by what looks like a video ID
        parts = filename.rsplit('-', 1)
        if len(parts) == 2:
            video_id = parts[1]
            remaining = parts[0]
            
            # Try to extract date (YYYY-MM-DD format)
            date_pattern = r'(\d{4}-\d{2}-\d{2})'
            import re
            date_match = re.search(date_pattern, remaining)
            
            if date_match:
                video_date = date_match.group(1)
                # Extract channel name (everything before the date)
                date_start = remaining.find(video_date)
                channel_name = remaining[:date_start].rstrip('-')
            else:
                # Fallback parsing
                parts = remaining.rsplit('-', 2)
                if len(parts) >= 3:
                    channel_name = parts[0]
                    video_date = f"{parts[1]}-{parts[2]}-01"  # Assume first day if partial
                else:
                    channel_name = remaining
                    video_date = datetime.now().strftime("%Y-%m-%d")
        else:
            # Fallback for unexpected format
            channel_name = "unknown_channel"
            video_date = datetime.now().strftime("%Y-%m-%d")
            video_id = filename
        
        # Read transcript content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try to extract title from markdown content
        video_title = None
        lines = content.split('\n')
        for line in lines[:10]:  # Check first 10 lines
            if line.startswith('# '):
                video_title = line[2:].strip()
                break
            elif line.startswith('Title: '):
                video_title = line[7:].strip()
                break
        
        transcripts.append(TranscriptResponse(
            video_id=video_id,
            video_url=f"https://youtube.com/watch?v={video_id}",
            video_title=video_title,
            channel_name=channel_name,
            video_date=video_date,
            transcript_text=content,
            format=ExportFormat.MARKDOWN,
            created_at=datetime.fromtimestamp(file_path.stat().st_mtime)
        ))
    
    return TranscriptListResponse(
        transcripts=transcripts,
        total=total,
        page=page,
        per_page=per_page
    )


@app.get("/api/transcript/{video_id}")
async def download_transcript(video_id: str, format: ExportFormat = ExportFormat.MARKDOWN):
    """Download a specific transcript in the requested format"""
    # Find the transcript file
    output_path = Path(config.output_dir)
    matching_files = list(output_path.glob(f"*-{video_id}.md"))
    
    if not matching_files:
        raise HTTPException(status_code=404, detail="Transcript not found")
    
    file_path = matching_files[0]
    
    # For markdown, return as-is
    if format == ExportFormat.MARKDOWN:
        return FileResponse(
            path=file_path,
            media_type="text/markdown",
            filename=f"{video_id}.md"
        )
    
    # For other formats, convert on the fly
    # This is a simplified version - in production, you'd re-fetch and convert
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if format == ExportFormat.TEXT:
        # Simple conversion - remove timestamps
        text_content = '\n'.join([line.split(': ', 1)[1] if ': ' in line else line 
                                 for line in content.split('\n') if line.strip()])
        return JSONResponse(content={"text": text_content})
    
    return JSONResponse(content={"text": content})


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom HTTP exception handler"""
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(error=exc.detail).dict()
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)