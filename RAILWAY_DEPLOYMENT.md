# Deploy to Railway

## Quick Deployment (5 minutes)

### 1. Create Railway Account
Go to [railway.app](https://railway.app) and sign up with GitHub

### 2. Deploy from GitHub

**Option A: Via Railway Dashboard**
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose your `Image-Bg-remover` repository
4. Railway auto-detects Python and deploys automatically
5. Done! You'll get a public URL

**Option B: Via Railway CLI**
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Initialize and deploy
cd /Users/shaharabi/Documents/MyCode/background-removal-app-python-yt-short-main
railway init
railway up
```

### 3. Configure (Optional)

Railway will automatically:
- ✅ Detect Python from `requirements.txt`
- ✅ Install dependencies
- ✅ Run `app.py`
- ✅ Assign a public URL

**To use a specific model:**
1. Go to your project settings
2. Add environment variable:
   - `REMBG_MODEL` = `u2netp` (fast) or `u2net` (quality)
   - `PORT` = `5000` (or any port)

### 4. Access Your App

Railway will provide a URL like:
```
https://your-app.railway.app
```

## Why Railway?

✅ **No size limits** - AI models work fine  
✅ **Always-on containers** - No cold starts  
✅ **Persistent storage** - Files stay between requests  
✅ **Free tier** - $5 credit/month, enough for testing  
✅ **Auto-deploy** - Push to GitHub → Auto redeploys  

## Troubleshooting

**Build fails?**
- Check Railway build logs
- Ensure `requirements.txt` is correct

**App won't start?**
- Railway needs to know the start command
- It should auto-detect `python app.py`
- If not, set start command: `python app.py` in Railway settings

**Port issues?**
- Railway assigns `PORT` env var automatically
- Your app already reads `os.getenv('PORT', '5000')`
