# AegisX - Quickstart Demo Guide (5 min)

Perfect for showing judges at a hackathon! Follow these steps exactly.

---

## ⏱️ Total Time: 5-7 minutes

---

## 🎯 Step 1: Pre-Demo Setup (1-2 mins before showing judges)

### Terminal A: Backend
```bash
cd backend
venv\Scripts\activate
python -m uvicorn app.main:app --reload --port 8000
```

Wait for: `Uvicorn running on http://127.0.0.1:8000`

### Terminal B: Frontend
```bash
cd frontend
npm run dev
```

Wait for: `Local: http://localhost:5173`

### Terminal C: Prepare Test Script
```bash
cd aegis
# Leave ready to run: python test_scenarios.py
```

---

## 👀 Step 2: Demo the Dashboard (1-2 mins)

1. **Open browser:** `http://localhost:5173`

2. **Point out key elements:**
   
   ```
   "Here's AegisX - an AI incident analyst. The green dot means 
   we're connected to the backend. Watch the incident feed on 
   the left as new security incidents stream in real-time."
   ```

3. **Show connection status:**
   ```
   "See this green indicator? That means our WebSocket connection 
   is live. Incidents will appear here instantly."
   ```

---

## 🎬 Step 3: Generate Test Incidents (1-2 mins)

### Run the test simulator:
```bash
python test_scenarios.py
```

**Select option: `1`** (Realistic Attack Sequence)

This will simulate a phased attack:
1. 🔍 Reconnaissance
2. ⚔️  Brute force
3. 💥 Service crash
etc.

**Point out to judges:**
```
"Watch the incident feed - new incidents appear in real-time as 
they're detected. Each one has different severity levels shown 
by the color coding."
```

---

## 🔴 Step 4: Show Incident Details (1-2 mins)

1. **Click on a HIGH or CRITICAL incident** in the feed

2. **Point to the Analysis Panel:**
   ```
   "When you click an incident, our AI instantly analyzes it. 
   It tells you:
   - What happened
   - Why it happened
   - Which service is affected
   - What action to take
   - How confident the AI is"
   ```

3. **Show the mascot:**
   ```
   "This is Aegis, our AI assistant. You can see it transitions 
   between emotional states - alert when new incidents come in, 
   analyzing when we're running AI checks, and satisfied when 
   everything's healthy."
   ```

---

## ⚡ Step 5: Execute an Action (1-2 mins)

1. **Click one of the action buttons** (Block IP, Restart Service, etc.)

2. **Show the execution:**
   ```
   "The system executes the action immediately. You'll see:
   - Mascot changes to 'Action Running' state
   - Action button shows loading
   - Confirmation appears when complete"
   ```

3. **Point out the metrics:**
   ```
   "In the bottom right, we track CPU, memory, and network 
   metrics in real-time. So you can see the impact of your actions 
   immediately."
   ```

---

## 📊 Step 6: Show Metrics & Performance (30 secs)

```
"The metrics panel shows real-time system health. In this 
dashboard we're tracking:
- CPU utilization
- Memory usage
- Network I/O
- Disk operations

All updating every second."
```

---

## 💾 Step 7: Show Incident History (30 secs)

**Scroll through the incident feed:**

```
"All incidents are logged here. You can see:
- Incident type
- Severity level (color-coded)
- Timestamp
- Brief description
- Whether it's resolved

Click any past incident to review the analysis or take action."
```

---

## 🔧 Bonus: Show Terminal Alternative (Optional, 1 min)

If judges ask about alternative interfaces:

```bash
cd terminal
python app.py
```

```
"We also built a Terminal UI version using Python and Textual. 
This gives you TUI access on the command line without needing 
a web browser."
```

---

## 📱 Bonus: Desktop Assistant (Optional, 1 min)

```bash
cd electron
npm run dev
```

```
"We also have an Electron desktop app with a floating 
assistant that sits in your corner. Great for monitoring 
while you're working on other things."
```

---

## 🎓 Key Talking Points

When judges ask questions, emphasize these:

### **"How does it detect incidents?"**
```
"Incidents can come from any monitoring system - Prometheus, 
Datadog, Splunk, etc. In this demo we're simulating realistic 
security and observability incidents. In production, these would 
come from your actual infrastructure."
```

### **"How does the AI work?"**
```
"Each incident is analyzed by an AI model that:
1. Understands the incident type
2. Infers the root cause
3. Assesses severity
4. Recommends an action
5. Routes to the right team

This all happens instantly."
```

### **"Can it take action automatically?"**
```
"Yes. We can set policies like:
- Auto-block IPs after 3 failed login attempts
- Auto-restart services when they crash
- Auto-scale when CPU exceeds 90%

For critical incidents, it can auto-execute with audit logging."
```

### **"What about false positives?"**
```
"Good question. The AI assigns confidence scores (0-100%). 
Operators can ignore low-confidence incidents. Over time, the 
system learns to reduce false positives."
```

### **"How does it scale?"**
```
"The WebSocket connection can handle thousands of concurrent 
incidents. The architecture uses async/await, so it's very efficient. 
We could scale to millions of incidents per second with 
load balancing and caching."
```

---

## ❌ Troubleshooting During Demo

### **No incidents appearing**
```bash
# In Terminal C, manually trigger:
python test_scenarios.py
# Pick option 2 (Bulk generation)
```

### **Dashboard says "Disconnected"**
```
1. Check backend terminal - if it crashed, restart it
2. Refresh browser (Ctrl+R)
3. Wait 5 seconds and refresh again
```

### **Frontend won't load**
```bash
# Restart frontend
cd frontend
npm run dev
```

### **Mascot not animating**
```
"Don't worry, that's okay. The key part is the incident 
analysis and response - the mascot is just visual feedback."
```

---

## 📋 Demo Checklist

Before showing judges, verify:

- [ ] Backend running and healthy
- [ ] Frontend loaded at http://localhost:5173
- [ ] Connection status shows green
- [ ] Can trigger incidents via test script
- [ ] Can click incident and see analysis
- [ ] Can execute an action
- [ ] Metrics display is working

---

## ⏰ If Short on Time (3-min version)

1. **Quick setup** (30 secs)
   - Show running services
   - Point out 3 main components

2. **Generate incidents** (30 secs)
   - Run test scenario
   - Point to incidents appearing

3. **Show analysis** (1 min)
   - Click incident
   - Show AI explained what happened
   - Click action button

4. **Wrap up** (1 min)
   - Mention other features
   - Answer questions

---

## 🚀 If You Have Extra Time (10-min version)

1. Normal demo (5 mins)
2. Show code architecture
3. Explain async/await design
4. Show metrics collection
5. Demonstrate stress test
6. Show terminal UI
7. Discuss scaling strategy

---

## 🎤 Closing Statement

```
"AegisX is an AI incident response platform that helps 
security teams respond faster to threats. It's built for 
real-time incident management with:

✅ Live incident streaming
✅ AI-powered analysis
✅ Instant remediation actions
✅ Beautiful visual interface
✅ Multiple deployment options (web, desktop, terminal)

Best for security teams who need to respond to hundreds 
of incidents daily."
```

---

## 📞 Question Prep

**"What technologies do you use?"**
```
Backend: FastAPI, Python, async/await, WebSocket
Frontend: React, TypeScript, Vite
Terminal: Python Textual
Desktop: Electron
AI: Claude or similar LLM
```

**"How is this different from existing tools?"**
```
Most tools show you incidents. Ours:
1. Analyzes each one automatically
2. Recommends actions
3. Can execute them
4. Tracks emotional state (novel!)
5. Works across web, desktop, and terminal
```

**"What's the business model?"**
```
Could be:
- SaaS subscription per incident volume
- Enterprise licensing
- Open source + premium support
```

---

Good luck with your presentation! 🎉
