# Input Folder

Place your audio files here for transcription.

## Supported Formats

- **AAC** (.aac) - Advanced Audio Coding
- **FLAC** (.flac) - Free Lossless Audio Codec  
- **MP3** (.mp3) - MPEG Audio Layer III
- **MP4** (.mp4) - MPEG-4 Audio
- **M4A** (.m4a) - MPEG-4 Audio
- **OGG** (.ogg) - Ogg Vorbis
- **WAV** (.wav) - Waveform Audio File Format
- **WebM** (.webm) - WebM Audio

## Usage Examples

```bash
# Single file
python src/audio_transcriber.py input/meeting.mp3

# Multiple files
python src/audio_transcriber.py input/*.wav --batch

# With custom output location
python src/audio_transcriber.py input/podcast.m4a --output-dir transcripts/
```

## Sample Files

The sample files in this folder demonstrate different use cases:
- `sample_meeting.wav` - Business meeting recording
- `sample_interview.mp3` - Interview transcript
- `sample_lecture.m4a` - Educational content