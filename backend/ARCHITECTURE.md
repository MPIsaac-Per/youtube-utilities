# Backend Architecture

## Overview

This backend follows a clean, layered architecture pattern to ensure proper separation of concerns, maintainability, and testability.

## Layers

### 1. Presentation Layer (`app.py`)
- **Responsibility**: Handle HTTP requests/responses, validation, and API endpoints
- **Dependencies**: Service layer only
- **Key Components**:
  - FastAPI endpoints
  - Request/response models
  - Error handling middleware
  - Background job management

### 2. Service Layer (`services/`)
- **Responsibility**: Business logic and orchestration
- **Dependencies**: Repository layer
- **Key Components**:
  - `TranscriptService`: Handles transcript extraction logic
  - Formats transcripts based on export type
  - Orchestrates between YouTube API and file storage

### 3. Repository Layer (`repositories/`)
- **Responsibility**: Data access and external API integration
- **Dependencies**: None (except external libraries)
- **Key Components**:
  - `TranscriptRepository`: File system operations
  - `YouTubeRepository`: YouTube API operations

## Benefits

1. **Separation of Concerns**: Each layer has a single, well-defined responsibility
2. **Testability**: Each layer can be tested independently with mocks
3. **Maintainability**: Changes in one layer don't affect others
4. **Scalability**: Easy to swap implementations (e.g., file storage → database)
5. **Error Handling**: Centralized and consistent across layers

## Anti-Patterns Fixed

1. ✅ **No direct imports between non-adjacent layers**
   - API endpoints don't directly import transcript extraction functions
   - All communication goes through proper interfaces

2. ✅ **Proper error handling at each layer**
   - Repository layer handles data access errors
   - Service layer handles business logic errors
   - API layer handles HTTP-specific errors

3. ✅ **No business logic in presentation layer**
   - Formatting functions moved to service layer
   - API endpoints only handle HTTP concerns

4. ✅ **No data access in presentation layer**
   - File operations isolated in repository layer
   - API endpoints use service layer for all operations

## Future Improvements

1. **Dependency Injection**: Use a DI container for better testability
2. **Interface Definitions**: Define abstract base classes for repositories
3. **Caching Layer**: Add Redis for job storage and caching
4. **Event-Driven**: Use message queues for long-running tasks
5. **Database Storage**: Replace file system with proper database

## Migration Guide

To migrate from the old architecture:

1. Replace imports in `app.py`:
   ```python
   # Old
   from extract_transcript import extract_transcript
   
   # New
   from backend.services.transcript_service import TranscriptService
   ```

2. Use service methods instead of direct calls:
   ```python
   # Old
   extract_transcript(url, output_dir, channel, date)
   
   # New
   transcript_service.extract_single_transcript(url, channel, date, format)
   ```

3. Handle errors properly:
   ```python
   # Old
   transcript = extract_transcript(...)  # May fail silently
   
   # New
   try:
       transcript = transcript_service.extract_single_transcript(...)
   except Exception as e:
       raise HTTPException(status_code=500, detail=str(e))
   ```