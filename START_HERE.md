# 🛡️ AegisX - START HERE (2 Minutes)

## 🚀 To Run It (3 terminals)

**Terminal 1 - Backend:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm install
npm run dev
```

**Terminal 3 - Open Browser:**
```
http://localhost:5173
```

✅ **Done! Watch incidents appear automatically.**

---

## 🎬 To Test It

```bash
python test_scenarios.py
# Choose option 1 for REALISTIC ATTACK SEQUENCE (best for demo)
```

---

## 📖 To Learn It

Read these in order:
1. **QUICKSTART_DEMO.md** - 5-minute presentation guide
2. **AEGISX_USER_GUIDE.md** - Complete reference guide
3. **TESTING_AND_GUIDE_README.md** - Overview of all docs

---

## 📊 What You'll See

- **Left:** Incident feed (red = critical, orange = high, yellow = medium, blue = low)
- **Center:** AI analysis of selected incident
- **Right:** Aegis mascot + system metrics
- **Header:** Green dot = connected to backend ✅

---

## 🎯 Quick Demo (5 mins for Judge)

1. Show dashboard layout
2. Run: `python test_scenarios.py` → select option 1
3. Point out incidents appearing in real-time
4. Click an incident
5. Click "Block IP" action
6. Show mascot state changing
7. Explain color-coded severity

---

## 🆘 Troubleshooting

| Problem | Fix |
|---------|-----|
| No incidents | Backend not running: check Terminal 1 |
| Disconnected | Refresh browser (Ctrl+R) or restart backend |
| Frontend won't load | Run `npm install` in frontend folder |
| Test script fails | Make sure backend is running on 8000 |

---

## 📁 Key Files

```
aegis/
├── QUICKSTART_DEMO.md          ← Read this before presenting
├── AEGISX_USER_GUIDE.md        ← Full documentation
├── TESTING_AND_GUIDE_README.md ← Overview of all resources
├── test_scenarios.py           ← Generate test incidents
├── create_pdf.py               ← Create PDF guide
├── backend/                    ← FastAPI backend
├── frontend/                   ← React frontend
└── terminal/                   ← Terminal UI (optional)
```

---

## ✨ What's Special About AegisX

✅ Real-time incident streaming (WebSocket)  
✅ AI analyzes each incident automatically  
✅ Can execute remediation actions  
✅ Beautiful mascot with 9 emotional states  
✅ Works on web, desktop, and terminal  
✅ Production-ready architecture  

---

## 📝 Create PDF Guide

```bash
python create_pdf.py
# Creates: AEGISX_GUIDE.pdf
```

Then share PDF with judges! 📧

---

## 🎓 Architecture

```
Frontend (React) ←→ Backend (FastAPI) ← Generates Incidents
    ↓
  WebSocket
    ↑
Shows in real-time
```

---

**Ready to impress at your hackathon? 🎉**

Next: Read **QUICKSTART_DEMO.md** for the full demo flow.
