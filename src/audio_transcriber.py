#!/usr/bin/env python3
"""
Advanced Audio Transcription Tool

Supports multiple audio formats and provides flexible transcription options
using OpenAI's Whisper model.
"""

import whisper
import sys
import os
import json
import logging
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import argparse

class AudioTranscriber:
    """Enhanced audio transcription class with support for multiple formats and features."""
    
    SUPPORTED_FORMATS = {
        '.aac', '.flac', '.mp3', '.mp4', '.m4a', '.ogg', '.wav', '.webm'
    }
    
    WHISPER_MODELS = ['tiny', 'base', 'small', 'medium', 'large', 'large-v2', 'large-v3']
    
    def __init__(self, model_size: str = "base", output_dir: str = "outputs"):
        """Initialize the transcriber with model and output directory."""
        self.model_size = model_size
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.model = None
        self._setup_logging()
        self._setup_ffmpeg_path()
    
    def _setup_logging(self):
        """Set up logging configuration."""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_dir / f"transcription_{datetime.now().strftime('%Y%m%d')}.log"),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def _setup_ffmpeg_path(self):
        """Check ffmpeg availability and add local binary to PATH if it exists."""
        # First check if ffmpeg is in system PATH
        try:
            subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
            self.logger.info("Using system ffmpeg")
            return
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
        
        # Check for local ffmpeg binary
        current_dir = Path(__file__).parent.parent
        ffmpeg_path = current_dir / "ffmpeg"
        if ffmpeg_path.exists():
            os.environ['PATH'] = f"{current_dir}:{os.environ.get('PATH', '')}"
            self.logger.info("Using local ffmpeg binary")
        else:
            self.logger.warning("ffmpeg not found in PATH or locally. Please install ffmpeg.")
    
    def load_model(self):
        """Load the Whisper model."""
        if self.model is None:
            self.logger.info(f"Loading Whisper model ({self.model_size})...")
            self.model = whisper.load_model(self.model_size)
            self.logger.info("Model loaded successfully")
    
    def is_supported_format(self, file_path: str) -> bool:
        """Check if the audio file format is supported."""
        return Path(file_path).suffix.lower() in self.SUPPORTED_FORMATS
    
    def get_audio_info(self, file_path: str) -> Dict:
        """Get basic information about the audio file."""
        file_path = Path(file_path)
        return {
            'filename': file_path.name,
            'size_mb': round(file_path.stat().st_size / 1024 / 1024, 2),
            'format': file_path.suffix.lower(),
            'supported': self.is_supported_format(str(file_path))
        }
    
    def transcribe_audio(self, 
                        audio_file_path: str, 
                        language: Optional[str] = None,
                        task: str = "transcribe",
                        temperature: float = 0.0,
                        save_json: bool = True) -> Dict:
        """
        Transcribe an audio file using OpenAI Whisper.
        
        Args:
            audio_file_path: Path to the audio file
            language: Language code (e.g., 'en', 'es', 'fr')
            task: Either 'transcribe' or 'translate'
            temperature: Temperature for sampling (0.0 to 1.0)
            save_json: Whether to save detailed JSON output
        
        Returns:
            Dictionary containing transcription results
        """
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError(f"Audio file not found: {audio_file_path}")
        
        if not self.is_supported_format(audio_file_path):
            raise ValueError(f"Unsupported audio format. Supported: {', '.join(self.SUPPORTED_FORMATS)}")
        
        self.load_model()
        
        # Get file info
        audio_info = self.get_audio_info(audio_file_path)
        self.logger.info(f"Transcribing: {audio_info['filename']} ({audio_info['size_mb']} MB)")
        
        # Transcription options
        options = {
            "task": task,
            "temperature": temperature
        }
        if language:
            options["language"] = language
        
        # Perform transcription
        start_time = datetime.now()
        result = self.model.transcribe(audio_file_path, **options)
        end_time = datetime.now()
        
        # Add metadata
        result['metadata'] = {
            'file_info': audio_info,
            'model_used': self.model_size,
            'transcription_time': str(end_time - start_time),
            'timestamp': start_time.isoformat(),
            'options_used': options
        }
        
        # Save results
        self._save_results(audio_file_path, result, save_json)
        
        return result
    
    def _save_results(self, audio_file_path: str, result: Dict, save_json: bool):
        """Save transcription results to files."""
        audio_file = Path(audio_file_path)
        base_name = audio_file.stem
        
        # Save text transcription
        text_file = self.output_dir / f"{base_name}_transcription.txt"
        with open(text_file, "w", encoding="utf-8") as f:
            f.write(result["text"])
        
        self.logger.info(f"Text transcription saved to: {text_file}")
        
        # Save JSON with segments and metadata if requested
        if save_json:
            json_file = self.output_dir / f"{base_name}_detailed.json"
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            self.logger.info(f"Detailed results saved to: {json_file}")
    
    def batch_transcribe(self, audio_files: List[str], **kwargs) -> Dict[str, Dict]:
        """Transcribe multiple audio files."""
        results = {}
        
        self.logger.info(f"Starting batch transcription of {len(audio_files)} files")
        
        for i, file_path in enumerate(audio_files, 1):
            try:
                self.logger.info(f"Processing file {i}/{len(audio_files)}: {Path(file_path).name}")
                results[file_path] = self.transcribe_audio(file_path, **kwargs)
            except Exception as e:
                self.logger.error(f"Error processing {file_path}: {e}")
                results[file_path] = {"error": str(e)}
        
        self.logger.info("Batch transcription completed")
        return results


def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(
        description="Advanced Audio Transcription Tool using OpenAI Whisper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python audio_transcriber.py audio.mp3
    python audio_transcriber.py audio.wav --model large --language en
    python audio_transcriber.py *.mp3 --batch
    python audio_transcriber.py audio.aac --task translate --temperature 0.2
        """
    )
    
    parser.add_argument("files", nargs="+", help="Audio file(s) to transcribe")
    parser.add_argument("--model", choices=AudioTranscriber.WHISPER_MODELS, 
                       default="base", help="Whisper model size (default: base)")
    parser.add_argument("--language", help="Language code (e.g., en, es, fr)")
    parser.add_argument("--task", choices=["transcribe", "translate"], 
                       default="transcribe", help="Task to perform")
    parser.add_argument("--temperature", type=float, default=0.0,
                       help="Sampling temperature (0.0 to 1.0)")
    parser.add_argument("--output-dir", default="outputs",
                       help="Output directory for results")
    parser.add_argument("--no-json", action="store_true",
                       help="Don't save detailed JSON output")
    parser.add_argument("--batch", action="store_true",
                       help="Process multiple files in batch mode")
    parser.add_argument("--info", action="store_true",
                       help="Show audio file information only")
    
    args = parser.parse_args()
    
    # Initialize transcriber
    transcriber = AudioTranscriber(
        model_size=args.model,
        output_dir=args.output_dir
    )
    
    # Handle info mode
    if args.info:
        print("\n" + "="*60)
        print("AUDIO FILE INFORMATION")
        print("="*60)
        for file_path in args.files:
            if os.path.exists(file_path):
                info = transcriber.get_audio_info(file_path)
                print(f"\nFile: {info['filename']}")
                print(f"Size: {info['size_mb']} MB")
                print(f"Format: {info['format']}")
                print(f"Supported: {'✓' if info['supported'] else '✗'}")
            else:
                print(f"\nFile not found: {file_path}")
        return 0
    
    try:
        if args.batch or len(args.files) > 1:
            # Batch mode
            results = transcriber.batch_transcribe(
                args.files,
                language=args.language,
                task=args.task,
                temperature=args.temperature,
                save_json=not args.no_json
            )
            
            # Summary
            successful = sum(1 for r in results.values() if "error" not in r)
            print(f"\n{'='*60}")
            print(f"BATCH TRANSCRIPTION COMPLETE")
            print(f"{'='*60}")
            print(f"Processed: {len(args.files)} files")
            print(f"Successful: {successful}")
            print(f"Failed: {len(args.files) - successful}")
            
        else:
            # Single file mode
            result = transcriber.transcribe_audio(
                args.files[0],
                language=args.language,
                task=args.task,
                temperature=args.temperature,
                save_json=not args.no_json
            )
            
            print(f"\n{'='*60}")
            print("TRANSCRIPTION RESULT")
            print(f"{'='*60}")
            print(result["text"])
            print(f"{'='*60}")
            
            if "segments" in result:
                print(f"Segments: {len(result['segments'])}")
            print(f"Language: {result.get('language', 'auto-detected')}")
    
    except KeyboardInterrupt:
        print("\nTranscription interrupted by user")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())