# 🚀 AegisX Deployment Guide

Deploy AegisX to **Railway** or **Render** with Docker support.

## Quick Start

### Step 1: Push Code to GitHub

```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit: AegisX ready for deployment"

# Add remote and push
git remote add origin https://github.com/YOUR_USERNAME/aegis.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy to Railway

1. **Go to [Railway.app](https://railway.app)**
2. **Click "New Project" → "Deploy from GitHub repo"**
3. **Select your `aegis` repository**
4. Railway automatically:
   - Detects the Dockerfile
   - Builds the Docker image
   - Deploys the container
5. **Set Environment Variables:**
   - Go to Settings → Variables
   - Add any required `.env` variables (e.g., API keys, database URLs)
6. **Get your endpoint** - Railway provides a public URL automatically

### Step 3: Deploy to Render

1. **Go to [Render.com](https://render.com)**
2. **Click "New +" → "Web Service"**
3. **Select "Deploy an existing Docker repository"**
4. **Connect your GitHub account and select `aegis` repo**
5. **Configure:**
   - Name: `aegis-backend`
   - Environment: `Docker`
   - Plan: Free or Paid
6. **Set Environment Variables:**
   - Add in Environment section
7. **Click "Create Web Service"** - Render auto-builds and deploys

## Docker Build Locally

### Build Image

```bash
docker build -t aegis-backend .
```

### Run Container

```bash
docker run -p 8000:8000 \
  -e PORT=8000 \
  aegis-backend
```

Access at `http://localhost:8000`

## Docker Compose (Development)

```bash
# Build and start services
docker-compose up -d

# View logs
docker-compose logs -f backend

# Stop services
docker-compose down
```

## Project Structure

- **Dockerfile**: Multi-stage build for optimized image
- **.dockerignore**: Excludes unnecessary files
- **docker-compose.yml**: Local development stack
- **backend/**: FastAPI server (main deployable)
- **frontend/**: React app (can be built separately)
- **terminal/**: TUI app (optional for deployment)

## Deployment Checklist

- ✅ Code pushed to GitHub
- ✅ `.env` and secrets NOT committed
- ✅ Dockerfile present in root
- ✅ Environment variables configured on platform
- ✅ Port 8000 exposed and accessible
- ✅ Health check passes

## Environment Variables

Add these on Railway/Render:

```
PYTHONUNBUFFERED=1
LOG_LEVEL=info
PORT=8000
# Add your custom variables here
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Build fails | Check Dockerfile syntax and ensure requirements.txt is valid |
| Port not accessible | Railway/Render auto-assigns port; check deployment logs |
| Dependencies missing | Add to `backend/requirements.txt` and rebuild |
| Environment variables not working | Use uppercase names and set via platform UI |

## Monitoring & Logs

**Railway**: Dashboard → Deployments → View Logs
**Render**: Services → Logs tab

## Scale Up

Both platforms support:
- Auto-scaling
- Custom domains
- SSL/TLS (automatic)
- Monitoring dashboards
- Rollback to previous deployments

## Cost Comparison

| Platform | Free Tier | Pro Tier |
|----------|-----------|----------|
| Railway | $5/month credit | Pay as you go (~$0.05/hr) |
| Render | Limited | Pay as you go (~$0.05/hr) |

---

**Next Steps:**
1. Create `.gitignore` for local files
2. Set up GitHub repository
3. Connect to Railway or Render
4. Monitor first deployment
5. Configure custom domain (optional)
