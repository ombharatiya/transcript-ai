#!/usr/bin/env python3
"""
Setup script for Audio Transcription Tool
Handles automatic installation of dependencies including ffmpeg
"""

import os
import sys
import subprocess
import platform
import urllib.request
import zipfile
import tarfile
import shutil
from pathlib import Path


def run_command(cmd, check=True):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(cmd, shell=True, check=check, 
                              capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return False, e.stdout, e.stderr


def check_ffmpeg():
    """Check if ffmpeg is available in PATH."""
    success, _, _ = run_command("ffmpeg -version", check=False)
    return success


def install_ffmpeg_macos():
    """Install ffmpeg on macOS."""
    print("Installing ffmpeg on macOS...")
    
    # Try Homebrew first
    success, _, _ = run_command("which brew", check=False)
    if success:
        print("Installing via Homebrew...")
        success, stdout, stderr = run_command("brew install ffmpeg", check=False)
        if success:
            print("✓ ffmpeg installed via Homebrew")
            return True
        else:
            print(f"Homebrew installation failed: {stderr}")
    
    # Fallback: Download static binary
    print("Downloading static ffmpeg binary...")
    arch = platform.machine().lower()
    if arch == 'arm64':
        url = "https://evermeet.cx/ffmpeg/ffmpeg-7.1.zip"
    else:
        url = "https://evermeet.cx/ffmpeg/ffmpeg-7.1.zip"
    
    try:
        urllib.request.urlretrieve(url, "ffmpeg.zip")
        with zipfile.ZipFile("ffmpeg.zip", 'r') as zip_ref:
            zip_ref.extract("ffmpeg", ".")
        os.chmod("ffmpeg", 0o755)
        os.remove("ffmpeg.zip")
        
        # Add to user's PATH (in their shell profile)
        current_dir = Path.cwd()
        shell_profile = Path.home() / ".zshrc"  # Default for modern macOS
        if not shell_profile.exists():
            shell_profile = Path.home() / ".bash_profile"
        
        path_line = f'export PATH="{current_dir}:$PATH"'
        
        try:
            with open(shell_profile, "r") as f:
                content = f.read()
            
            if str(current_dir) not in content:
                with open(shell_profile, "a") as f:
                    f.write(f"\n# Added by audio transcription tool\n{path_line}\n")
                print(f"✓ Added to {shell_profile}")
                print("⚠️  Please run 'source ~/.zshrc' or restart terminal")
        except:
            pass
        
        print("✓ ffmpeg binary downloaded and configured")
        return True
        
    except Exception as e:
        print(f"Failed to download ffmpeg: {e}")
        return False


def install_ffmpeg_linux():
    """Install ffmpeg on Linux."""
    print("Installing ffmpeg on Linux...")
    
    # Try common package managers
    distro_commands = [
        ("apt", "sudo apt update && sudo apt install -y ffmpeg"),
        ("yum", "sudo yum install -y ffmpeg"),
        ("dnf", "sudo dnf install -y ffmpeg"),
        ("pacman", "sudo pacman -S ffmpeg"),
        ("zypper", "sudo zypper install ffmpeg"),
    ]
    
    for pkg_manager, cmd in distro_commands:
        if run_command(f"which {pkg_manager}", check=False)[0]:
            print(f"Installing via {pkg_manager}...")
            success, stdout, stderr = run_command(cmd, check=False)
            if success:
                print(f"✓ ffmpeg installed via {pkg_manager}")
                return True
    
    print("❌ Could not install ffmpeg automatically")
    print("Please install ffmpeg manually:")
    print("  Ubuntu/Debian: sudo apt install ffmpeg")
    print("  CentOS/RHEL:   sudo yum install ffmpeg")
    print("  Arch:          sudo pacman -S ffmpeg")
    return False


def install_ffmpeg_windows():
    """Install ffmpeg on Windows."""
    print("❌ Automatic ffmpeg installation not supported on Windows")
    print("Please install ffmpeg manually:")
    print("1. Download from: https://ffmpeg.org/download.html#build-windows")
    print("2. Extract to C:\\ffmpeg")
    print("3. Add C:\\ffmpeg\\bin to your PATH")
    print("4. Restart command prompt")
    return False


def install_ffmpeg():
    """Install ffmpeg based on the current platform."""
    if check_ffmpeg():
        print("✓ ffmpeg is already installed")
        return True
    
    system = platform.system().lower()
    
    if system == "darwin":
        return install_ffmpeg_macos()
    elif system == "linux":
        return install_ffmpeg_linux()
    elif system == "windows":
        return install_ffmpeg_windows()
    else:
        print(f"❌ Unsupported platform: {system}")
        return False


def setup_python_environment():
    """Set up Python virtual environment and install dependencies."""
    print("Setting up Python environment...")
    
    # Create virtual environment if it doesn't exist
    if not Path("venv").exists():
        print("Creating virtual environment...")
        success, _, stderr = run_command(f"{sys.executable} -m venv venv")
        if not success:
            print(f"❌ Failed to create virtual environment: {stderr}")
            return False
        print("✓ Virtual environment created")
    
    # Determine activation command
    if platform.system().lower() == "windows":
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"
    
    # Install requirements
    if Path("requirements.txt").exists():
        print("Installing Python dependencies...")
        success, _, stderr = run_command(f"{pip_cmd} install -r requirements.txt")
        if not success:
            print(f"❌ Failed to install requirements: {stderr}")
            return False
        print("✓ Python dependencies installed")
    
    return True


def main():
    """Main setup function."""
    print("🎵 Audio Transcription Tool Setup")
    print("=" * 40)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher required")
        sys.exit(1)
    print(f"✓ Python {sys.version.split()[0]} detected")
    
    # Setup Python environment
    if not setup_python_environment():
        print("❌ Python setup failed")
        sys.exit(1)
    
    # Install ffmpeg
    if not install_ffmpeg():
        print("⚠️  ffmpeg installation failed or requires manual setup")
        print("The tool will still work if you install ffmpeg manually")
    
    print("\n" + "=" * 40)
    print("🎉 Setup complete!")
    print("\nNext steps:")
    
    if platform.system().lower() == "windows":
        print("1. Activate environment: venv\\Scripts\\activate")
    else:
        print("1. Activate environment: source venv/bin/activate")
    
    print("2. Test installation:")
    print("   python src/audio_transcriber.py --help")
    print("3. Transcribe audio:")
    print("   python src/audio_transcriber.py your_audio.mp3")


if __name__ == "__main__":
    main()