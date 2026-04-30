# AegisX - User Guide & Quickstart

**Autonomous AI Incident Analyst & Auto-Response Agent**

Welcome to AegisX! This guide will help you get up and running with the Command Center, Incident Feed, and all key features.

---

## 📋 Table of Contents
1. [Quick Start](#quick-start)
2. [Command Center Overview](#command-center-overview)
3. [Incident Feed](#incident-feed)
4. [Dashboard Features](#dashboard-features)
5. [Taking Actions](#taking-actions)
6. [Testing & Simulation](#testing--simulation)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- Git

### Step 1: Clone & Setup Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
# OR
source venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
✅ Backend runs on: `http://localhost:8000`

### Step 2: Start Frontend (Command Center)
```bash
cd frontend
npm install
npm run dev
```
✅ Frontend runs on: `http://localhost:5173`

### Step 3: Start Terminal UI (Optional)
```bash
cd terminal
pip install -r requirements.txt
python app.py
```

### Step 4: Start Desktop App (Optional)
```bash
cd electron
npm install
npm run dev
```

---

## 💪 Command Center Overview

The **Command Center** is your main web interface for monitoring and responding to security incidents in real-time.

### Layout
```
┌─────────────────────────────────────────────────┐
│  🛡️ AegisX    Status: ● Connected              │  ← Header
├────────┬──────────────────────┬─────────────────┤
│        │                      │                 │
│ Incident  │  Analysis Pane     │   Mascot        │
│ Feed   │  + Chat Panel       │ (Aegis AI)      │
│        │                      │   + Metrics     │
│        │                      │                 │
└────────┴──────────────────────┴─────────────────┘
```

### Key Components:

#### 1. **Status Indicator** (Top-Right)
   - 🟢 **Green** = Connected to backend
   - 🔴 **Red** = Disconnected
   - 📡 Shows real-time WebSocket connection

#### 2. **Incident Feed** (Left Panel)
   - Displays incidents in reverse chronological order (newest first)
   - **Color-coded by severity:**
     - 🔵 Blue = LOW
     - 🟡 Yellow = MEDIUM
     - 🟠 Orange = HIGH
     - 🔴 Red = CRITICAL
   - Click an incident to view details & AI analysis

#### 3. **Analysis Pane** (Center)
   - **What Happened** - Description of the incident
   - **Why** - Root cause analysis
   - **Affected Service** - Which system was impacted
   - **Suggested Action** - AI-recommended response
   - **Confidence** - AI analysis confidence level (0-100%)

#### 4. **Aegis Mascot** (Right Panel)
   - 🤖 Animated companion with 9 emotional states
   - **States:**
     - 😌 Idle - All good
     - 🚨 Alert - New incident detected
     - 🤔 Analyzing - Running AI analysis
     - ⚡ Action Running - Executing remediation
     - ✅ Success - Action completed successfully
     - ❌ Failed - Action failed
     - 🔥 Critical - CRITICAL severity incident
     - 😈 Attacking - Under attack
     - 😴 Satisfied - Systems healthy

#### 5. **Metrics Panel** (Bottom Right)
   - **CPU %** - System CPU utilization
   - **Memory %** - RAM usage
   - **Network** - Data in/out
   - **Disk I/O** - Read/write operations

---

## 🔔 Incident Feed

### What is an Incident?
An incident is any security or observability event that needs attention:
- **Brute-force attacks** - Multiple login failures
- **API errors** - Service crashes or high error rates
- **Resource overload** - CPU, memory, disk exhaustion
- **Suspicious traffic** - Anomalies in network patterns
- **Service crashes** - Unexpected process terminations

### Reading an Incident Card

```
┌─────────────────────────────────────────┐
│ BRUTE_FORCE  [CRITICAL] 14:25:32        │
│                                         │
│ Multiple failed login attempts          │
│ detected from 192.168.1.105             │
│ — 342 attempts in 5m                    │
│                                         │
│ Service: auth-api                       │
│ [Not Resolved]  [Select] [Copy]        │
└─────────────────────────────────────────┘
```

### Incident Types

| Type | Severity Range | Icon | Description |
|------|---|---|---|
| **BRUTE_FORCE** | MEDIUM-CRITICAL | 🔐 | Login attack attempts |
| **API_500** | MEDIUM-CRITICAL | ⚠️ | Server errors & crashes |
| **CPU_OVERLOAD** | MEDIUM-CRITICAL | 📈 | High CPU utilization |
| **SUSPICIOUS_TRAFFIC** | LOW-CRITICAL | 🌐 | Network anomalies |
| **SERVICE_CRASH** | HIGH-CRITICAL | 💥 | Process termination |

---

## 📊 Dashboard Features

### Feature 1: Live WebSocket Connection
- Real-time incident streaming
- Auto-refresh without page reload
- Connection status indicator

### Feature 2: AI Analysis
- **One-click analysis** - Click an incident to trigger AI analysis
- **Root cause detection** - Understands why incident occurred
- **Action recommendations** - Suggests fixes
- **Smart routing** - Assigns to correct team

### Feature 3: Action Center
- Block an IP address
- Restart affected service
- Scan for vulnerabilities
- Kill malicious process
- Rollback deployment

### Feature 4: Real-time Metrics
- CPU, Memory, Disk monitoring
- Network I/O tracking
- Performance graphs
- Alert thresholds

---

## ⚡ Taking Actions

### How to Execute an Action

1. **Select an Incident**
   - Click on an incident card in the feed
   
2. **Read the AI Analysis**
   - Review what happened and why
   - Check "Suggested Action"
   
3. **Click an Action Button**
   - "Block IP" - Blocks the attacker's IP
   - "Restart Service" - Restarts the affected service
   - "Scan Service" - Runs security scan
   - "Kill Process" - Terminates malicious process
   - "Auto-Remediate" - Executes recommended action
   
4. **Confirm & Execute**
   - System executes the action
   - Mascot shows "Action Running" state
   - Receive confirmation when complete

### Sample Incident Response

```
Incident: BRUTE_FORCE from 192.168.1.105
↓
AI Analysis: "Attacker trying 342 passwords on auth-api"
↓
Suggested Action: "Block 192.168.1.105 + enable MFA"
↓
You click: "Block IP"
↓
Status: ✅ Action Complete - IP 192.168.1.105 blocked
```

---

## 🧪 Testing & Simulation

### Option 1: Auto-Generated Incidents (Fastest)
The backend automatically generates realistic incidents every 5-15 seconds.

**Just start the backend & frontend, incidents appear!**

### Option 2: Manual API Trigger

Create an incident via API:

```bash
curl -X POST http://localhost:8000/api/incidents/trigger \
  -H "Content-Type: application/json" \
  -d '{
    "type": "brute_force",
    "severity": "critical",
    "source_ip": "192.168.1.100",
    "affected_service": "auth-api",
    "description": "10000 failed login attempts detected"
  }'
```

### Option 3: Bulk Test Script

Run the provided test simulator:

```bash
python test_scenarios.py
```

This will:
- Generate 20 realistic incidents
- Simulate attack patterns
- Test all incident types
- Vary severity levels
- Create a realistic incident timeline

### Option 4: Chaos Testing

For aggressive testing (recommended for demos):

```bash
python chaos_test.py --incidents 50 --interval 1 --severity critical
```

---

## 📱 Terminal UI (Alternative View)

If using the Terminal UI instead of web interface:

```
(Start with: cd terminal && python app.py)

┌──────────────────────────────────────┐
│ 🛡️  AegisX Terminal                  │
├──────────────────────────────────────┤
│                                      │
│  [Incident Feed]    [Metrics]        │
│  - CRITICAL: Brute-force 14:25      │
│  - HIGH: API 500                    │ CPU: 87%
│  - MEDIUM: CPU Overload             │ MEM: 72%
│                                      │ NET: 15.2 Mbps
│  [Analysis Panel]                    │
│  What: 342 login attempts            │
│  Why: Dictionary attack              │
│  Action: Block 192.168.1.105         │
│                                      │
│  [Command Input] ► /block 192...     │
│                                      │
└──────────────────────────────────────┘
```

---

## 🖥️ Desktop Floating Assistant

Click the Aegis mascot in the corner for a floating assistant:
- View current incident
- Quick actions
- Metric glance
- Emotional state transitions

---

## ❓ Troubleshooting

### Connection Issues

**Issue:** Frontend says "Disconnected"
```
Solution:
1. Verify backend is running: curl http://localhost:8000/api/incidents
2. Check if backend port 8000 is available
3. Firewall issue? Check Windows Defender
```

**Issue:** No incidents appearing
```
Solution:
1. Manually trigger: curl -X POST http://localhost:8000/api/incidents/simulate
2. Check browser console (F12) for WebSocket errors
3. Ensure mock incident generator is enabled
```

### Performance Issues

**Issue:** Dashboard is slow
```
Solution:
1. Reduce incident limit: Edit frontend to show 10 incidents vs 50
2. Disable metrics polling temporarily
3. Close other tabs
4. Clear browser cache (Ctrl+Shift+Delete)
```

---

## 🎯 Demo Checklist for Hackathon Judge

Use this checklist when demonstrating to your judge:

- [ ] **Backend Started** - Show terminal running `uvicorn`
- [ ] **Frontend Loaded** - Show `http://localhost:5173` 
- [ ] **Status Connected** - Show green dot in header
- [ ] **Incident Feed** - Show live incidents streaming in
- [ ] **Select Incident** - Click one and show AI analysis
- [ ] **Trigger Action** - Click "Block IP" and show success
- [ ] **Mascot Emotions** - Show state changes (alert → analyzing → success)
- [ ] **Metrics Update** - Show real-time CPU/Memory changes
- [ ] **Multiple Incidents** - Scroll through incident history
- [ ] **Severity Levels** - Point out color-coding scheme
- [ ] **WebSocket Speed** - Show how fast new incidents appear
- [ ] **Terminal UI** - Optional: Show alternative interface
- [ ] **Desktop App** - Optional: Show floating assistant

---

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review console logs (F12 in browser)
3. Check backend logs for API errors
4. Verify all services are running

---

## 🎓 Key Concepts to Explain

When presenting to judges, emphasize:

1. **Real-time Streaming** - WebSocket for instant incident notification
2. **AI-Powered Analysis** - Each incident gets automatic root cause analysis
3. **Multi-Platform** - Works on web, terminal, and desktop
4. **Autonomous Response** - AI suggests and can auto-execute remediation
5. **Mascot Feedback** - Emotional AI provides visual feedback
6. **Production-Ready** - FastAPI backend, React frontend, async WebSocket
7. **Scalable** - Can handle thousands of simultaneous incidents

---

## 🚀 Pro Tips

- **Keyboard Shortcuts:** (Coming in v2)
- **Custom Incident Types:** Edit `backend/app/models/incident.py`
- **AI Analyzer Tuning:** Modify prompts in `backend/app/services/ai_analyzer.py`
- **Mascot Customization:** Add emotions in `frontend/src/state/aegisEmotion.ts`
- **Metrics Sources:** Add integrations in `backend/app/services/metrics_collector.py`

---

**Happy Securing! 🛡️**
