# Audio Transcription Tool

A powerful, user-friendly audio transcription tool built with OpenAI's Whisper model. Supports multiple audio formats and provides flexible transcription options with batch processing capabilities.

## Features

- 🎵 **Multiple Audio Format Support**: AAC, FLAC, MP3, MP4, M4A, OGG, WAV, WebM
- 🤖 **Multiple Whisper Models**: From tiny (39MB) to large-v3 (1550MB)
- 🌍 **Language Support**: Auto-detection or specify language codes
- 📝 **Dual Output**: Plain text and detailed JSON with timestamps
- 🔄 **Batch Processing**: Process multiple files at once
- 📊 **Detailed Logging**: Track transcription progress and errors
- 🛠 **Easy Setup**: Automated dependency management

## Project Structure

```
speechtotext/
├── src/
│   └── audio_transcriber.py      # Main transcription script
├── input/                        # Place audio files here
│   ├── sample_meeting.wav        # Sample business meeting
│   ├── sample_interview.mp3      # Sample interview
│   └── sample_lecture.m4a        # Sample educational content
├── outputs/                      # Transcription results
│   ├── sample_meeting_transcription.txt
│   └── sample_meeting_detailed.json
├── config/
│   └── default_config.json      # Configuration settings
├── temp/                         # Your personal files (git-ignored)
├── logs/                         # Application logs
├── venv/                         # Python virtual environment
├── requirements.txt              # Python dependencies
├── setup.py                      # Automated setup script
└── README.md                     # This file
```

## Installation

### Prerequisites

- Python 3.8 or higher
- macOS, Linux, or Windows

### Automatic Setup (Recommended)

```bash
# Clone or download this project
cd speechtotext

# Run the setup script (handles everything automatically)
python setup.py
```

The setup script will:
- Create Python virtual environment
- Install Python dependencies
- Install ffmpeg (system-wide or locally)
- Configure everything for immediate use

### Manual Setup

If you prefer manual installation:

1. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install FFmpeg**
   ```bash
   # macOS
   brew install ffmpeg
   
   # Ubuntu/Debian
   sudo apt update && sudo apt install ffmpeg
   
   # Windows
   # Download from https://ffmpeg.org/download.html and add to PATH
   ```

## Usage

### Basic Transcription

```bash
# Activate environment
source venv/bin/activate

# Transcribe a single file
python src/audio_transcriber.py input/audio.mp3

# Use a different model
python src/audio_transcriber.py input/audio.wav --model large

# Specify language
python src/audio_transcriber.py input/audio.aac --language en
```

### Advanced Options

```bash
# Translate to English
python src/audio_transcriber.py input/foreign_audio.mp3 --task translate

# Adjust sampling temperature for creative/technical content
python src/audio_transcriber.py input/audio.wav --temperature 0.2

# Custom output directory
python src/audio_transcriber.py input/audio.mp3 --output-dir /custom/path

# Skip detailed JSON output
python src/audio_transcriber.py input/audio.mp3 --no-json
```

### Batch Processing

```bash
# Process multiple files
python src/audio_transcriber.py input/*.mp3 --batch

# Process specific files
python src/audio_transcriber.py input/file1.wav input/file2.aac input/file3.mp3

# Batch with custom settings
python src/audio_transcriber.py input/*.wav --batch --model medium --language es
```

### File Information

```bash
# Check audio file details
python src/audio_transcriber.py input/audio.mp3 --info
```

## Whisper Models

| Model    | Size   | Speed    | Quality | Use Case |
|----------|--------|----------|---------|----------|
| tiny     | 39 MB  | Fastest  | Basic   | Quick tests, low-resource |
| base     | 74 MB  | Fast     | Good    | General use (default) |
| small    | 244 MB | Moderate | Better  | Good balance |
| medium   | 769 MB | Slower   | High    | Professional transcription |
| large    | 1550 MB| Slowest  | Best    | Highest accuracy needed |
| large-v2 | 1550 MB| Slowest  | Best    | Latest improvements |
| large-v3 | 1550 MB| Slowest  | Best    | Most recent version |

## Supported Audio Formats

- **AAC** (.aac) - Advanced Audio Coding
- **FLAC** (.flac) - Free Lossless Audio Codec
- **MP3** (.mp3) - MPEG Audio Layer III
- **MP4** (.mp4) - MPEG-4 Audio
- **M4A** (.m4a) - MPEG-4 Audio
- **OGG** (.ogg) - Ogg Vorbis
- **WAV** (.wav) - Waveform Audio File Format
- **WebM** (.webm) - WebM Audio

## Output Files

### Text Output
- **Filename**: `{original_name}_transcription.txt`
- **Content**: Clean transcribed text

### JSON Output (Detailed)
- **Filename**: `{original_name}_detailed.json`
- **Content**: 
  - Full transcription text
  - Word-level timestamps
  - Segment information
  - File metadata
  - Model and processing details

### Example JSON Structure
```json
{
  "text": "Your transcribed text here...",
  "segments": [
    {
      "id": 0,
      "seek": 0,
      "start": 0.0,
      "end": 5.0,
      "text": " Your transcribed text here...",
      "tokens": [50364, 2396, ...],
      "temperature": 0.0,
      "avg_logprob": -0.5,
      "compression_ratio": 1.2,
      "no_speech_prob": 0.1
    }
  ],
  "language": "en",
  "metadata": {
    "file_info": {
      "filename": "audio.mp3",
      "size_mb": 5.2,
      "format": ".mp3",
      "supported": true
    },
    "model_used": "base",
    "transcription_time": "0:00:30.123456",
    "timestamp": "2024-01-01T12:00:00.000000"
  }
}
```

## Configuration

Edit `config/default_config.json` to customize default settings:

```json
{
  "model_settings": {
    "default_model": "base",
    "default_language": null,
    "default_task": "transcribe",
    "default_temperature": 0.0
  },
  "output_settings": {
    "output_directory": "outputs",
    "save_json_details": true,
    "log_directory": "logs"
  }
}
```

## Examples

### Personal Voice Notes
```bash
python src/audio_transcriber.py input/voice_memo.m4a
```

### Meeting Recordings
```bash
python src/audio_transcriber.py input/meeting.wav --model medium --output-dir meetings/
```

### Podcast Episodes
```bash
python src/audio_transcriber.py input/podcast_*.mp3 --batch --model large
```

### Foreign Language Content
```bash
python src/audio_transcriber.py input/spanish_audio.mp3 --language es --task translate
```

## Troubleshooting

### Common Issues

**1. FFmpeg not found**
```bash
# Install ffmpeg using the setup script:
python setup.py

# Or install manually:
# macOS
brew install ffmpeg

# Ubuntu/Debian  
sudo apt install ffmpeg

# Windows: Download from https://ffmpeg.org/download.html
```

**2. Out of memory errors**
```bash
# Use a smaller model
python src/audio_transcriber.py large_file.mp3 --model tiny
```

**3. Slow transcription**
```bash
# Use GPU acceleration if available (requires CUDA setup)
# Or use smaller model for faster processing
python src/audio_transcriber.py file.mp3 --model small
```

**4. Unsupported file format**
```bash
# Check supported formats
python src/audio_transcriber.py input/file.xyz --info

# Convert using ffmpeg
ffmpeg -i input/file.xyz -c:a aac input/output.aac
```

### Performance Tips

1. **Choose appropriate model size** based on your needs
2. **Use batch processing** for multiple files
3. **Specify language** when known (saves detection time)
4. **Use SSD storage** for better I/O performance
5. **Close other applications** for memory-intensive models

## Logging

Logs are automatically saved to `logs/transcription_YYYYMMDD.log` and include:
- Processing start/end times
- File information
- Error messages
- Model loading status
- Transcription progress

## Requirements

- Python 3.8+
- ~2GB RAM (for base model)
- ~8GB RAM (for large models)
- FFmpeg (auto-configured)
- Internet connection (first run to download models)

## License

This project uses OpenAI's Whisper model. Please refer to [Whisper's license](https://github.com/openai/whisper/blob/main/LICENSE) for usage terms.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for the transcription model
- [FFmpeg](https://ffmpeg.org/) for audio processing

---

**Happy Transcribing! 🎙️ ➜ 📝**