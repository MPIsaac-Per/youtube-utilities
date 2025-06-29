import React from 'react';
import { FileText, Calendar, Clock } from 'lucide-react';

const formatDate = (dateString) => {
  try {
    // Handle YYYY-MM-DD format
    if (dateString && dateString.match(/^\d{4}-\d{2}-\d{2}$/)) {
      const [year, month, day] = dateString.split('-');
      return `${month}/${day}/${year}`;
    }
    // Try parsing as a date
    const date = new Date(dateString);
    if (!isNaN(date.getTime())) {
      return date.toLocaleDateString();
    }
  } catch (e) {
    console.error('Date parsing error:', e);
  }
  return dateString || 'Unknown date';
};

const formatTime = (dateString) => {
  try {
    const date = new Date(dateString);
    if (!isNaN(date.getTime())) {
      return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }
  } catch (e) {
    console.error('Time parsing error:', e);
  }
  return '';
};

const TranscriptList = ({ transcripts, onSelect }) => {
  if (!transcripts || transcripts.length === 0) {
    return (
      <div className="text-center py-12">
        <FileText className="w-12 h-12 text-gray-400 mx-auto mb-4" />
        <p className="text-gray-500 dark:text-gray-400">No transcripts found</p>
      </div>
    );
  }

  return (
    <div className="grid gap-4 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
      {transcripts.map((transcript) => (
        <div
          key={transcript.video_id}
          onClick={() => onSelect(transcript)}
          className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 hover:shadow-lg 
                   transition-shadow cursor-pointer border border-gray-200 dark:border-gray-700"
        >
          {transcript.video_title ? (
            <h3 className="font-semibold text-gray-900 dark:text-white mb-1 line-clamp-2">
              {transcript.video_title}
            </h3>
          ) : (
            <h3 className="font-semibold text-gray-900 dark:text-white mb-1 truncate">
              {transcript.channel_name}
            </h3>
          )}
          
          <p className="text-sm text-gray-600 dark:text-gray-400 mb-3 truncate">
            {transcript.channel_name}
          </p>
          
          <div className="space-y-2 text-sm text-gray-600 dark:text-gray-400">
            <div className="flex items-center gap-2">
              <Calendar className="w-4 h-4" />
              <span>{formatDate(transcript.video_date)}</span>
            </div>
            
            {transcript.created_at && (
              <div className="flex items-center gap-2">
                <Clock className="w-4 h-4" />
                <span>{formatTime(transcript.created_at)}</span>
              </div>
            )}
          </div>

          <div className="mt-4">
            <p className="text-xs text-gray-500 dark:text-gray-500 truncate">
              ID: {transcript.video_id}
            </p>
          </div>
        </div>
      ))}
    </div>
  );
};

export default TranscriptList;