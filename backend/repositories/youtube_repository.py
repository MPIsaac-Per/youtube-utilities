"""Repository layer for YouTube API access"""
from typing import List, Tuple, Optional, Dict
import googleapiclient.discovery
from youtube_transcript_api import YouTubeTranscriptApi


class YouTubeRepository:
    """Handles all YouTube API operations"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self._youtube = None
    
    @property
    def youtube(self):
        """Lazy initialization of YouTube API client"""
        if self._youtube is None:
            self._youtube = googleapiclient.discovery.build(
                "youtube", "v3", developerKey=self.api_key
            )
        return self._youtube
    
    def get_channel_id(self, channel_name: str) -> Optional[str]:
        """Get channel ID from channel name"""
        try:
            request = self.youtube.search().list(
                part="snippet",
                q=channel_name,
                type="channel",
                maxResults=1
            )
            response = request.execute()
            
            for item in response.get("items", []):
                if item["id"].get("channelId"):
                    return item["id"]["channelId"]
            return None
        except Exception as e:
            raise Exception(f"Failed to get channel ID: {str(e)}")
    
    def get_channel_videos(self, channel_id: str, max_videos: int) -> List[Tuple[str, str]]:
        """Get recent videos from a channel"""
        try:
            request = self.youtube.search().list(
                part="snippet",
                channelId=channel_id,
                maxResults=max_videos,
                order="date",
                type="video"
            )
            response = request.execute()
            
            video_data = []
            for item in response.get("items", []):
                if item["id"].get("videoId"):
                    video_id = item["id"]["videoId"]
                    video_url = f"https://www.youtube.com/watch?v={video_id}"
                    video_date = item["snippet"]["publishedAt"][:10]
                    video_data.append((video_url, video_date))
            
            return video_data
        except Exception as e:
            raise Exception(f"Failed to get channel videos: {str(e)}")
    
    def get_video_metadata(self, video_id: str) -> Dict[str, Optional[str]]:
        """Get video metadata from YouTube"""
        try:
            request = self.youtube.videos().list(
                part="snippet",
                id=video_id
            )
            response = request.execute()
            
            if response.get("items"):
                snippet = response["items"][0]["snippet"]
                return {
                    'title': snippet.get("title"),
                    'channel_name': snippet.get("channelTitle"),
                    'published_date': snippet.get("publishedAt", "")[:10],
                    'description': snippet.get("description")
                }
            
            return {
                'title': None,
                'channel_name': None,
                'published_date': None,
                'description': None
            }
        except Exception as e:
            raise Exception(f"Failed to get video metadata: {str(e)}")
    
    def get_transcript(self, video_id: str) -> List[Dict]:
        """Get transcript for a video"""
        try:
            return YouTubeTranscriptApi.get_transcript(video_id)
        except Exception as e:
            raise Exception(f"Failed to get transcript: {str(e)}")