import React, { useState } from 'react';
import { Link, Loader2, Download } from 'lucide-react';
import toast from 'react-hot-toast';

const URLInput = ({ onExtract, isLoading }) => {
  const [url, setUrl] = useState('');
  const [channelName, setChannelName] = useState('');
  const [format, setFormat] = useState('md');

  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (!url.trim()) {
      toast.error('Please enter a YouTube URL');
      return;
    }

    // Basic YouTube URL validation
    const youtubeRegex = /^(https?:\/\/)?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/)/;
    if (!youtubeRegex.test(url)) {
      toast.error('Please enter a valid YouTube URL');
      return;
    }

    onExtract(url, channelName || null, null, format);
  };

  return (
    <form onSubmit={handleSubmit} className="w-full max-w-2xl space-y-4">
      <div>
        <label htmlFor="url" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
          YouTube URL
        </label>
        <div className="relative">
          <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <Link className="h-5 w-5 text-gray-400" />
          </div>
          <input
            type="url"
            id="url"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="https://www.youtube.com/watch?v=..."
            className="block w-full pl-10 pr-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md 
                     focus:ring-youtube-red focus:border-youtube-red dark:bg-gray-800 dark:text-white"
            disabled={isLoading}
          />
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <label htmlFor="channel" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Channel Name (Optional)
          </label>
          <input
            type="text"
            id="channel"
            value={channelName}
            onChange={(e) => setChannelName(e.target.value)}
            placeholder="e.g., TED"
            className="block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md 
                     focus:ring-youtube-red focus:border-youtube-red dark:bg-gray-800 dark:text-white"
            disabled={isLoading}
          />
        </div>

        <div>
          <label htmlFor="format" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Export Format
          </label>
          <select
            id="format"
            value={format}
            onChange={(e) => setFormat(e.target.value)}
            className="block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md 
                     focus:ring-youtube-red focus:border-youtube-red dark:bg-gray-800 dark:text-white"
            disabled={isLoading}
          >
            <option value="md">Markdown</option>
            <option value="txt">Plain Text</option>
            <option value="srt">SRT Subtitles</option>
            <option value="json">JSON</option>
          </select>
        </div>
      </div>

      <button
        type="submit"
        disabled={isLoading}
        className="w-full flex justify-center items-center px-4 py-2 border border-transparent rounded-md shadow-sm 
                 text-white bg-youtube-red hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 
                 focus:ring-youtube-red disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
      >
        {isLoading ? (
          <>
            <Loader2 className="animate-spin -ml-1 mr-3 h-5 w-5" />
            Extracting...
          </>
        ) : (
          <>
            <Download className="-ml-1 mr-3 h-5 w-5" />
            Extract Transcript
          </>
        )}
      </button>
    </form>
  );
};

export default URLInput;