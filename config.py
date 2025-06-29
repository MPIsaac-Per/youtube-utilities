import os
from dotenv import load_dotenv
from typing import List, Optional

# Load environment variables from .env file
load_dotenv()


class Config:
    """Centralized configuration management for YouTube Utilities"""
    
    def __init__(self):
        # YouTube API Configuration
        self.youtube_api_key = self._get_api_key()
        self.youtube_api_keys = self._get_api_keys()
        
        # Output Configuration
        self.output_dir = os.getenv('OUTPUT_DIR', 'output')
        self.default_channel_name = os.getenv('DEFAULT_CHANNEL_NAME', 'unknown_channel')
        
        # API Settings
        self.max_results_per_page = int(os.getenv('MAX_RESULTS_PER_PAGE', '50'))
        self.api_timeout = int(os.getenv('API_TIMEOUT', '30'))
        
        # API key rotation
        self._current_key_index = 0
    
    def _get_api_key(self) -> str:
        """Get single YouTube API key from environment"""
        api_key = os.getenv('YOUTUBE_API_KEY')
        if not api_key:
            raise ValueError(
                "YouTube API key not found. Please set YOUTUBE_API_KEY in your .env file "
                "or as an environment variable. See .env.example for reference."
            )
        return api_key
    
    def _get_api_keys(self) -> List[str]:
        """Get multiple YouTube API keys for rotation if available"""
        # First check for multiple keys
        api_keys_str = os.getenv('YOUTUBE_API_KEYS')
        if api_keys_str:
            return [key.strip() for key in api_keys_str.split(',') if key.strip()]
        
        # Fall back to single key
        return [self.youtube_api_key]
    
    def get_current_api_key(self) -> str:
        """Get the current API key (supports rotation)"""
        if not self.youtube_api_keys:
            return self.youtube_api_key
        
        return self.youtube_api_keys[self._current_key_index]
    
    def rotate_api_key(self) -> str:
        """Rotate to the next API key (for rate limit management)"""
        if len(self.youtube_api_keys) > 1:
            self._current_key_index = (self._current_key_index + 1) % len(self.youtube_api_keys)
        return self.get_current_api_key()
    
    def ensure_output_dir(self) -> None:
        """Ensure the output directory exists"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)


# Global config instance
config = Config()