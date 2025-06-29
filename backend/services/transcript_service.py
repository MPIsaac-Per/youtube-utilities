"""Service layer for transcript business logic"""
from typing import List, Optional, Dict
from datetime import datetime
import json

from backend.repositories.transcript_repository import TranscriptRepository
from backend.repositories.youtube_repository import YouTubeRepository
from backend.api_models import ExportFormat, TranscriptResponse


class TranscriptService:
    """Handles transcript business logic"""
    
    def __init__(self, transcript_repo: TranscriptRepository, youtube_repo: YouTubeRepository):
        self.transcript_repo = transcript_repo
        self.youtube_repo = youtube_repo
    
    def extract_single_transcript(
        self, 
        youtube_url: str, 
        channel_name: Optional[str] = None,
        video_date: Optional[str] = None,
        export_format: ExportFormat = ExportFormat.MARKDOWN
    ) -> TranscriptResponse:
        """Extract transcript from a single video"""
        # Extract video ID
        video_id = youtube_url.split('v=')[-1].split('&')[0]
        
        # Get video metadata
        metadata = self.youtube_repo.get_video_metadata(video_id)
        video_title = metadata['title']
        channel_name = channel_name or metadata['channel_name'] or "unknown_channel"
        video_date = video_date or metadata['published_date'] or datetime.now().strftime("%Y-%m-%d")
        
        # Get transcript
        transcript_data = self.youtube_repo.get_transcript(video_id)
        
        # Format transcript
        formatted_transcript = self._format_transcript(transcript_data, export_format)
        
        # Create markdown content with metadata
        if export_format == ExportFormat.MARKDOWN:
            content = self._create_markdown_content(
                video_title, youtube_url, channel_name, video_date, formatted_transcript
            )
        else:
            content = formatted_transcript
        
        # Save to file
        self.transcript_repo.save_transcript(content, channel_name, video_date, video_id)
        
        # Calculate duration
        duration = sum(entry.get('duration', 0) for entry in transcript_data)
        
        return TranscriptResponse(
            video_id=video_id,
            video_url=youtube_url,
            video_title=video_title,
            channel_name=channel_name,
            video_date=video_date,
            transcript_text=formatted_transcript,
            duration_seconds=duration,
            format=export_format
        )
    
    def extract_channel_transcripts(
        self, 
        channel_name: str, 
        max_videos: int
    ) -> Dict[str, any]:
        """Extract transcripts from multiple videos in a channel"""
        # Get channel ID
        channel_id = self.youtube_repo.get_channel_id(channel_name)
        if not channel_id:
            raise ValueError(f"Channel '{channel_name}' not found")
        
        # Get videos
        videos = self.youtube_repo.get_channel_videos(channel_id, max_videos)
        
        results = {
            'successful': 0,
            'failed': 0,
            'failed_videos': [],
            'transcripts': []
        }
        
        for video_url, video_date in videos:
            try:
                transcript = self.extract_single_transcript(
                    video_url, channel_name, video_date
                )
                results['successful'] += 1
                results['transcripts'].append(transcript)
            except Exception as e:
                results['failed'] += 1
                results['failed_videos'].append({
                    'url': video_url,
                    'error': str(e)
                })
        
        return results
    
    def list_transcripts(self, page: int = 1, per_page: int = 10) -> Dict:
        """List saved transcripts with pagination"""
        files, total = self.transcript_repo.list_transcripts(page, per_page)
        
        transcripts = []
        for file_path in files:
            try:
                metadata = self.transcript_repo.parse_transcript_metadata(file_path)
                transcripts.append(TranscriptResponse(
                    video_id=metadata['video_id'],
                    video_url=f"https://youtube.com/watch?v={metadata['video_id']}",
                    video_title=metadata['video_title'],
                    channel_name=metadata['channel_name'],
                    video_date=metadata['video_date'],
                    transcript_text=metadata['content'],
                    format=ExportFormat.MARKDOWN,
                    created_at=metadata['created_at']
                ))
            except Exception as e:
                print(f"Error parsing transcript {file_path}: {e}")
                continue
        
        return {
            'transcripts': transcripts,
            'total': total,
            'page': page,
            'per_page': per_page
        }
    
    def get_transcript(self, video_id: str, export_format: ExportFormat) -> Optional[str]:
        """Get a specific transcript in the requested format"""
        file_path = self.transcript_repo.get_transcript_by_video_id(video_id)
        if not file_path:
            return None
        
        content = self.transcript_repo.read_transcript(file_path)
        
        if export_format == ExportFormat.MARKDOWN:
            return content
        
        # Convert from markdown to other formats
        # Extract just the transcript lines
        lines = content.split('\n')
        transcript_lines = []
        in_transcript = False
        
        for line in lines:
            if line.strip() == '---':
                in_transcript = True
                continue
            if in_transcript and line.strip():
                transcript_lines.append(line)
        
        if export_format == ExportFormat.TEXT:
            # Remove timestamps
            text_lines = []
            for line in transcript_lines:
                if ': ' in line:
                    text_lines.append(line.split(': ', 1)[1])
            return ' '.join(text_lines)
        
        return content
    
    def _format_transcript(self, transcript_data: List[Dict], format_type: ExportFormat) -> str:
        """Format transcript data based on export format"""
        if format_type == ExportFormat.MARKDOWN:
            return "\n".join([f"{entry['start']:.2f}s: {entry['text']}" for entry in transcript_data])
        elif format_type == ExportFormat.TEXT:
            return " ".join([entry['text'] for entry in transcript_data])
        elif format_type == ExportFormat.SRT:
            return self._format_srt(transcript_data)
        elif format_type == ExportFormat.JSON:
            return json.dumps(transcript_data, indent=2)
        return ""
    
    def _format_srt(self, transcript_data: List[Dict]) -> str:
        """Format transcript as SRT"""
        srt_content = []
        for i, entry in enumerate(transcript_data, 1):
            start_time = entry['start']
            end_time = entry.get('duration', 0) + start_time
            srt_content.append(f"{i}")
            srt_content.append(f"{self._format_srt_time(start_time)} --> {self._format_srt_time(end_time)}")
            srt_content.append(entry['text'])
            srt_content.append("")
        return "\n".join(srt_content)
    
    def _format_srt_time(self, seconds: float) -> str:
        """Format seconds to SRT timestamp"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{secs:06.3f}".replace('.', ',')
    
    def _create_markdown_content(
        self, 
        title: Optional[str], 
        url: str, 
        channel_name: str, 
        video_date: str, 
        transcript: str
    ) -> str:
        """Create markdown content with metadata"""
        content = []
        
        if title:
            content.append(f"# {title}\n")
        
        content.append(f"URL: {url}")
        if title:
            content.append(f"Title: {title}")
        content.append(f"Channel: {channel_name}")
        content.append(f"Date: {video_date}")
        content.append("\n---\n")
        content.append(transcript)
        
        return "\n".join(content)