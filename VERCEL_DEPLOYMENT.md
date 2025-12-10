# Deploying to Vercel

## Prerequisites
- [Vercel account](https://vercel.com/signup) (free)
- [Vercel CLI](https://vercel.com/cli) installed: `npm i -g vercel`

## Quick Deployment Steps

### 1. Install Vercel CLI (if not already installed)
```bash
npm i -g vercel
```

### 2. Login to Vercel
```bash
vercel login
```

### 3. Deploy from project directory
```bash
cd /path/to/background-removal-app-python-yt-short-main
vercel
```

Follow the prompts:
- **Set up and deploy?** → Yes
- **Which scope?** → Select your account
- **Link to existing project?** → No
- **Project name?** → Press Enter (or provide custom name)
- **Directory?** → Press Enter (use current directory)
- **Override settings?** → No

### 4. Deploy to production
```bash
vercel --prod
```

## Alternative: Deploy via GitHub

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Click "Add New Project"
4. Import your GitHub repository
5. Vercel will auto-detect the configuration
6. Click "Deploy"

## Environment Variables (Optional)

If you want to use a specific model, add environment variables in Vercel:

1. Go to your project settings on Vercel dashboard
2. Navigate to "Environment Variables"
3. Add:
   - **Key:** `REMBG_MODEL`
   - **Value:** `u2netp` (fast) or `u2net` (quality)

## Important Notes

⚠️ **Limitations on Vercel:**
- **Serverless function timeout:** 10 seconds (Hobby), 60 seconds (Pro)
- **Max payload size:** 4.5 MB
- **Ephemeral storage:** Files saved to `static/uploads/` are temporary and will be lost after the function execution

For large images or heavy processing, consider:
- Upgrading to Vercel Pro for longer timeouts
- Using cloud storage (AWS S3, Cloudflare R2, etc.) instead of local file storage
- Switching to a platform with persistent storage (Railway, Render, etc.)

## Troubleshooting

**Build fails with model download timeout?**
- The first deployment may take longer as it downloads the AI model
- Try deploying with `u2netp` (faster, smaller model)

**Function timeout errors?**
- Large images take longer to process
- Consider upgrading to Vercel Pro
- Or use a different hosting platform

**File upload not working?**
- Ensure your images are under 4.5 MB
- Vercel has payload size limits
