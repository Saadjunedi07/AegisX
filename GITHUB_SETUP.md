# 🚀 GitHub Setup for AegisX Deployment

Quick walkthrough to prepare your project for Railway/Render deployment.

## Prerequisites

- [Git](https://git-scm.com/download) installed
- [GitHub account](https://github.com/signup)
- SSH key configured (or use HTTPS)

## Step-by-Step Setup

### 1. Initialize Local Git Repository

```bash
cd c:\Users\adity\Downloads\aegis
git init
```

### 2. Configure Git User (First Time Only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 3. Stage and Commit Changes

```bash
# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: AegisX ready for deployment"
```

### 4. Create GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click **+** → **New repository**
3. Name: `aegis`
4. Description: `Autonomous AI Incident Analyst`
5. Choose **Public** (for Railway/Render to access) or **Private** + create access token
6. Click **Create repository**

### 5. Connect Local Repo to GitHub

Replace `YOUR_USERNAME` with your GitHub username:

```bash
# Using HTTPS (easier)
git remote add origin https://github.com/YOUR_USERNAME/aegis.git
git branch -M main
git push -u origin main
```

**OR** (using SSH if configured):

```bash
git remote add origin git@github.com:YOUR_USERNAME/aegis.git
git branch -M main
git push -u origin main
```

### 6. Verify Connection

```bash
git remote -v
```

Should output:
```
origin  https://github.com/YOUR_USERNAME/aegis.git (fetch)
origin  https://github.com/YOUR_USERNAME/aegis.git (push)
```

## File Structure Checklist

Before pushing, ensure these files exist:

- ✅ `Dockerfile` - Container image definition
- ✅ `.dockerignore` - Files to exclude from Docker build
- ✅ `docker-compose.yml` - Local development setup
- ✅ `.gitignore` - Files to exclude from git
- ✅ `.env.example` - Environment variables template
- ✅ `backend/requirements.txt` - Python dependencies
- ✅ `backend/app/main.py` - FastAPI entry point

## Example Workflow

```bash
# After making changes locally
git add .
git commit -m "Add new feature or fix"
git push origin main

# The changes are now on GitHub
# Railway/Render can pull and auto-deploy
```

## For Private Repository

If you want to use a private repo:

1. Create repository as **Private** on GitHub
2. Go to Settings → Developer settings → **Personal access tokens**
3. Create a new token with `repo` scope
4. On Railway/Render, add GitHub token when connecting repo

## Troubleshooting

### "Permission denied (publickey)"
- Use HTTPS instead: `https://github.com/YOUR_USERNAME/aegis.git`
- Or [configure SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

### "fatal: not a git repository"
- Run `git init` in the project root directory

### "Nothing to commit"
- Ensure files are modified and staged with `git add .`

### "Couldn't read from remote repository"
- Check internet connection
- Verify GitHub username and repo name spelling

## Next Steps

1. ✅ Push code to GitHub
2. 📖 Read [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)
3. 🚀 Connect repo to Railway or Render
4. 📊 Deploy and monitor

---

**Quick Deploy Links:**
- [Railway.app](https://railway.app)
- [Render.com](https://render.com)
