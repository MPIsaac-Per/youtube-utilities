"""
Refactored FastAPI application with proper architectural layers
"""
import os
import sys
from pathlib import Path
from typing import Dict
import uuid
from datetime import datetime
import asyncio

from fastapi import FastAPI, HTTPException, BackgroundTasks, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
import uvicorn

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from config import config
from backend.api_models import (
    ExtractRequest, ChannelFetchRequest, TranscriptResponse, 
    JobResponse, JobStatus, ErrorResponse, TranscriptListResponse,
    ExportFormat
)
from backend.repositories.transcript_repository import TranscriptRepository
from backend.repositories.youtube_repository import YouTubeRepository
from backend.services.transcript_service import TranscriptService

# Initialize app
app = FastAPI(
    title="YouTube Transcript Extractor API",
    description="Extract transcripts from YouTube videos and channels",
    version="2.0.0"
)

# Configure CORS
origins = os.getenv("CORS_ORIGINS", "http://localhost:5173,http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize repositories and services
transcript_repo = TranscriptRepository(config.output_dir)
youtube_repo = YouTubeRepository(config.get_current_api_key())
transcript_service = TranscriptService(transcript_repo, youtube_repo)

# In-memory job storage (should be replaced with Redis in production)
jobs: Dict[str, JobResponse] = {}


async def process_single_video_job(job_id: str, request: ExtractRequest):
    """Background task to process a single video"""
    try:
        jobs[job_id].status = JobStatus.PROCESSING
        
        # Use service layer
        result = transcript_service.extract_single_transcript(
            str(request.youtube_url),
            request.channel_name,
            request.video_date,
            request.export_format
        )
        
        jobs[job_id].status = JobStatus.COMPLETED
        jobs[job_id].result = result
        jobs[job_id].progress = 100
        
    except Exception as e:
        jobs[job_id].status = JobStatus.FAILED
        jobs[job_id].message = str(e)


async def process_channel_videos_job(job_id: str, channel_name: str, max_videos: int):
    """Background task to process multiple videos from a channel"""
    try:
        jobs[job_id].status = JobStatus.PROCESSING
        
        # Process videos with progress updates
        total_processed = 0
        
        # Get channel videos first to know total count
        channel_id = youtube_repo.get_channel_id(channel_name)
        if not channel_id:
            raise ValueError(f"Channel '{channel_name}' not found")
        
        videos = youtube_repo.get_channel_videos(channel_id, max_videos)
        total_videos = len(videos)
        
        if total_videos == 0:
            jobs[job_id].status = JobStatus.COMPLETED
            jobs[job_id].message = "No videos found"
            jobs[job_id].progress = 100
            return
        
        successful = 0
        failed = 0
        failed_videos = []
        
        for i, (video_url, video_date) in enumerate(videos):
            try:
                # Update progress
                progress = int((i / total_videos) * 100)
                jobs[job_id].progress = progress
                jobs[job_id].message = f"Processing video {i+1} of {total_videos}"
                
                # Extract transcript using service
                transcript_service.extract_single_transcript(
                    video_url, channel_name, video_date
                )
                successful += 1
                
            except Exception as e:
                failed += 1
                failed_videos.append(f"{video_url} - {str(e)}")
        
        # Final status
        jobs[job_id].status = JobStatus.COMPLETED
        jobs[job_id].progress = 100
        
        if failed > 0:
            jobs[job_id].message = f"Completed: {successful} transcripts extracted, {failed} failed"
        else:
            jobs[job_id].message = f"Success! All {successful} transcripts extracted"
        
    except Exception as e:
        jobs[job_id].status = JobStatus.FAILED
        jobs[job_id].message = str(e)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "YouTube Transcript Extractor API", 
        "version": "2.0.0",
        "docs": "/docs"
    }


@app.post("/api/extract", response_model=JobResponse)
async def extract_transcript_endpoint(
    request: ExtractRequest,
    background_tasks: BackgroundTasks
):
    """Extract transcript from a single YouTube video"""
    try:
        job_id = str(uuid.uuid4())
        
        # Create job entry
        jobs[job_id] = JobResponse(
            job_id=job_id,
            status=JobStatus.PENDING,
            progress=0
        )
        
        # Start background processing
        background_tasks.add_task(process_single_video_job, job_id, request)
        
        return jobs[job_id]
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/fetch-channel", response_model=JobResponse)
async def fetch_channel_videos(
    request: ChannelFetchRequest,
    background_tasks: BackgroundTasks
):
    """Fetch recent videos from a YouTube channel and extract all transcripts"""
    try:
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
            process_channel_videos_job, 
            job_id, 
            request.channel_name, 
            request.max_videos
        )
        
        return jobs[job_id]
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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
    try:
        result = transcript_service.list_transcripts(page, per_page)
        return TranscriptListResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error listing transcripts: {str(e)}")


@app.get("/api/transcript/{video_id}")
async def download_transcript(
    video_id: str, 
    format: ExportFormat = ExportFormat.MARKDOWN
):
    """Download a specific transcript in the requested format"""
    try:
        content = transcript_service.get_transcript(video_id, format)
        
        if content is None:
            raise HTTPException(status_code=404, detail="Transcript not found")
        
        # Return appropriate response based on format
        if format == ExportFormat.MARKDOWN:
            return FileResponse(
                content=content,
                media_type="text/markdown",
                filename=f"{video_id}.md"
            )
        elif format == ExportFormat.TEXT:
            return JSONResponse(content={"text": content})
        elif format == ExportFormat.SRT:
            return FileResponse(
                content=content,
                media_type="text/plain",
                filename=f"{video_id}.srt"
            )
        elif format == ExportFormat.JSON:
            return JSONResponse(content={"transcript": content})
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error downloading transcript: {str(e)}")


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom HTTP exception handler"""
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(error=exc.detail).dict()
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """General exception handler for unexpected errors"""
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            error="Internal server error",
            detail=str(exc) if os.getenv("DEBUG") else None
        ).dict()
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)