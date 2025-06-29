from pydantic import BaseModel, HttpUrl, Field, validator
from typing import Optional, List
from datetime import datetime
from enum import Enum


class ExportFormat(str, Enum):
    MARKDOWN = "md"
    TEXT = "txt"
    SRT = "srt"
    JSON = "json"


class ExtractRequest(BaseModel):
    youtube_url: HttpUrl
    channel_name: Optional[str] = None
    video_date: Optional[str] = None
    export_format: ExportFormat = ExportFormat.MARKDOWN

    @validator('youtube_url')
    def validate_youtube_url(cls, v):
        url_str = str(v)
        if 'youtube.com/watch?v=' not in url_str and 'youtu.be/' not in url_str:
            raise ValueError('Invalid YouTube URL format')
        return v


class ChannelFetchRequest(BaseModel):
    channel_name: str
    max_videos: int = Field(default=10, ge=1, le=50)


class TranscriptResponse(BaseModel):
    video_id: str
    video_url: str
    video_title: Optional[str] = None
    channel_name: str
    video_date: str
    transcript_text: str
    duration_seconds: Optional[float] = None
    format: ExportFormat
    created_at: datetime = Field(default_factory=datetime.now)


class JobStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class JobResponse(BaseModel):
    job_id: str
    status: JobStatus
    message: Optional[str] = None
    result: Optional[TranscriptResponse] = None
    progress: Optional[int] = Field(None, ge=0, le=100)


class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None


class TranscriptListResponse(BaseModel):
    transcripts: List[TranscriptResponse]
    total: int
    page: int
    per_page: int