# TranscriptAI GitHub Pages

This directory contains the built web interface for TranscriptAI, automatically deployed to GitHub Pages.

**Live URL**: [https://ombharatiya.github.io/transcript-ai](https://ombharatiya.github.io/transcript-ai)

## 🚀 Deployment

This directory is automatically updated by GitHub Actions when changes are made to the `web/src/` directory.

### Build Process
1. Source files from `web/src/` are processed
2. Built files are copied to this `docs/` directory  
3. GitHub Pages serves the content from this directory

### Manual Build
```bash
cd web
npm run build
npm run deploy
```

## 📁 Contents

- `index.html` - Main web application
- `styles.css` - All styling and responsive design
- `app.js` - Application logic and transcription handling

## 🔧 Technology Stack

- **HTML5** - Semantic markup and modern web standards
- **CSS3** - Grid/Flexbox layouts, animations, responsive design
- **Vanilla JavaScript** - ES6+ features, Web APIs
- **GitHub Pages** - Static site hosting and deployment