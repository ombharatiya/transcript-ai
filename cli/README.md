# TranscriptAI CLI Tool

> **Command-line interface for AI-powered audio transcription**

The CLI version of TranscriptAI provides powerful batch processing and advanced features for developers and power users.

## Quick Start

```bash
# Navigate to CLI directory
cd cli

# Set up environment
python setup.py

# Activate environment  
source venv/bin/activate

# Transcribe audio
python src/audio_transcriber.py input/audio.mp3
```

## Features

- 🎵 **8 Audio Formats** - AAC, FLAC, MP3, MP4, M4A, OGG, WAV, WebM
- ⚡ **Batch Processing** - Process multiple files simultaneously
- 🌍 **99+ Languages** - Automatic detection and translation
- 🤖 **7 AI Models** - Choose speed vs accuracy balance
- 📝 **Rich Output** - Text files + JSON with timestamps
- 🔧 **Developer-Friendly** - Comprehensive logging and configuration

## Usage Examples

```bash
# Single file transcription
python src/audio_transcriber.py input/meeting.wav

# Batch processing
python src/audio_transcriber.py input/*.mp3 --batch

# Different model sizes
python src/audio_transcriber.py input/audio.wav --model large

# Language specification
python src/audio_transcriber.py input/audio.aac --language en

# Translation to English
python src/audio_transcriber.py input/foreign.mp3 --task translate
```

## Installation

See the main [README.md](../README.md) for detailed installation instructions.

## Advanced Usage

For complete documentation, see the main project README and the `--help` command:

```bash
python src/audio_transcriber.py --help
```

---

**Prefer a web interface?** Check out the [web version](../web/) at [ombharatiya.github.io/transcript-ai](https://ombharatiya.github.io/transcript-ai)