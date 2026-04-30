# 🛡️ AegisX - Complete Demo & Testing Guide

Welcome! This directory contains everything you need to understand and demonstrate **AegisX** - an AI-powered incident response system.

---

## 📁 What's Included

### 📖 Documentation Files

| File | Purpose | Audience |
|------|---------|----------|
| **AEGISX_USER_GUIDE.md** | Comprehensive user manual | Anyone using the system |
| **QUICKSTART_DEMO.md** | 5-minute demo guide | Hackathon judges & presenters |
| **AEGISX_GUIDE.html** | Beautiful HTML reference | Browser viewing |
| **AEGISX_GUIDE.pdf** | Professional PDF version | Easy sharing & printing |

### 🧪 Testing & Simulation

| File | Purpose | Usage |
|------|---------|-------|
| **test_scenarios.py** | Incident generator | `python test_scenarios.py` |
| **generate_pdf_guide.py** | Creates PDF from HTML | `python generate_pdf_guide.py` |

---

## 🚀 Quick Start (Choose Your Path)

### Path 1: I Want to See It Running (5 mins)

```bash
# Terminal 1: Start Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# Terminal 2: Start Frontend
cd frontend
npm install
npm run dev

# Open: http://localhost:5173
# Incidents auto-generate every 5-15 seconds!
```

### Path 2: I Want to Demo It (7 mins)

Follow **QUICKSTART_DEMO.md** step-by-step for a complete presentation

### Path 3: I Want to Learn It (20 mins)

Read through **AEGISX_USER_GUIDE.md** for complete feature documentation

### Path 4: I Want to Test It (custom)

Run incident scenarios:
```bash
python test_scenarios.py
```
Choose from 4 test options (attack sequence, bulk load, all types, stress test)

---

## 📊 Dashboard Overview

The **Command Center** has 5 main areas:

```
┌─────────────────────────────────────────────┐
│ 🛡️ AegisX    Status: ● (Connected)         │
├────────┬──────────────────┬─────────────────┤
│        │                  │                 │
│Incident│  Analysis Panel  │  Aegis Mascot   │
│ Feed   │  + Chat          │  + Metrics      │
│        │  + Actions       │  (9 states)     │
│        │                  │                 │
└────────┴──────────────────┴─────────────────┘
```

**Key Features:**
- ✅ Live WebSocket incident streaming
- ✅ AI-powered analysis per incident
- ✅ Executable remediation actions
- ✅ Real-time system metrics
- ✅ Animated Aegis mascot companion

---

## 🎬 Testing Scenarios

### Auto-Generated Incidents (Easiest)
Just start the backend and frontend. Realistic incidents appear automatically.

### Option 1: Realistic Attack Sequence (BEST for DEMO)
```bash
python test_scenarios.py
# Select: 1
```
Simulates phased attack:
1. 🔍 Reconnaissance
2. ⚔️ Brute force
3. 💥 Service crash
etc.

### Option 2: Bulk Generation
```bash
python test_scenarios.py
# Select: 2
```
Generates 20 random incidents rapidly

### Option 3: All Incident Types
```bash
python test_scenarios.py
# Select: 3
```
Creates one of each type to test all features

### Option 4: Stress Test
```bash
python test_scenarios.py
# Select: 4
```
Generates 50+ incidents to test performance

### Manual API Call
```bash
curl -X POST http://localhost:8000/api/incidents/simulate \
  -H "Content-Type: application/json" \
  -d '{
    "type": "brute_force",
    "severity": "critical",
    "source_ip": "192.168.1.100",
    "affected_service": "auth-api",
    "description": "1000 failed login attempts"
  }'
```

---

## 📋 Incident Types

| Type | Severity | Services | Example |
|------|----------|----------|---------|
| 🔐 **BRUTE_FORCE** | MEDIUM-CRITICAL | auth-api, admin-portal, ssh-gateway | Login attack attempts |
| ⚠️ **API_500** | MEDIUM-CRITICAL | payment-api, user-service, order-service | Server crashes & errors |
| 📈 **CPU_OVERLOAD** | MEDIUM-CRITICAL | ml-pipeline, data-processor, web-server | High CPU usage |
| 🌐 **SUSPICIOUS_TRAFFIC** | LOW-CRITICAL | edge-proxy, load-balancer, firewall | Network anomalies |
| 💥 **SERVICE_CRASH** | HIGH-CRITICAL | postgres-primary, redis-cluster, kafka-broker | Process termination |

---

## 🎯 For Your Hackathon Judge

### Before Demo (15 mins)
- [ ] Backend running on port 8000
- [ ] Frontend loaded at http://localhost:5173
- [ ] Status shows green (connected)
- [ ] Test script ready
- [ ] Browser cache cleared

### During Demo (5-7 mins)
- [ ] Show dashboard layout
- [ ] Run test_scenarios.py option 1
- [ ] Click incident → show AI analysis
- [ ] Execute action
- [ ] Point out color-coded severity
- [ ] Show mascot state changes
- [ ] Explain real-time metrics

### Key Talking Points
1. **Real-time Streaming** - WebSocket for instant updates
2. **AI Analysis** - Auto root cause detection
3. **Autonomous Response** - Can execute actions automatically
4. **Multi-Platform** - Web, terminal, desktop
5. **Scalable** - Handles thousands of incidents
6. **Production-Ready** - FastAPI + React + async architecture

---

## 📚 Documentation Files Explained

### AEGISX_USER_GUIDE.md
**80+ paragraphs covering:**
- Quick start (5 min)
- Command Center walkthrough
- Incident feed explained
- Dashboard features
- How to execute actions
- Testing & simulation options
- Troubleshooting guide
- Demo checklist

**Best for:** Learning how to use the system

### QUICKSTART_DEMO.md
**5-minute guide with:**
- Step-by-step demo flow
- Exact talking points
- Troubleshooting during demo
- Bonus features to show
- Common judge questions
- If-short-on-time guide (3-min version)

**Best for:** Presenting to judges

### AEGISX_GUIDE.html
**Professional web version:**
- Beautiful styled HTML
- Tables and formatting
- Color-coded sections
- Easy to view in browser
- Can print to PDF directly

**Best for:** Browsing and printing

### AEGISX_GUIDE.pdf
**Shareable PDF:**
- Professional formatting
- Print-friendly
- Can be emailed
- Looks polished

**How to create:**
```bash
# Option 1: Using Python
pip install weasyprint
python generate_pdf_guide.py

# Option 2: Using browser
# Open AEGISX_GUIDE.html in Chrome/Firefox
# Print (Ctrl+P) → Save as PDF

# Option 3: Online
# Upload HTML to cloudconvert.com
```

---

## 🧪 Test Script Options Explained

### test_scenarios.py Menu

**Option 1: Realistic Attack Sequence** ⭐ RECOMMENDED
- 🔍 Reconnaissance phase
- ⚔️ Brute force phase
- 💥 Service crash phase
- 🔥 Resource exhaustion phase
- Perfect for showing a complete story to judges
- Duration: ~30 seconds

**Option 2: Bulk Generation**
- Rapid-fire 20 random incidents
- Good for load testing
- Shows volume handling
- Duration: ~10 seconds

**Option 3: All Incident Types**
- Exactly 1 of each type
- Verify all types work
- Good for testing
- Duration: ~5 seconds

**Option 4: Stress Test**
- 50+ incidents rapidly
- Performance measurement
- Shows scalability
- Duration: Configurable

---

## 🔧 Troubleshooting

### Nothing Appearing?
```bash
# Verify backend is running
curl http://localhost:8000/api/incidents

# Manually trigger incident
python test_scenarios.py
# Choose option 2
```

### Disconnected Status?
```bash
# Restart backend
cd backend
uvicorn app.main:app --reload

# Refresh browser (Ctrl+R)
```

### Actions Not Working?
```bash
# Check browser console (F12)
# Check backend logs
# Verify backend is running
# Try a different action
```

### Dashboard Slow?
```bash
# Close other browser tabs
# Clear cache (Ctrl+Shift+Delete)
# Restart frontend
cd frontend
npm run dev
```

---

## 🎓 What to Emphasize to Judges

### "This is different because..."
✅ Auto-analyzes each incident with AI
✅ Suggests AND executes remediation
✅ Works across web, terminal, desktop
✅ Beautiful visual feedback (mascot emotions)
✅ Production-grade async architecture
✅ Real-time WebSocket streaming

### "It scales because..."
✅ FastAPI with async/await
✅ Handles thousands of concurrent connections
✅ Incident buffer keeps only recent 100
✅ Efficient publisher-subscriber pattern
✅ Horizontal scaling ready

### "It's unique because..."
✅ Mascot provides emotional feedback
✅ Multi-platform UIs (not just web)
✅ AI explains what's happening
✅ Can auto-execute with confidence scoring
✅ Beautiful, engaging UI

---

## 📞 Quick Reference

| Task | Command | Time |
|------|---------|------|
| Start backend | `uvicorn app.main:app --reload` | 5s |
| Start frontend | `npm run dev` | 10s |
| Generate incidents | `python test_scenarios.py` | 30-60s |
| Open dashboard | Visit http://localhost:5173 | instant |
| View API docs | Visit http://localhost:8000/docs | instant |
| Read guide | Open AEGISX_USER_GUIDE.md | 20 min |
| Do full demo | Follow QUICKSTART_DEMO.md | 5-7 min |

---

## 🎉 You're Ready!

Everything you need is here:
- ✅ Documentation
- ✅ Testing tools
- ✅ Demo guide
- ✅ HTML & PDF guides

**Next Steps:**
1. Start the backend and frontend
2. Run test_scenarios.py option 1
3. Follow QUICKSTART_DEMO.md when presenting
4. If judges ask detailed questions, reference AEGISX_USER_GUIDE.md

---

## 📧 Need Help?

- **Dashboard won't load?** Check backend running on 8000
- **No incidents?** Run test_scenarios.py to trigger manually
- **Questions about features?** Check AEGISX_USER_GUIDE.md
- **Demo flow unclear?** Read QUICKSTART_DEMO.md
- **Performance issues?** See Troubleshooting section above

---

**Good luck with your presentation! 🎉🛡️**

*Made for hackathon judges with ❤️*
