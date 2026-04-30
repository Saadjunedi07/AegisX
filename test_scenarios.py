#!/usr/bin/env python3
"""
AegisX Test Scenario Generator
Generates realistic incident scenarios for testing & demos
"""

import asyncio
import json
import random
import httpx
from datetime import datetime

BASE_URL = "http://localhost:8000"

# Incident templates with realistic variations
INCIDENT_SCENARIOS = [
    {
        "type": "brute_force",
        "descriptions": [
            "Multiple failed login attempts detected from {ip} — {count} attempts in {window}",
            "Brute-force attack targeting {service} from {ip}",
            "Credential stuffing attack detected — {count} unique passwords tried",
            "Dictionary attack on admin panel from {ip}",
            "SSH brute-force: {count} failed attempts from {ip} in {window}",
        ],
        "severity_weights": {"critical": 0.5, "high": 0.3, "medium": 0.2},
        "services": ["auth-api", "admin-portal", "ssh-gateway", "vpn-gateway"],
    },
    {
        "type": "api_500",
        "descriptions": [
            "Spike in 500 errors on {service} — {count} errors in last {window}",
            "{service} returning HTTP 500 — database connection pool exhausted",
            "Internal server error cascade — upstream dependency timeout",
            "{service} crash loop detected — OOM killer triggered",
            "Payment processing failing with 500 errors — {count} failed transactions",
        ],
        "severity_weights": {"high": 0.4, "critical": 0.2, "medium": 0.4},
        "services": ["payment-api", "user-service", "order-service", "search-api"],
    },
    {
        "type": "cpu_overload",
        "descriptions": [
            "CPU usage at {cpu}% on {service} — sustained for {window}",
            "Runaway process consuming {cpu}% CPU on {service}",
            "Compute node overloaded at {cpu}% utilization — queue backing up",
            "CPU thermal throttling detected — {cpu}% load on {service}",
        ],
        "severity_weights": {"high": 0.4, "critical": 0.3, "medium": 0.3},
        "services": ["ml-pipeline", "data-processor", "cache-server", "web-server"],
    },
    {
        "type": "suspicious_traffic",
        "descriptions": [
            "Anomalous traffic pattern from {ip} — potential DDoS reconnaissance",
            "Port scanning detected from {ip} targeting {service}",
            "Suspicious outbound traffic from internal host to {ip}",
            "Anomalous DNS queries — potential data exfiltration attempt",
            "Botnet-like traffic pattern detected from {ip}",
        ],
        "severity_weights": {"high": 0.4, "medium": 0.3, "critical": 0.2, "low": 0.1},
        "services": ["edge-proxy", "load-balancer", "firewall", "dns-server"],
    },
    {
        "type": "service_crash",
        "descriptions": [
            "{service} process terminated unexpectedly — exit code {exit_code}",
            "{service} failed health check {count} consecutive times",
            "Segmentation fault in {service} — core dump generated",
            "{service} out of memory — killed by OOM killer",
        ],
        "severity_weights": {"critical": 0.5, "high": 0.4, "medium": 0.1},
        "services": ["postgres-primary", "redis-cluster", "kafka-broker", "nginx-ingress"],
    },
]

ATTACKER_IPS = [
    "192.168.1.105", "10.0.0.47", "203.0.113.42", "198.51.100.73",
    "45.33.32.156", "91.198.174.192", "185.220.101.34",
]


def generate_test_incident(scenario_type=None):
    """Generate a single test incident."""
    scenario = random.choice(INCIDENT_SCENARIOS) if scenario_type is None else [s for s in INCIDENT_SCENARIOS if s["type"] == scenario_type][0]
    
    severity = random.choices(
        list(scenario["severity_weights"].keys()),
        weights=list(scenario["severity_weights"].values()),
        k=1
    )[0]
    
    service = random.choice(scenario["services"])
    ip = random.choice(ATTACKER_IPS)
    desc = random.choice(scenario["descriptions"])
    
    description = desc.format(
        ip=ip,
        service=service,
        count=random.randint(50, 5000),
        window=random.choice(["30s", "1m", "5m", "10m"]),
        cpu=random.randint(85, 99),
        exit_code=random.randint(1, 139),
    )
    
    return {
        "type": scenario["type"],
        "severity": severity,
        "source_ip": ip,
        "affected_service": service,
        "description": description,
    }


async def send_incident(client: httpx.AsyncClient, incident: dict):
    """Send an incident to the backend."""
    try:
        response = await client.post(
            f"{BASE_URL}/api/incidents/simulate",
            json=incident,
            timeout=5
        )
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Created: {incident['type'].upper()} [{incident['severity'].upper()}]")
            print(f"   Service: {incident['affected_service']}")
            print(f"   IP: {incident['source_ip']}")
            return True
        else:
            print(f"❌ Failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


async def demo_realistic_attack_sequence():
    """Simulate a realistic attack sequence for demo purposes."""
    print("\n🎬 STARTING REALISTIC ATTACK SEQUENCE DEMO\n")
    print("=" * 60)
    
    attack_scenario = [
        {
            "type": "suspicious_traffic",
            "count": 1,
            "delay": 0,
            "description": "🔍 Phase 1: Reconnaissance - Attacker probing network"
        },
        {
            "type": "suspicious_traffic",
            "count": 2,
            "delay": 3,
            "description": "🔍 Phase 2: Port scanning intensifies"
        },
        {
            "type": "brute_force",
            "count": 1,
            "delay": 5,
            "description": "⚔️  Phase 3: Brute force attack begins"
        },
        {
            "type": "brute_force",
            "count": 2,
            "delay": 3,
            "description": "⚔️  Phase 4: Multiple attack vectors"
        },
        {
            "type": "api_500",
            "count": 1,
            "delay": 4,
            "description": "💥 Phase 5: Service compromise - APIs failing"
        },
        {
            "type": "cpu_overload",
            "count": 1,
            "delay": 3,
            "description": "🔥 Phase 6: Resource exhaustion - CPU spiking"
        },
        {
            "type": "service_crash",
            "count": 1,
            "delay": 2,
            "description": "💀 Phase 7: Critical service crashed"
        },
    ]
    
    async with httpx.AsyncClient() as client:
        for phase in attack_scenario:
            print(f"\n{phase['description']}")
            print("-" * 60)
            
            # Wait before phase
            if phase['delay'] > 0:
                print(f"⏳ Waiting {phase['delay']}s before phase...")
                for i in range(phase['delay']):
                    await asyncio.sleep(1)
                    print(f"   {i+1}/{phase['delay']}")
            
            # Generate incidents for this phase
            for i in range(phase['count']):
                incident = generate_test_incident(phase['type'])
                success = await send_incident(client, incident)
                if i < phase['count'] - 1:
                    await asyncio.sleep(1)
    
    print("\n" + "=" * 60)
    print("✅ Attack sequence complete! Check the dashboard.\n")


async def bulk_test_incidents(num_incidents: int = 20):
    """Generate multiple incidents rapidly."""
    print(f"\n📊 GENERATING {num_incidents} TEST INCIDENTS\n")
    print("=" * 60)
    
    async with httpx.AsyncClient() as client:
        success_count = 0
        
        for i in range(num_incidents):
            incident = generate_test_incident()
            success = await send_incident(client, incident)
            if success:
                success_count += 1
            
            # Small delay between incidents
            if i < num_incidents - 1:
                await asyncio.sleep(0.5)
        
        print("=" * 60)
        print(f"\n✅ Generated {success_count}/{num_incidents} incidents successfully\n")


async def test_all_incident_types():
    """Generate one incident of each type."""
    print("\n🧪 TESTING ALL INCIDENT TYPES\n")
    print("=" * 60)
    
    incident_types = [s["type"] for s in INCIDENT_SCENARIOS]
    
    async with httpx.AsyncClient() as client:
        for incident_type in incident_types:
            incident = generate_test_incident(incident_type)
            print(f"\nTesting: {incident_type.upper()}")
            print(f"Description: {incident['description']}")
            await send_incident(client, incident)
            await asyncio.sleep(1)
    
    print("\n" + "=" * 60)
    print("✅ All incident types tested!\n")


async def stress_test(num_incidents: int = 50, interval: float = 0.5):
    """Stress test with rapid incident generation."""
    print(f"\n⚡ STRESS TEST: {num_incidents} incidents with {interval}s interval\n")
    print("=" * 60)
    
    async with httpx.AsyncClient() as client:
        start_time = datetime.now()
        
        for i in range(num_incidents):
            incident = generate_test_incident()
            await send_incident(client, incident)
            
            if (i + 1) % 10 == 0:
                elapsed = (datetime.now() - start_time).total_seconds()
                rate = (i + 1) / elapsed
                print(f"📈 Progress: {i+1}/{num_incidents} ({rate:.1f} incidents/sec)")
            
            await asyncio.sleep(interval)
    
    total_time = (datetime.now() - start_time).total_seconds()
    print("=" * 60)
    print(f"\n✅ Stress test complete!")
    print(f"   Total: {num_incidents} incidents")
    print(f"   Time: {total_time:.1f}s")
    print(f"   Rate: {num_incidents / total_time:.1f} incidents/sec\n")


async def main():
    """Interactive test menu."""
    print("\n" + "=" * 60)
    print("🛡️  AegisX Test Scenario Generator")
    print("=" * 60)
    print("\nChoose a test scenario:")
    print("\n1. 🎬 Realistic Attack Sequence (RECOMMENDED for DEMO)")
    print("   → Shows full attack lifecycle with delays")
    print("\n2. 📊 Bulk Generation (20 incidents)")
    print("   → Quick load test with random incidents")
    print("\n3. 🧪 Test All Types (1 of each)")
    print("   → Verify all incident types work")
    print("\n4. ⚡ Stress Test (50 incidents)")
    print("   → Measure performance under load")
    print("\n0. 🚫 Exit")
    print("\n" + "-" * 60)
    
    choice = input("Select option (0-4): ").strip()
    
    try:
        if choice == "1":
            await demo_realistic_attack_sequence()
        elif choice == "2":
            await bulk_test_incidents(20)
        elif choice == "3":
            await test_all_incident_types()
        elif choice == "4":
            num = input("How many incidents? (default 50): ").strip()
            num = int(num) if num else 50
            interval = input("Interval between incidents in seconds? (default 0.5): ").strip()
            interval = float(interval) if interval else 0.5
            await stress_test(num, interval)
        elif choice == "0":
            print("\nGoodbye! 👋\n")
            return
        else:
            print("\n❌ Invalid choice. Please try again.\n")
            await main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Test interrupted by user\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        print("Make sure the backend is running: uvicorn app.main:app --reload")


if __name__ == "__main__":
    asyncio.run(main())
