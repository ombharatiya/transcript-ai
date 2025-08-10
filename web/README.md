# TranscriptAI Web Interface

> **Browser-based AI transcription tool - No installation required!**

Access TranscriptAI directly in your browser at **[ombharatiya.github.io/transcript-ai](https://ombharatiya.github.io/transcript-ai)**

## ✨ Features

### 🎵 Universal Audio Support
- **8 Audio Formats**: MP3, WAV, M4A, AAC, FLAC, OGG, WebM, MP4
- **Drag & Drop**: Simply drag files into the browser
- **File Size**: Up to 25MB per file
- **Quality**: Supports all sample rates and bit depths

### 🤖 AI-Powered Transcription
- **Multiple Models**: Choose from 4 Whisper model sizes
- **Language Detection**: Automatic detection of 99+ languages  
- **Translation**: Built-in translation to English
- **High Accuracy**: State-of-the-art OpenAI Whisper technology

### 🌐 Web-Optimized
- **No Installation**: Works in any modern browser
- **Mobile Friendly**: Responsive design for all devices
- **Privacy First**: Files processed securely, never stored
- **Instant Results**: Get transcriptions in seconds

### 📱 User Experience
- **Intuitive Interface**: Clean, modern design
- **Real-time Progress**: Visual progress indicators
- **Copy & Download**: Easy result management
- **Error Handling**: Helpful error messages and validation

## 🚀 How to Use

1. **Visit the Web App**
   - Go to [ombharatiya.github.io/transcript-ai](https://ombharatiya.github.io/transcript-ai)
   - No registration or installation required

2. **Upload Your Audio**
   - Click the upload area or drag & drop your file
   - Supported formats: MP3, WAV, M4A, AAC, FLAC, OGG, WebM
   - Maximum file size: 25MB

3. **Configure Options**
   - **Model**: Choose speed vs accuracy (Base recommended)
   - **Language**: Auto-detect or specify language
   - **Translation**: Option to translate to English

4. **Get Results**
   - View transcription in real-time
   - Copy text to clipboard
   - Download as TXT file
   - See processing metadata

## 🛠️ Technical Details

### Architecture
- **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Modern CSS Grid/Flexbox, responsive design
- **APIs**: Web Audio API for file handling
- **Deployment**: GitHub Pages with automated CI/CD

### Browser Support
- **Chrome/Chromium**: Full support
- **Firefox**: Full support  
- **Safari**: Full support
- **Edge**: Full support
- **Mobile**: iOS Safari, Chrome Mobile

### File Processing
```javascript
// Example of audio file validation
function isValidAudioFile(file) {
    const validTypes = [
        'audio/mpeg', 'audio/wav', 'audio/m4a',
        'audio/aac', 'audio/flac', 'audio/ogg'
    ];
    return validTypes.includes(file.type) ||
           /\.(mp3|wav|m4a|aac|flac|ogg|webm)$/i.test(file.name);
}
```

## 🔧 Development

### Local Development
```bash
# Clone the repository
git clone https://github.com/ombharatiya/transcript-ai.git
cd transcript-ai/web

# Serve locally (Python)
python -m http.server 8000

# Or use any static file server
npx http-server src/
```

### Project Structure
```
web/
├── src/
│   ├── index.html      # Main application page
│   ├── styles.css      # All styling and responsive design
│   └── app.js          # Application logic and API handling
├── public/             # Static assets (if needed)
├── dist/               # Built files for deployment
└── README.md           # This file
```

### Adding Features
1. **New audio formats**: Update `isValidAudioFile()` function
2. **UI improvements**: Modify `styles.css` and HTML structure
3. **API integration**: Update transcription logic in `app.js`
4. **Mobile optimization**: Test and adjust responsive breakpoints

## 🚀 Deployment

### Automatic Deployment
The web interface is automatically deployed to GitHub Pages when changes are pushed to the `main` branch:

```yaml
# .github/workflows/deploy-web.yml
- Web source files are copied from web/src/ to docs/
- GitHub Pages serves from docs/ directory  
- Live at: https://ombharatiya.github.io/transcript-ai
```

### Manual Deployment
```bash
# Build and deploy manually
cd web
cp -r src/* ../docs/
git add ../docs/
git commit -m "Update web interface"
git push origin main
```

## 🔮 Future Enhancements

### Planned Features
- **Real-time transcription**: Live audio input from microphone
- **Batch processing**: Multiple file upload and processing
- **Custom vocabulary**: Domain-specific word recognition
- **Export formats**: SRT, VTT subtitle formats
- **Collaboration**: Share transcriptions with others

### Integration Ideas
- **API endpoints**: Backend service integration
- **Webhook support**: Automated workflow triggers
- **Cloud storage**: Direct upload from Google Drive, Dropbox
- **Social sharing**: Share transcriptions on social platforms

## 🤝 Contributing

### Web Interface Contributions
1. Fork the repository
2. Create feature branch: `git checkout -b feature/web-enhancement`
3. Make changes in `web/src/` directory
4. Test locally with static file server
5. Submit pull request

### Testing Guidelines
- Test on multiple browsers and devices
- Verify responsive design on mobile
- Check accessibility with screen readers
- Validate with various audio file formats
- Test error handling scenarios

## 🔗 Links

- **Live Web App**: [ombharatiya.github.io/transcript-ai](https://ombharatiya.github.io/transcript-ai)
- **CLI Tool**: [../cli/README.md](../cli/README.md)
- **GitHub Repository**: [github.com/ombharatiya/transcript-ai](https://github.com/ombharatiya/transcript-ai)
- **Issues & Support**: [GitHub Issues](https://github.com/ombharatiya/transcript-ai/issues)

---

**Ready to transcribe?** Visit the web app now: **[ombharatiya.github.io/transcript-ai](https://ombharatiya.github.io/transcript-ai)** 🎙️ ➜ 📝