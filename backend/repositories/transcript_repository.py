"""Repository layer for transcript data access"""
import os
import re
from pathlib import Path
from typing import List, Optional, Tuple
from datetime import datetime


class TranscriptRepository:
    """Handles all transcript file operations"""
    
    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        
    def ensure_output_dir(self):
        """Ensure the output directory exists"""
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def save_transcript(self, content: str, channel_name: str, video_date: str, video_id: str) -> str:
        """Save transcript content to file"""
        self.ensure_output_dir()
        filename = f"{channel_name}-{video_date}-{video_id}.md"
        filepath = self.output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return str(filepath)
    
    def list_transcripts(self, page: int = 1, per_page: int = 10) -> Tuple[List[Path], int]:
        """List transcript files with pagination"""
        if not self.output_dir.exists():
            return [], 0
        
        # Get files sorted by modification time (newest first)
        transcript_files = sorted(
            self.output_dir.glob("*.md"), 
            key=lambda x: x.stat().st_mtime, 
            reverse=True
        )
        total = len(transcript_files)
        
        # Pagination
        start_idx = (page - 1) * per_page
        end_idx = start_idx + per_page
        page_files = transcript_files[start_idx:end_idx]
        
        return page_files, total
    
    def get_transcript_by_video_id(self, video_id: str) -> Optional[Path]:
        """Find transcript file by video ID"""
        if not self.output_dir.exists():
            return None
        
        matching_files = list(self.output_dir.glob(f"*-{video_id}.md"))
        return matching_files[0] if matching_files else None
    
    def read_transcript(self, filepath: Path) -> str:
        """Read transcript content from file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    
    def parse_transcript_metadata(self, filepath: Path) -> dict:
        """Parse metadata from transcript filename and content"""
        filename = filepath.stem
        
        # Parse filename
        parts = filename.rsplit('-', 1)
        if len(parts) == 2:
            video_id = parts[1]
            remaining = parts[0]
            
            # Extract date
            date_pattern = r'(\d{4}-\d{2}-\d{2})'
            date_match = re.search(date_pattern, remaining)
            
            if date_match:
                video_date = date_match.group(1)
                date_start = remaining.find(video_date)
                channel_name = remaining[:date_start].rstrip('-')
            else:
                # Fallback parsing
                channel_name = remaining
                video_date = datetime.now().strftime("%Y-%m-%d")
        else:
            # Fallback for unexpected format
            channel_name = "unknown_channel"
            video_date = datetime.now().strftime("%Y-%m-%d")
            video_id = filename
        
        # Read content to extract title
        content = self.read_transcript(filepath)
        video_title = None
        
        lines = content.split('\n')
        for line in lines[:10]:
            if line.startswith('# '):
                video_title = line[2:].strip()
                break
            elif line.startswith('Title: '):
                video_title = line[7:].strip()
                break
        
        return {
            'video_id': video_id,
            'channel_name': channel_name,
            'video_date': video_date,
            'video_title': video_title,
            'content': content,
            'created_at': datetime.fromtimestamp(filepath.stat().st_mtime)
        }