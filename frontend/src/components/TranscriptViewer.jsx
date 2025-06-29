import React from 'react';
import { Copy, Download, X } from 'lucide-react';
import toast from 'react-hot-toast';

const TranscriptViewer = ({ transcript, onClose }) => {
  if (!transcript) return null;

  const handleCopy = () => {
    navigator.clipboard.writeText(transcript.transcript_text);
    toast.success('Transcript copied to clipboard');
  };

  const handleDownload = () => {
    const blob = new Blob([transcript.transcript_text], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${transcript.video_id}-transcript.${transcript.format}`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    toast.success('Transcript downloaded');
  };

  const formatDuration = (seconds) => {
    if (!seconds) return '';
    const hrs = Math.floor(seconds / 3600);
    const mins = Math.floor((seconds % 3600) / 60);
    const secs = Math.floor(seconds % 60);
    return `${hrs > 0 ? hrs + 'h ' : ''}${mins}m ${secs}s`;
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow-xl max-w-4xl w-full max-h-[90vh] flex flex-col">
        <div className="flex justify-between items-center p-6 border-b dark:border-gray-700">
          <div className="flex-1 mr-4">
            <h2 className="text-xl font-semibold text-gray-900 dark:text-white">
              {transcript.video_title || 'Transcript Viewer'}
            </h2>
            <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">
              {transcript.channel_name} • {transcript.video_date} 
              {transcript.duration_seconds && ` • ${formatDuration(transcript.duration_seconds)}`}
            </p>
          </div>
          <button
            onClick={onClose}
            className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition-colors"
          >
            <X className="w-5 h-5 text-gray-500 dark:text-gray-400" />
          </button>
        </div>

        <div className="flex-1 overflow-y-auto p-6">
          <pre className="whitespace-pre-wrap text-sm text-gray-700 dark:text-gray-300 font-mono">
            {transcript.transcript_text}
          </pre>
        </div>

        <div className="flex justify-between gap-3 p-6 border-t dark:border-gray-700">
          <button
            onClick={onClose}
            className="flex items-center gap-2 px-4 py-2 text-gray-700 dark:text-gray-300 
                     hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition-colors"
          >
            <X className="w-4 h-4" />
            Close
          </button>
          
          <div className="flex gap-3">
            <button
              onClick={handleCopy}
              className="flex items-center gap-2 px-4 py-2 text-gray-700 dark:text-gray-300 
                       hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition-colors"
            >
              <Copy className="w-4 h-4" />
              Copy
            </button>
            <button
              onClick={handleDownload}
              className="flex items-center gap-2 px-4 py-2 bg-youtube-red text-white 
                       hover:bg-red-700 rounded-lg transition-colors"
            >
              <Download className="w-4 h-4" />
              Download
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TranscriptViewer;