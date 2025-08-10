# 🚀 TranscriptAI Deployment Guide

## GitHub Pages Setup Instructions

### Step 1: Repository Settings
1. Go to your GitHub repository: `https://github.com/ombharatiya/transcript-ai`
2. Click on **Settings** tab
3. Scroll down to **Pages** section (left sidebar)

### Step 2: Configure GitHub Pages Source
**IMPORTANT**: Select **"GitHub Actions"** (not "Deploy from a branch")

1. Under **Source**, click the dropdown
2. Select **"GitHub Actions"**
3. Click **Save**

### Step 3: Enable Workflow Permissions
1. In **Settings**, go to **Actions** → **General**
2. Scroll to **Workflow permissions**
3. Select **"Read and write permissions"**
4. Check ✅ **"Allow GitHub Actions to create and approve pull requests"**
5. Click **Save**

### Step 4: Trigger Deployment
```bash
git add .
git commit -m "Enable GitHub Pages with GitHub Actions workflow"
git push origin main
```

### Step 5: Check Deployment
1. Go to **Actions** tab in your repository
2. Look for the "Deploy to GitHub Pages (Official)" workflow
3. Wait for it to complete (green checkmark)
4. Your site will be live at: **`https://ombharatiya.github.io/transcript-ai`**

## 🔧 Troubleshooting

### If the workflow fails:
1. **Check Actions tab** for error messages
2. **Verify Pages settings** are set to "GitHub Actions" (not branch)
3. **Ensure permissions** are set to "Read and write permissions"

### Manual deployment option:
```bash
# If automated deployment fails, you can deploy manually
cd web
npm run build
npm run deploy
git add ../docs/
git commit -m "Manual deployment update"
git push origin main
```

### Alternative: Direct docs/ folder deployment
If GitHub Actions continues to have issues:

1. **Settings** → **Pages**
2. **Source**: "Deploy from a branch"
3. **Branch**: `main`
4. **Folder**: `/docs`
5. **Save**

The `docs/` folder is already built and ready to serve.

## 📋 What happens when it works:

1. ✅ **Workflow triggers** on push to main (when web/ files change)
2. ✅ **Files are built** from `web/src/` 
3. ✅ **Site deploys** to GitHub Pages
4. ✅ **Live at**: `https://ombharatiya.github.io/transcript-ai`

## 🌐 Expected Result

Your TranscriptAI web interface will be live with:
- 🎵 **File upload** with drag & drop
- 🤖 **AI model selection** 
- 🌍 **Language detection**
- 📝 **Transcription results**
- 📱 **Mobile-responsive design**

---

**Need help?** Check the GitHub Actions logs or create an issue in the repository.