import axios from 'axios';

const API_BASE_URL = '/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response) {
      // Server responded with error
      throw new Error(error.response.data.error || 'An error occurred');
    } else if (error.request) {
      // Request made but no response
      throw new Error('No response from server');
    } else {
      // Something else happened
      throw new Error('Request failed');
    }
  }
);

export const transcriptAPI = {
  // Extract transcript from a single video
  extractTranscript: async (youtubeUrl, channelName = null, videoDate = null, exportFormat = 'md') => {
    const response = await api.post('/extract', {
      youtube_url: youtubeUrl,
      channel_name: channelName,
      video_date: videoDate,
      export_format: exportFormat,
    });
    return response.data;
  },

  // Fetch videos from a channel
  fetchChannelVideos: async (channelName, maxVideos = 10) => {
    const response = await api.post('/fetch-channel', {
      channel_name: channelName,
      max_videos: maxVideos,
    });
    return response.data;
  },

  // Get job status
  getJobStatus: async (jobId) => {
    const response = await api.get(`/status/${jobId}`);
    return response.data;
  },

  // List all transcripts
  listTranscripts: async (page = 1, perPage = 10) => {
    const response = await api.get('/transcripts', {
      params: { page, per_page: perPage },
    });
    return response.data;
  },

  // Download transcript
  downloadTranscript: async (videoId, format = 'md') => {
    const response = await api.get(`/transcript/${videoId}`, {
      params: { format },
      responseType: format === 'md' ? 'blob' : 'json',
    });
    return response.data;
  },

  // Poll job status until completion
  pollJobStatus: async (jobId, onProgress = null) => {
    const maxAttempts = 60; // 60 seconds timeout
    let attempts = 0;

    while (attempts < maxAttempts) {
      const status = await transcriptAPI.getJobStatus(jobId);
      
      if (onProgress) {
        onProgress(status);
      }

      if (status.status === 'completed' || status.status === 'failed') {
        return status;
      }

      // Wait 1 second before next poll
      await new Promise(resolve => setTimeout(resolve, 1000));
      attempts++;
    }

    throw new Error('Job timeout - please try again');
  },
};

export default api;