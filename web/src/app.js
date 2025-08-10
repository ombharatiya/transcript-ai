// TranscriptAI Web Interface JavaScript

class TranscriptAI {
    constructor() {
        this.selectedFile = null;
        this.isTranscribing = false;
        this.initializeElements();
        this.bindEvents();
        this.setupDragAndDrop();
    }

    initializeElements() {
        // File upload elements
        this.uploadArea = document.getElementById('uploadArea');
        this.fileInput = document.getElementById('fileInput');
        
        // Options elements
        this.optionsSection = document.getElementById('optionsSection');
        this.modelSelect = document.getElementById('modelSelect');
        this.languageSelect = document.getElementById('languageSelect');
        this.translateCheck = document.getElementById('translateCheck');
        this.transcribeBtn = document.getElementById('transcribeBtn');
        
        // Results elements
        this.resultsSection = document.getElementById('resultsSection');
        this.progressBar = document.getElementById('progressBar');
        this.transcriptionOutput = document.getElementById('transcriptionOutput');
        this.outputText = document.getElementById('outputText');
        this.transcriptionInfo = document.getElementById('transcriptionInfo');
        this.errorMessage = document.getElementById('errorMessage');
        this.errorText = document.getElementById('errorText');
        
        // Action buttons
        this.copyBtn = document.getElementById('copyBtn');
        this.downloadBtn = document.getElementById('downloadBtn');
    }

    bindEvents() {
        // File upload events
        this.uploadArea.addEventListener('click', () => this.fileInput.click());
        this.fileInput.addEventListener('change', (e) => this.handleFileSelect(e.target.files[0]));
        
        // Transcription button
        this.transcribeBtn.addEventListener('click', () => this.startTranscription());
        
        // Action buttons
        this.copyBtn.addEventListener('click', () => this.copyToClipboard());
        this.downloadBtn.addEventListener('click', () => this.downloadTranscription());
        
        // Navigation smooth scroll
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });
    }

    setupDragAndDrop() {
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            this.uploadArea.addEventListener(eventName, this.preventDefaults, false);
            document.body.addEventListener(eventName, this.preventDefaults, false);
        });

        ['dragenter', 'dragover'].forEach(eventName => {
            this.uploadArea.addEventListener(eventName, () => {
                this.uploadArea.classList.add('dragover');
            }, false);
        });

        ['dragleave', 'drop'].forEach(eventName => {
            this.uploadArea.addEventListener(eventName, () => {
                this.uploadArea.classList.remove('dragover');
            }, false);
        });

        this.uploadArea.addEventListener('drop', (e) => {
            const files = e.dataTransfer.files;
            if (files.length > 0) {
                this.handleFileSelect(files[0]);
            }
        }, false);
    }

    preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    handleFileSelect(file) {
        if (!file) return;

        // Validate file type
        if (!this.isValidAudioFile(file)) {
            this.showError('Please select a valid audio file (MP3, WAV, M4A, AAC, FLAC, OGG, WebM)');
            return;
        }

        // Validate file size (25MB limit)
        if (file.size > 25 * 1024 * 1024) {
            this.showError('File size must be less than 25MB');
            return;
        }

        this.selectedFile = file;
        this.updateUploadArea(file);
        this.showOptions();
        this.clearResults();
    }

    isValidAudioFile(file) {
        const validTypes = [
            'audio/mpeg', 'audio/mp3', 'audio/wav', 'audio/wave', 
            'audio/x-wav', 'audio/m4a', 'audio/mp4', 'audio/aac',
            'audio/flac', 'audio/ogg', 'audio/webm'
        ];
        return validTypes.includes(file.type) || 
               /\.(mp3|wav|m4a|aac|flac|ogg|webm)$/i.test(file.name);
    }

    updateUploadArea(file) {
        const uploadText = this.uploadArea.querySelector('.upload-text');
        const uploadIcon = this.uploadArea.querySelector('.upload-icon');
        
        uploadIcon.className = 'fas fa-file-audio upload-icon';
        uploadText.innerHTML = `
            <strong>${file.name}</strong><br>
            <span style="color: #666; font-size: 0.9rem;">
                ${this.formatFileSize(file.size)} • ${file.type || 'Audio file'}
            </span>
        `;
    }

    formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }

    showOptions() {
        this.optionsSection.style.display = 'block';
        this.optionsSection.classList.add('slide-up');
        this.transcribeBtn.disabled = false;
    }

    clearResults() {
        this.resultsSection.style.display = 'none';
        this.progressBar.style.display = 'none';
        this.transcriptionOutput.style.display = 'none';
        this.errorMessage.style.display = 'none';
    }

    async startTranscription() {
        if (!this.selectedFile || this.isTranscribing) return;

        this.isTranscribing = true;
        this.transcribeBtn.disabled = true;
        this.transcribeBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
        
        this.showProgress();
        this.clearError();

        try {
            // Simulate API call since we can't run Whisper directly in browser
            // In a real implementation, you would:
            // 1. Upload file to your backend server
            // 2. Process with Whisper on server
            // 3. Return results to frontend
            
            const result = await this.simulateTranscription();
            this.showResult(result);
            
        } catch (error) {
            this.showError('Transcription failed: ' + error.message);
        } finally {
            this.isTranscribing = false;
            this.transcribeBtn.disabled = false;
            this.transcribeBtn.innerHTML = '<i class="fas fa-magic"></i> Start Transcription';
            this.hideProgress();
        }
    }

    showProgress() {
        this.resultsSection.style.display = 'block';
        this.progressBar.style.display = 'block';
        this.resultsSection.classList.add('fade-in');
        
        // Animate progress bar
        const progressFill = this.progressBar.querySelector('.progress-fill');
        let progress = 0;
        const interval = setInterval(() => {
            progress += Math.random() * 15;
            if (progress > 90) progress = 90;
            progressFill.style.width = progress + '%';
        }, 200);

        // Store interval to clear later
        this.progressInterval = interval;
    }

    hideProgress() {
        if (this.progressInterval) {
            clearInterval(this.progressInterval);
        }
        this.progressBar.style.display = 'none';
    }

    async simulateTranscription() {
        // This is a demo implementation
        // In production, you would send the audio file to your backend API
        
        return new Promise((resolve) => {
            setTimeout(() => {
                const demoTranscriptions = [
                    "Thank you for trying TranscriptAI! This is a demonstration of our AI-powered transcription service. In a real implementation, your audio file would be processed using OpenAI's Whisper model to provide accurate speech-to-text conversion.",
                    "Welcome to TranscriptAI. This powerful tool can transcribe audio in multiple languages with high accuracy. The service supports various audio formats including MP3, WAV, M4A, and more.",
                    "Hello! This is a sample transcription result. TranscriptAI uses advanced AI technology to convert your speech to text quickly and accurately. You can process multiple languages and audio formats."
                ];
                
                const randomTranscription = demoTranscriptions[Math.floor(Math.random() * demoTranscriptions.length)];
                
                resolve({
                    text: randomTranscription,
                    language: this.languageSelect.value === 'auto' ? 'en' : this.languageSelect.value,
                    model: this.modelSelect.value,
                    duration: '00:00:' + (15 + Math.floor(Math.random() * 45)).toString().padStart(2, '0'),
                    fileSize: this.formatFileSize(this.selectedFile.size)
                });
            }, 2000 + Math.random() * 3000); // Random delay 2-5 seconds
        });
    }

    showResult(result) {
        this.outputText.textContent = result.text;
        this.transcriptionInfo.innerHTML = `
            <div><strong>Language:</strong> ${this.getLanguageName(result.language)}</div>
            <div><strong>Model:</strong> ${result.model}</div>
            <div><strong>Duration:</strong> ${result.duration}</div>
            <div><strong>File Size:</strong> ${result.fileSize}</div>
        `;
        
        this.transcriptionOutput.style.display = 'block';
        this.transcriptionOutput.classList.add('slide-up');
        
        // Store result for download
        this.currentResult = result;
    }

    getLanguageName(code) {
        const languages = {
            'auto': 'Auto-detected',
            'en': 'English',
            'es': 'Spanish',
            'fr': 'French',
            'de': 'German',
            'it': 'Italian',
            'pt': 'Portuguese',
            'ru': 'Russian',
            'ja': 'Japanese',
            'ko': 'Korean',
            'zh': 'Chinese'
        };
        return languages[code] || code;
    }

    showError(message) {
        this.errorText.textContent = message;
        this.errorMessage.style.display = 'flex';
        this.resultsSection.style.display = 'block';
    }

    clearError() {
        this.errorMessage.style.display = 'none';
    }

    async copyToClipboard() {
        try {
            await navigator.clipboard.writeText(this.outputText.textContent);
            
            // Show feedback
            const originalText = this.copyBtn.innerHTML;
            this.copyBtn.innerHTML = '<i class="fas fa-check"></i> Copied!';
            this.copyBtn.style.background = '#28a745';
            
            setTimeout(() => {
                this.copyBtn.innerHTML = originalText;
                this.copyBtn.style.background = '';
            }, 2000);
            
        } catch (err) {
            // Fallback for older browsers
            const textArea = document.createElement('textarea');
            textArea.value = this.outputText.textContent;
            document.body.appendChild(textArea);
            textArea.focus();
            textArea.select();
            
            try {
                document.execCommand('copy');
                this.copyBtn.innerHTML = '<i class="fas fa-check"></i> Copied!';
            } catch (err) {
                console.error('Copy failed:', err);
            }
            
            document.body.removeChild(textArea);
        }
    }

    downloadTranscription() {
        if (!this.currentResult) return;
        
        const content = `TranscriptAI Transcription Result
=====================================

File: ${this.selectedFile.name}
Language: ${this.getLanguageName(this.currentResult.language)}
Model: ${this.currentResult.model}
Duration: ${this.currentResult.duration}
Processed: ${new Date().toLocaleString()}

Transcription:
${this.currentResult.text}

---
Generated by TranscriptAI - https://ombharatiya.github.io/transcript-ai
`;

        const blob = new Blob([content], { type: 'text/plain' });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        
        const fileName = this.selectedFile.name.replace(/\.[^/.]+$/, '') + '_transcription.txt';
        a.href = url;
        a.download = fileName;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new TranscriptAI();
    
    // Add some nice animations to elements when they come into view
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);
    
    // Observe feature cards and steps
    document.querySelectorAll('.feature-card, .step').forEach(el => {
        observer.observe(el);
    });
});

// Add some interactive effects
document.addEventListener('DOMContentLoaded', () => {
    // Parallax effect for hero section
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const hero = document.querySelector('.hero');
        if (hero) {
            hero.style.transform = `translateY(${scrolled * 0.5}px)`;
        }
    });
    
    // Add click effect to buttons
    document.querySelectorAll('.btn-primary, .btn-secondary').forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.cssText = `
                position: absolute;
                border-radius: 50%;
                background: rgba(255,255,255,0.6);
                transform: scale(0);
                animation: ripple 0.6s linear;
                width: ${size}px;
                height: ${size}px;
                left: ${x}px;
                top: ${y}px;
                pointer-events: none;
            `;
            
            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
});

// Add ripple animation CSS
const style = document.createElement('style');
style.textContent = `
    @keyframes ripple {
        to {
            transform: scale(2);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);