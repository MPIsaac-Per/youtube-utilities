import React, { useState } from 'react';
import { Users, Loader2, Download } from 'lucide-react';
import toast from 'react-hot-toast';

const ChannelInput = ({ onExtract, isLoading }) => {
  const [channelName, setChannelName] = useState('');
  const [maxVideos, setMaxVideos] = useState(10);

  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (!channelName.trim()) {
      toast.error('Please enter a channel name');
      return;
    }

    if (maxVideos < 1 || maxVideos > 50) {
      toast.error('Max videos must be between 1 and 50');
      return;
    }

    onExtract(channelName, maxVideos);
  };

  return (
    <form onSubmit={handleSubmit} className="w-full max-w-2xl space-y-4">
      <div>
        <label htmlFor="channel" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
          YouTube Channel Name
        </label>
        <div className="relative">
          <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <Users className="h-5 w-5 text-gray-400" />
          </div>
          <input
            type="text"
            id="channel"
            value={channelName}
            onChange={(e) => setChannelName(e.target.value)}
            placeholder="e.g., TED, Google, MrBeast"
            className="block w-full pl-10 pr-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md 
                     focus:ring-youtube-red focus:border-youtube-red dark:bg-gray-800 dark:text-white"
            disabled={isLoading}
          />
        </div>
      </div>

      <div>
        <label htmlFor="maxVideos" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
          Number of Recent Videos
        </label>
        <input
          type="number"
          id="maxVideos"
          value={maxVideos}
          onChange={(e) => setMaxVideos(parseInt(e.target.value) || 10)}
          min="1"
          max="50"
          className="block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md 
                   focus:ring-youtube-red focus:border-youtube-red dark:bg-gray-800 dark:text-white"
          disabled={isLoading}
        />
        <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">
          Extract transcripts from the {maxVideos} most recent videos
        </p>
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
            Processing Channel...
          </>
        ) : (
          <>
            <Download className="-ml-1 mr-3 h-5 w-5" />
            Extract All Transcripts
          </>
        )}
      </button>
    </form>
  );
};

export default ChannelInput;