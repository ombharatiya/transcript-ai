# TranscriptAI Project Structure Plan

## Monorepo Architecture

### Current Structure (CLI-focused)
```
transcript-ai/
├── src/                          # CLI source code
├── input/                        # Sample audio files
├── outputs/                      # Sample transcriptions
├── config/                       # Configuration files
├── temp/                         # User temporary files
├── logs/                         # Application logs
├── requirements.txt              # Python dependencies
├── setup.py                      # CLI setup script
└── README.md                     # Main documentation
```

### Proposed Structure (Monorepo)
```
transcript-ai/
├── cli/                          # Python CLI Tool
│   ├── src/
│   │   └── audio_transcriber.py
│   ├── input/                    # Sample audio files
│   ├── outputs/                  # Sample transcriptions  
│   ├── config/
│   ├── requirements.txt
│   ├── setup.py
│   └── README_CLI.md
│
├── web/                          # Web Interface
│   ├── src/
│   │   ├── index.html
│   │   ├── app.js
│   │   └── styles.css
│   ├── public/
│   ├── dist/                     # Built files for GitHub Pages
│   ├── package.json
│   └── README_WEB.md
│
├── docs/                         # GitHub Pages (symbolic link to web/dist)
│
├── shared/                       # Common resources
│   ├── examples/
│   ├── assets/
│   └── docs/
│
├── .github/
│   ├── workflows/
│   │   ├── test-cli.yml         # CI for Python CLI
│   │   ├── build-web.yml        # Build web interface
│   │   └── deploy-pages.yml     # Deploy to GitHub Pages
│   └── ISSUE_TEMPLATE/
│
├── README.md                     # Main project documentation
├── CONTRIBUTING.md
├── LICENSE
└── CHANGELOG.md
```

## Migration Strategy

### Phase 1: Restructure Current Code
1. Move current CLI code to `cli/` directory
2. Update paths and imports
3. Test CLI functionality
4. Update documentation

### Phase 2: Add Web Interface  
1. Create `web/` directory structure
2. Build HTML/CSS/JS web interface
3. Integrate with OpenAI API or client-side solution
4. Set up build process

### Phase 3: GitHub Pages Deployment
1. Configure GitHub Pages to serve from `docs/`
2. Set up automated deployment
3. Link web interface to main README

### Phase 4: Cross-Integration
1. Add web interface links to CLI
2. Add CLI download links to web interface
3. Unified branding and documentation

## Benefits of This Approach

### For Users
- **Single Source** - Everything in one place
- **Options** - Choose CLI or web based on needs
- **Consistency** - Same features, different interfaces

### For Development
- **Unified Issues** - Track bugs and features in one place
- **Shared Resources** - Common examples, documentation
- **SEO Benefits** - Single repo gets all traffic and stars

### For Maintenance
- **Single Release Cycle** - Coordinate CLI and web releases
- **Consistent Branding** - Same look and feel
- **Cross-Promotion** - CLI users discover web, vice versa

## Technology Stack

### CLI (Existing)
- Python 3.8+
- OpenAI Whisper
- FFmpeg
- Click/Argparse

### Web Interface
- HTML5/CSS3/JavaScript
- OpenAI API (with user's key)
- Web Audio API
- Modern responsive design

### Build & Deploy
- GitHub Actions
- GitHub Pages
- Automated testing for both CLI and web