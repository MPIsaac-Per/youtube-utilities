import React, { useState, useEffect } from 'react';
import { Toaster, toast } from 'react-hot-toast';
import Header from './components/Header';
import URLInput from './components/URLInput';
import ChannelInput from './components/ChannelInput';
import TranscriptList from './components/TranscriptList';
import TranscriptViewer from './components/TranscriptViewer';
import { transcriptAPI } from './services/api';
import { RefreshCw, List, Video, Users } from 'lucide-react';

function App() {
  const [darkMode, setDarkMode] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [transcripts, setTranscripts] = useState([]);
  const [selectedTranscript, setSelectedTranscript] = useState(null);
  const [showHistory, setShowHistory] = useState(false);
  const [activeTab, setActiveTab] = useState('single'); // 'single' or 'channel'

  useEffect(() => {
    // Check for saved dark mode preference
    const savedDarkMode = localStorage.getItem('darkMode');
    if (savedDarkMode) {
      setDarkMode(JSON.parse(savedDarkMode));
    }
  }, []);

  useEffect(() => {
    // Apply dark mode class to document
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    localStorage.setItem('darkMode', JSON.stringify(darkMode));
  }, [darkMode]);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  const handleExtract = async (url, channelName, videoDate, format) => {
    setIsLoading(true);
    
    try {
      // Start extraction job
      const job = await transcriptAPI.extractTranscript(url, channelName, videoDate, format);
      
      toast.loading('Extracting transcript...', { id: job.job_id });

      // Poll for completion
      const result = await transcriptAPI.pollJobStatus(job.job_id, (status) => {
        if (status.progress) {
          toast.loading(`Extracting transcript... ${status.progress}%`, { id: job.job_id });
        }
      });

      if (result.status === 'completed') {
        toast.success('Transcript extracted successfully!', { id: job.job_id });
        setSelectedTranscript(result.result);
        // Refresh transcript list
        loadTranscripts();
      } else {
        toast.error(result.message || 'Failed to extract transcript', { id: job.job_id });
      }
    } catch (error) {
      toast.error(error.message || 'An error occurred');
    } finally {
      setIsLoading(false);
    }
  };

  const handleChannelExtract = async (channelName, maxVideos) => {
    setIsLoading(true);
    
    try {
      // Start channel extraction job
      const job = await transcriptAPI.fetchChannelVideos(channelName, maxVideos);
      
      toast.loading(`Fetching videos from ${channelName}...`, { id: job.job_id });

      // Poll for completion
      const result = await transcriptAPI.pollJobStatus(job.job_id, (status) => {
        if (status.message) {
          toast.loading(status.message, { id: job.job_id });
        }
      });

      if (result.status === 'completed') {
        toast.success(result.message || 'Channel transcripts extracted!', { id: job.job_id });
        // Refresh transcript list
        loadTranscripts();
        setShowHistory(true);
      } else {
        toast.error(result.message || 'Failed to extract channel transcripts', { id: job.job_id });
      }
    } catch (error) {
      toast.error(error.message || 'An error occurred');
    } finally {
      setIsLoading(false);
    }
  };

  const loadTranscripts = async () => {
    try {
      const data = await transcriptAPI.listTranscripts(1, 20);
      setTranscripts(data.transcripts);
    } catch (error) {
      console.error('Failed to load transcripts:', error);
    }
  };

  useEffect(() => {
    loadTranscripts();
  }, []);

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 transition-colors">
      <Toaster position="top-right" />
      
      <Header darkMode={darkMode} toggleDarkMode={toggleDarkMode} />
      
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="text-center mb-8">
          <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-4">
            Extract YouTube Transcripts
          </h2>
          <p className="text-lg text-gray-600 dark:text-gray-400">
            Enter a YouTube URL to extract and download transcripts in multiple formats
          </p>
        </div>

        <div className="flex justify-center mb-8">
          <div className="w-full max-w-2xl">
            {/* Tab Navigation */}
            <div className="flex border-b border-gray-200 dark:border-gray-700 mb-6">
              <button
                onClick={() => setActiveTab('single')}
                className={`flex items-center gap-2 px-4 py-2 text-sm font-medium border-b-2 transition-colors ${
                  activeTab === 'single'
                    ? 'border-youtube-red text-youtube-red'
                    : 'border-transparent text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300'
                }`}
              >
                <Video className="w-4 h-4" />
                Single Video
              </button>
              <button
                onClick={() => setActiveTab('channel')}
                className={`flex items-center gap-2 px-4 py-2 text-sm font-medium border-b-2 transition-colors ${
                  activeTab === 'channel'
                    ? 'border-youtube-red text-youtube-red'
                    : 'border-transparent text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300'
                }`}
              >
                <Users className="w-4 h-4" />
                Entire Channel
              </button>
            </div>

            {/* Tab Content */}
            {activeTab === 'single' ? (
              <URLInput onExtract={handleExtract} isLoading={isLoading} />
            ) : (
              <ChannelInput onExtract={handleChannelExtract} isLoading={isLoading} />
            )}
          </div>
        </div>

        <div className="flex justify-between items-center mb-6">
          <h3 className="text-xl font-semibold text-gray-900 dark:text-white">
            Recent Transcripts
          </h3>
          <div className="flex gap-2">
            <button
              onClick={loadTranscripts}
              className="flex items-center gap-2 px-4 py-2 text-gray-700 dark:text-gray-300 
                       hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-colors"
            >
              <RefreshCw className="w-4 h-4" />
              Refresh
            </button>
            <button
              onClick={() => setShowHistory(!showHistory)}
              className="flex items-center gap-2 px-4 py-2 text-gray-700 dark:text-gray-300 
                       hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-colors"
            >
              <List className="w-4 h-4" />
              {showHistory ? 'Hide' : 'Show'} History
            </button>
          </div>
        </div>

        {showHistory && (
          <TranscriptList 
            transcripts={transcripts} 
            onSelect={setSelectedTranscript} 
          />
        )}

        {selectedTranscript && (
          <TranscriptViewer
            transcript={selectedTranscript}
            onClose={() => setSelectedTranscript(null)}
          />
        )}
      </main>

      <footer className="mt-auto py-6 text-center text-sm text-gray-500 dark:text-gray-400">
        <p>&copy; 2024 YouTube Transcript Extractor. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;