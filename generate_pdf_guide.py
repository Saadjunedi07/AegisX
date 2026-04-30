"""
HTML-to-PDF Guide Generator for AegisX
Run this to generate a professional PDF guide
"""

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AegisX - Command Center User Guide</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: white;
        }
        
        .cover-page {
            page-break-after: always;
            background: linear-gradient(135deg, #4ade80, #3b82f6);
            color: white;
            padding: 60px;
            text-align: center;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        
        .cover-page h1 {
            font-size: 56px;
            margin-bottom: 20px;
            font-weight: 800;
        }
        
        .cover-page p {
            font-size: 20px;
            margin-bottom: 10px;
            opacity: 0.9;
        }
        
        .cover-page .subtitle {
            font-size: 24px;
            margin-top: 30px;
        }
        
        section {
            page-break-inside: avoid;
            padding: 40px;
            margin-bottom: 20px;
        }
        
        h1 {
            color: #4ade80;
            font-size: 32px;
            margin-bottom: 20px;
            border-bottom: 3px solid #4ade80;
            padding-bottom: 10px;
        }
        
        h2 {
            color: #3b82f6;
            font-size: 24px;
            margin-top: 30px;
            margin-bottom: 15px;
        }
        
        h3 {
            color: #1e40af;
            font-size: 18px;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        
        p {
            margin-bottom: 15px;
            font-size: 14px;
        }
        
        ul, ol {
            margin-left: 30px;
            margin-bottom: 15px;
        }
        
        li {
            margin-bottom: 10px;
        }
        
        code {
            background: #f5f5f5;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 13px;
        }
        
        .code-block {
            background: #1e293b;
            color: #e2e8f0;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 15px 0;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            page-break-inside: avoid;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        
        th {
            background: #4ade80;
            color: white;
            font-weight: 600;
        }
        
        tr:nth-child(even) {
            background: #f9fafb;
        }
        
        .highlight {
            background: #fef3c7;
            padding: 15px;
            border-left: 4px solid #f59e0b;
            margin: 15px 0;
        }
        
        .success {
            background: #dcfce7;
            padding: 15px;
            border-left: 4px solid #22c55e;
            margin: 15px 0;
        }
        
        .warning {
            background: #fed7aa;
            padding: 15px;
            border-left: 4px solid #f97316;
            margin: 15px 0;
        }
        
        .info {
            background: #e0f2fe;
            padding: 15px;
            border-left: 4px solid #0ea5e9;
            margin: 15px 0;
        }
        
        .toc {
            background: #f3f4f6;
            padding: 25px;
            border-radius: 5px;
            margin: 20px 0;
        }
        
        .toc ul {
            list-style: none;
            margin-left: 0;
        }
        
        .toc > ul > li {
            margin-bottom: 8px;
        }
        
        .toc a {
            color: #3b82f6;
            text-decoration: none;
        }
        
        .feature-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin: 20px 0;
        }
        
        .feature-box {
            border: 1px solid #ddd;
            padding: 15px;
            border-radius: 5px;
            background: #f9fafb;
        }
        
        .feature-box h4 {
            color: #3b82f6;
            margin-bottom: 10px;
        }
        
        .kbd {
            border: 1px solid #ccc;
            background: #fff;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: monospace;
            font-size: 12px;
        }
        
        .demo-checklist {
            list-style: none;
            margin: 20px 0;
        }
        
        .demo-checklist li {
            padding: 8px;
            margin-bottom: 5px;
            border-bottom: 1px solid #e5e7eb;
        }
        
        .demo-checklist li:before {
            content: "☐ ";
            color: #3b82f6;
            font-weight: bold;
            margin-right: 8px;
        }
        
        .page-break {
            page-break-after: always;
        }
        
        footer {
            text-align: center;
            color: #999;
            font-size: 12px;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e5e7eb;
        }
        
        .icon {
            font-size: 24px;
            margin-right: 10px;
        }
    </style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover-page">
    <div style="font-size: 80px; margin-bottom: 30px;">🛡️</div>
    <h1>AegisX</h1>
    <p>Autonomous AI Incident Analyst & Auto-Response Agent</p>
    <p class="subtitle">Command Center User Guide</p>
    <p style="margin-top: 50px; font-size: 16px;">Complete Guide to Using AegisX for Real-Time Incident Management</p>
    <p style="margin-top: 40px; font-size: 12px; opacity: 0.8;">Latest Version • Ready for Production</p>
</div>

<!-- TABLE OF CONTENTS -->
<div class="page-break"></div>
<section>
    <h1>📑 Table of Contents</h1>
    <div class="toc">
        <ul>
            <li><a href="#quick-start">Quick Start</a></li>
            <li><a href="#command-center">Command Center Overview</a></li>
            <li><a href="#incident-feed">Understanding the Incident Feed</a></li>
            <li><a href="#dashboard-features">Dashboard Features</a></li>
            <li><a href="#taking-actions">Taking Actions</a></li>
            <li><a href="#testing">Testing & Simulation</a></li>
            <li><a href="#demo-checklist">Demo Checklist</a></li>
            <li><a href="#troubleshooting">Troubleshooting</a></li>
        </ul>
    </div>
</section>

<!-- QUICK START -->
<div class="page-break"></div>
<section id="quick-start">
    <h1>🚀 Quick Start (5 Minutes)</h1>
    
    <h2>Prerequisites</h2>
    <ul>
        <li>Python 3.10 or higher</li>
        <li>Node.js 18 or higher</li>
        <li>Git</li>
    </ul>
    
    <h2>Step 1: Start Backend</h2>
    <div class="code-block">
cd backend
python -m venv venv
venv\\Scripts\\activate    # Windows
# OR
source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
    </div>
    <div class="success">✅ Backend ready at: http://localhost:8000</div>
    
    <h2>Step 2: Start Frontend</h2>
    <div class="code-block">
cd frontend
npm install
npm run dev
    </div>
    <div class="success">✅ Open: http://localhost:5173</div>
    
    <h2>Step 3: Watch Incidents Appear</h2>
    <p>The system automatically generates realistic incidents every 5-15 seconds. Just open the frontend and watch them stream in real-time!</p>
</section>

<!-- COMMAND CENTER OVERVIEW -->
<div class="page-break"></div>
<section id="command-center">
    <h1>💪 Command Center Overview</h1>
    
    <h2>Layout</h2>
    <div class="code-block">
┌──────────────────────────────────────────────────────┐
│ 🛡️ AegisX    Status: ● Connected              │ Header
├────────┬────────────────────┬─────────────────────┤
│        │                    │                     │
│ Incident│  Analysis Panel   │   Aegis Mascot      │
│ Feed   │  + Chat          │   + Metrics         │
│        │                    │                     │
└────────┴────────────────────┴─────────────────────┘
    </div>
    
    <h2>Key Components</h2>
    
    <h3>1️⃣ Status Indicator</h3>
    <table>
        <tr>
            <th>Indicator</th>
            <th>Meaning</th>
        </tr>
        <tr>
            <td>🟢 Green</td>
            <td>Connected to backend, incidents streaming</td>
        </tr>
        <tr>
            <td>🔴 Red</td>
            <td>Disconnected, check backend status</td>
        </tr>
    </table>
    
    <h3>2️⃣ Incident Feed (Left)</h3>
    <p>Shows incidents in reverse chronological order with severity color-coding:</p>
    <ul>
        <li><span style="color: #3b82f6;">🔵 BLUE</span> = LOW severity</li>
        <li><span style="color: #eab308;">🟡 YELLOW</span> = MEDIUM severity</li>
        <li><span style="color: #f97316;">🟠 ORANGE</span> = HIGH severity</li>
        <li><span style="color: #ef4444;">🔴 RED</span> = CRITICAL severity</li>
    </ul>
    
    <h3>3️⃣ Analysis Pane (Center)</h3>
    <p>Click any incident to see AI-powered analysis:</p>
    <ul>
        <li><strong>What Happened</strong> - Clear description</li>
        <li><strong>Why</strong> - Root cause analysis</li>
        <li><strong>Affected Service</strong> - Which system</li>
        <li><strong>Suggested Action</strong> - AI recommendation</li>
        <li><strong>Confidence</strong> - Analysis confidence (0-100%)</li>
    </ul>
    
    <h3>4️⃣ Aegis Mascot (Right)</h3>
    <p>AI companion with 9 emotional states showing system status:</p>
    <table>
        <tr>
            <th>State</th>
            <th>Meaning</th>
        </tr>
        <tr>
            <td>😌 Idle</td>
            <td>All systems normal</td>
        </tr>
        <tr>
            <td>🚨 Alert</td>
            <td>New incident detected</td>
        </tr>
        <tr>
            <td>🤔 Analyzing</td>
            <td>Running AI analysis</td>
        </tr>
        <tr>
            <td>⚡ Action Running</td>
            <td>Executing remediation</td>
        </tr>
        <tr>
            <td>✅ Success</td>
            <td>Action completed</td>
        </tr>
        <tr>
            <td>❌ Failed</td>
            <td>Action failed</td>
        </tr>
        <tr>
            <td>🔥 Critical</td>
            <td>Critical incident</td>
        </tr>
        <tr>
            <td>😈 Attacking</td>
            <td>Under attack</td>
        </tr>
        <tr>
            <td>😴 Satisfied</td>
            <td>Systems healthy</td>
        </tr>
    </table>
    
    <h3>5️⃣ Metrics Panel (Bottom Right)</h3>
    <ul>
        <li>CPU % - System CPU utilization</li>
        <li>Memory % - RAM usage</li>
        <li>Network - Data in/out</li>
        <li>Disk I/O - Read/write operations</li>
    </ul>
</section>

<!-- INCIDENT FEED -->
<div class="page-break"></div>
<section id="incident-feed">
    <h1>🔔 Understanding the Incident Feed</h1>
    
    <h2>What is an Incident?</h2>
    <p>An incident is any security or observability event requiring attention:</p>
    
    <div class="feature-grid">
        <div class="feature-box">
            <h4>🔐 Brute-Force</h4>
            <p>Multiple failed login attempts, credential stuffing attacks, dictionary attacks</p>
        </div>
        <div class="feature-box">
            <h4>⚠️ API 500 Errors</h4>
            <p>Service crashes, high error rates, database failures</p>
        </div>
        <div class="feature-box">
            <h4>📈 CPU Overload</h4>
            <p>High CPU usage, runaway processes, resource exhaustion</p>
        </div>
        <div class="feature-box">
            <h4>🌐 Suspicious Traffic</h4>
            <p>DDoS, port scanning, anomalous requests</p>
        </div>
        <div class="feature-box">
            <h4>💥 Service Crash</h4>
            <p>Unexpected termination, health check failures</p>
        </div>
        <div class="feature-box">
            <h4>🎯 Custom</h4>
            <p>Any other observability event</p>
        </div>
    </div>
    
    <h2>Reading an Incident Card</h2>
    <div class="code-block">
┌──────────────────────────────────────────┐
│ BRUTE_FORCE      [CRITICAL] 14:25:32     │ Type + Severity
│                                          │
│ Multiple failed login attempts detected  │ Description
│ from 192.168.1.105 — 342 attempts in 5m │
│                                          │
│ Service: auth-api                        │ Affected service
│ [Not Resolved] [Select] [Copy]          │ Actions
└──────────────────────────────────────────┘
    </div>
    
    <h2>Severity Levels</h2>
    <table>
        <tr>
            <th>Severity</th>
            <th>Color</th>
            <th>Action Priority</th>
        </tr>
        <tr>
            <td>CRITICAL</td>
            <td>🔴 Red</td>
            <td>Immediate (1-5 min)</td>
        </tr>
        <tr>
            <td>HIGH</td>
            <td>🟠 Orange</td>
            <td>Urgent (15-30 min)</td>
        </tr>
        <tr>
            <td>MEDIUM</td>
            <td>🟡 Yellow</td>
            <td>Soon (1-2 hours)</td>
        </tr>
        <tr>
            <td>LOW</td>
            <td>🔵 Blue</td>
            <td>Plan (next sprint)</td>
        </tr>
    </table>
</section>

<!-- DASHBOARD FEATURES -->
<div class="page-break"></div>
<section id="dashboard-features">
    <h1>📊 Dashboard Features</h1>
    
    <h2>Feature 1: Live WebSocket Streaming</h2>
    <p>Incidents stream in real-time without page refresh. The dashboard automatically updates as new incidents are detected.</p>
    <div class="info">
        <strong>💡 Tip:</strong> If you don't see incidents appearing, verify the green connection indicator in the header.
    </div>
    
    <h2>Feature 2: AI-Powered Analysis</h2>
    <p>Click any incident to trigger automatic AI analysis:</p>
    <ul>
        <li>Extract key details</li>
        <li>Identify root cause</li>
        <li>Assess severity</li>
        <li>Recommend action</li>
        <li>Route to team</li>
    </ul>
    <div class="highlight">
        <strong>⏱️ Timing:</strong> Analysis completes in 2-5 seconds. Mascot shows "Analyzing" state during this time.
    </div>
    
    <h2>Feature 3: Action Center</h2>
    <p>Execute remediation actions directly from the dashboard:</p>
    <table>
        <tr>
            <th>Action</th>
            <th>Effect</th>
            <th>Use When</th>
        </tr>
        <tr>
            <td>Block IP</td>
            <td>Adds IP to firewall blocklist</td>
            <td>Brute-force or DDoS attack</td>
        </tr>
        <tr>
            <td>Restart Service</td>
            <td>Restarts the affected service</td>
            <td>Service crash or freeze</td>
        </tr>
        <tr>
            <td>Scan Service</td>
            <td>Runs security scan</td>
            <td>Suspicious activity detected</td>
        </tr>
        <tr>
            <td>Kill Process</td>
            <td>Terminates malicious process</td>
            <td>Runaway process or malware</td>
        </tr>
        <tr>
            <td>Auto-Remediate</td>
            <td>Executes AI recommendation</td>
            <td>Any incident where AI suggests action</td>
        </tr>
    </table>
    
    <h2>Feature 4: Real-Time Metrics</h2>
    <ul>
        <li>CPU, memory, disk, and network stats</li>
        <li>Updated every 1 second</li>
        <li>Shows impact of remediation actions</li>
        <li>Helps validate if incident is resolved</li>
    </ul>
</section>

<!-- TAKING ACTIONS -->
<div class="page-break"></div>
<section id="taking-actions">
    <h1>⚡ Taking Actions</h1>
    
    <h2>Step-by-Step: Execute an Action</h2>
    
    <h3>Step 1: Select an Incident</h3>
    <table>
        <tr>
            <td style="background: #dcfce7; padding: 20px;">Click on any incident card in the feed</td>
        </tr>
    </table>
    
    <h3>Step 2: Review AI Analysis</h3>
    <ul>
        <li>Read "What Happened"</li>
        <li>Understand "Why"</li>
        <li>Check "Suggested Action"</li>
        <li>Verify "Confidence" level</li>
    </ul>
    
    <h3>Step 3: Choose an Action</h3>
    <p>Click one of the action buttons:</p>
    <ul>
        <li>Follow AI recommendation, OR</li>
        <li>Choose a different action, OR</li>
        <li>Skip action and mark resolved manually</li>
    </ul>
    
    <h3>Step 4: Confirm & Execute</h3>
    <ul>
        <li>System shows loading state</li>
        <li>Mascot changes to "Action Running"</li>
        <li>Wait for action to complete</li>
    </ul>
    
    <h3>Step 5: Verify Resolution</h3>
    <ul>
        <li>Check mascot state (should be ✅ Success or 😴 Satisfied)</li>
        <li>Verify metrics return to normal</li>
        <li>Confirm incident shows "Resolved"</li>
    </ul>
    
    <h2>Example: Handling a Brute-Force Attack</h2>
    <div class="code-block">
1. New incident appears: BRUTE_FORCE [CRITICAL]
   
2. Click incident to analyze
   
3. Read analysis: "342 failed login attempts from 192.168.1.105"
   
4. Suggested Action: "Block 192.168.1.105"
   
5. Click "Block IP" button
   
6. See confirmation: "✅ IP 192.168.1.105 blocked"
   
7. Metrics show attack traffic dropping to 0
   
8. Mascot shows ✅ Success state
    </div>
    
    <div class="warning">
        <strong>⚠️ Important:</strong> Some actions cannot be undone immediately. Always read the suggested action carefully before executing.
    </div>
</section>

<!-- TESTING & SIMULATION -->
<div class="page-break"></div>
<section id="testing">
    <h1>🧪 Testing & Simulation</h1>
    
    <h2>Option 1: Auto-Generated Incidents</h2>
    <p><strong>Easiest method!</strong> Just start the backend and frontend. Incidents generate automatically every 5-15 seconds.</p>
    
    <h2>Option 2: Bulk Test Script</h2>
    <div class="code-block">
python test_scenarios.py
    </div>
    <p>Choose from menu:</p>
    <table>
        <tr>
            <td><strong>Option 1</strong></td>
            <td>Realistic Attack Sequence (BEST FOR DEMO)</td>
        </tr>
        <tr>
            <td><strong>Option 2</strong></td>
            <td>Generate 20 random incidents</td>
        </tr>
        <tr>
            <td><strong>Option 3</strong></td>
            <td>Test all incident types</td>
        </tr>
        <tr>
            <td><strong>Option 4</strong></td>
            <td>Stress test (50+ incidents)</td>
        </tr>
    </table>
    
    <h2>Option 3: Manual API Trigger</h2>
    <div class="code-block">
curl -X POST http://localhost:8000/api/incidents/simulate \\
  -H "Content-Type: application/json" \\
  -d '{
    "type": "brute_force",
    "severity": "critical",
    "source_ip": "192.168.1.100",
    "affected_service": "auth-api",
    "description": "1000 failed login attempts"
  }'
    </div>
    
    <h2>Simulated Incident Types</h2>
    <table>
        <tr>
            <th>Type</th>
            <th>Description</th>
            <th>Services</th>
        </tr>
        <tr>
            <td>brute_force</td>
            <td>Login attacks</td>
            <td>auth-api, admin-portal, ssh-gateway</td>
        </tr>
        <tr>
            <td>api_500</td>
            <td>Service errors</td>
            <td>payment-api, user-service, order-service</td>
        </tr>
        <tr>
            <td>cpu_overload</td>
            <td>Resource exhaustion</td>
            <td>ml-pipeline, data-processor, web-server</td>
        </tr>
        <tr>
            <td>suspicious_traffic</td>
            <td>Anomalous requests</td>
            <td>edge-proxy, load-balancer, firewall</td>
        </tr>
        <tr>
            <td>service_crash</td>
            <td>Process termination</td>
            <td>postgres-primary, redis-cluster, kafka-broker</td>
        </tr>
    </table>
</section>

<!-- DEMO CHECKLIST -->
<div class="page-break"></div>
<section id="demo-checklist">
    <h1>🎯 Demo Checklist for Hackathon</h1>
    
    <h2>Pre-Demo Verification (10 mins before)</h2>
    <ul class="demo-checklist">
        <li>Backend started and running on port 8000</li>
        <li>Frontend loaded to http://localhost:5173</li>
        <li>Dashboard shows green connection indicator</li>
        <li>Test script ready: python test_scenarios.py</li>
        <li>Browser cache cleared</li>
        <li>Terminal windows visible to judge</li>
    </ul>
    
    <h2>During Demo (5-7 minutes)</h2>
    <ul class="demo-checklist">
        <li>Explain dashboard layout and components</li>
        <li>Run test_scenarios.py option 1 (Attack Sequence)</li>
        <li>Point out incidents appearing in real-time</li>
        <li>Click an incident to show AI analysis</li>
        <li>Demonstrate executing an action</li>
        <li>Show mascot state changes</li>
        <li>Point out metrics updating in real-time</li>
        <li>Scroll through incident history</li>
        <li>Explain color-coded severity levels</li>
        <li>Share key architectural decisions</li>
    </ul>
    
    <h2>Answer Questions</h2>
    <ul class="demo-checklist">
        <li>Be ready to explain AI analysis process</li>
        <li>Discuss async/await architecture</li>
        <li>Explain scalability approach</li>
        <li>Show code if asked (keep files open)</li>
        <li>Mention alternative UIs (terminal, desktop)</li>
        <li>Talk about future enhancements</li>
    </ul>
    
    <h2>If Something Goes Wrong</h2>
    <table>
        <tr>
            <th>Problem</th>
            <th>Solution</th>
        </tr>
        <tr>
            <td>No incidents appearing</td>
            <td>Run test_scenarios.py to manually trigger</td>
        </tr>
        <tr>
            <td>Backend disconnected</td>
            <td>Refresh browser, check backend terminal</td>
        </tr>
        <tr>
            <td>Frontend won't load</td>
            <td>Restart frontend with npm run dev</td>
        </tr>
        <tr>
            <td>Mascot not animating</td>
            <td>Not critical - focus on analysis/actions</td>
        </tr>
        <tr>
            <td>Action doesn't execute</td>
            <td>Check browser console (F12) for errors</td>
        </tr>
    </table>
</section>

<!-- TROUBLESHOOTING -->
<div class="page-break"></div>
<section id="troubleshooting">
    <h1>🔧 Troubleshooting</h1>
    
    <h2>Connection Issues</h2>
    
    <h3>Problem: "Disconnected" status</h3>
    <div class="info">
        <strong>Cause:</strong> Backend not running or WebSocket connection lost
        
        <strong>Solution:</strong>
        <br>1. Open terminal and verify backend is running
        <br>2. Check if port 8000 is available: netstat -an | findstr 8000
        <br>3. Restart backend: uvicorn app.main:app --reload
        <br>4. Refresh browser (Ctrl+R)
    </div>
    
    <h2>No Incidents Appearing</h2>
    
    <h3>Problem: Dashboard is blank</h3>
    <div class="info">
        <strong>Cause:</strong> Incidents not being generated or WebSocket not connected
        
        <strong>Solution:</strong>
        <br>1. Check connection status (green dot)
        <br>2. Manually trigger incident:
        <div class="code-block">python test_scenarios.py</div>
        <br>3. Check browser console for errors (F12)
        <br>4. Verify backend logs for API errors
        <br>5. Hard refresh browser (Ctrl+Shift+R)
    </div>
    
    <h2>Performance Issues</h2>
    
    <h3>Problem: Dashboard is sluggish</h3>
    <div class="info">
        <strong>Cause:</strong> Too many incidents in feed or heavy metrics polling
        
        <strong>Solution:</strong>
        <br>1. Edit frontend code to show fewer incidents
        <br>2. Disable metrics polling temporarily
        <br>3. Close other browser tabs
        <br>4. Clear browser cache (Ctrl+Shift+Delete)
        <br>5. Restart frontend
    </div>
    
    <h2>Action Execution Issues</h2>
    
    <h3>Problem: Actions don't execute</h3>
    <div class="info">
        <strong>Cause:</strong> Backend action endpoint failing
        
        <strong>Solution:</strong>
        <br>1. Open browser console (F12)
        <br>2. Check Network tab for failed requests
        <br>3. Verify backend is running
        <br>4. Check backend logs for error messages
        <br>5. Try a different action
    </div>
    
    <h2>AI Analysis Not Working</h2>
    
    <h3>Problem: Analysis completes but shows error</h3>
    <div class="info">
        <strong>Cause:</strong> AI analyzer service issue or API key missing
        
        <strong>Solution:</strong>
        <br>1. Check backend logs for AI service errors
        <br>2. Verify AI API credentials are configured
        <br>3. Check internet connection for API calls
        <br>4. Try analyzing a different incident
        <br>5. Restart backend service
    </div>
    
    <h2>Getting Help</h2>
    <ul>
        <li>Check backend logs: tail logs/backend.log</li>
        <li>Check browser console: Press F12 → Console tab</li>
        <li>Check network: Press F12 → Network tab</li>
        <li>View API docs: http://localhost:8000/docs</li>
    </ul>
</section>

<!-- CONCLUSION -->
<div class="page-break"></div>
<section>
    <h1>🎓 Key Takeaways</h1>
    
    <h2>What Makes AegisX Special</h2>
    <ul>
        <li><strong>Real-time Streaming:</strong> WebSocket for instant incident notification</li>
        <li><strong>AI-Powered:</strong> Automatic root cause analysis</li>
        <li><strong>Autonomous Response:</strong> AI-suggested and executable actions</li>
        <li><strong>Multi-Platform:</strong> Web, terminal, and desktop interfaces</li>
        <li><strong>Beautiful UI:</strong> Engaging mascot with emotional states</li>
        <li><strong>Production-Ready:</strong> FastAPI backend, React frontend, async architecture</li>
    </ul>
    
    <h2>Perfect Use Cases</h2>
    <ul>
        <li>Security teams responding to hundreds of incidents daily</li>
        <li>DevOps teams managing production issues</li>
        <li>Startups needing incident management without enterprise software</li>
        <li>Training teams to learn incident response</li>
    </ul>
    
    <h2>Next Steps</h2>
    <ol>
        <li>Start the system following the Quick Start guide</li>
        <li>Explore with the auto-generated incidents</li>
        <li>Run test_scenarios.py to create realistic data</li>
        <li>Practice responding to different incident types</li>
        <li>Customize for your specific infrastructure</li>
    </ol>
    
    <h2>Support & Resources</h2>
    <ul>
        <li>GitHub: [Your Repo Link]</li>
        <li>Documentation: See AEGISX_USER_GUIDE.md</li>
        <li>Demo Guide: See QUICKSTART_DEMO.md</li>
        <li>API Docs: http://localhost:8000/docs</li>
    </ul>
    
    <div class="success" style="text-align: center; padding: 30px;">
        <h2 style="margin-bottom: 10px;">🚀 Ready to Get Started?</h2>
        <p>Follow the Quick Start guide above and launch AegisX in 5 minutes!</p>
        <p style="margin-top: 20px; font-size: 12px;">Happy incident response! 🛡️</p>
    </div>
</section>

</body>
</html>
"""

# Save to file and provide Python script to convert to PDF
with open("AEGISX_GUIDE.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ HTML Guide created: AEGISX_GUIDE.html")
print("\nTo convert to PDF, use one of these methods:")
print("\n1️⃣  Using Python (simplest):")
print("   pip install weasyprint")
print("   python -c \"from weasyprint import HTML; HTML('AEGISX_GUIDE.html').write_pdf('AEGISX_GUIDE.pdf')\"")
print("\n2️⃣  Using browser:")
print("   Open AEGISX_GUIDE.html in Chrome/Firefox → Print → Save as PDF")
print("\n3️⃣  Using online converter:")
print("   Upload to https://cloudconvert.com (HTML to PDF)")
print("\n📋 Then share AEGISX_GUIDE.pdf with your hackathon judge!")
