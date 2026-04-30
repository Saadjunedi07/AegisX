"""Centralized Aegis emotion/state engine for the terminal UI."""

from __future__ import annotations

from dataclasses import dataclass
from time import monotonic


AegisState = str
AegisEvent = str


EVENT_TO_STATE: dict[AegisEvent, AegisState] = {
    "incident_detected": "alert",
    "critical_incident": "critical",
    "scan_started": "scanning",
    "analysis_started": "thinking",
    "action_running": "healing",
    "action_success": "success",
    "action_failed": "alert",
    "idle_timeout": "sleeping",
    "metrics_normal": "idle",
    "metrics_warning": "scanning",
    "metrics_critical": "critical",
    "default": "idle",
}

STATE_PRIORITY: dict[AegisState, int] = {
    "idle": 0,
    "monitoring": 1,
    "sleeping": 1,
    "scanning": 2,
    "thinking": 3,
    "healing": 4,
    "success": 5,
    "alert": 6,
    "critical": 7,
}


@dataclass(frozen=True)
class AegisEmotionSnapshot:
    state: AegisState = "idle"
    event: AegisEvent = "default"
    since: float = 0.0


class AegisEmotionEngine:
    """Maps product events into mascot states with priority rules."""

    def __init__(self, initial_state: AegisState = "idle") -> None:
        self.snapshot = AegisEmotionSnapshot(
            state=initial_state,
            event="default",
            since=monotonic(),
        )

    def dispatch(self, event: AegisEvent, *, force: bool = False) -> AegisEmotionSnapshot:
        next_state = EVENT_TO_STATE.get(event, EVENT_TO_STATE["default"])
        if force or self._should_replace(next_state):
            self.snapshot = AegisEmotionSnapshot(
                state=next_state,
                event=event,
                since=monotonic(),
            )
        return self.snapshot

    def reset(self) -> AegisEmotionSnapshot:
        return self.dispatch("default", force=True)

    def _should_replace(self, next_state: AegisState) -> bool:
        current = self.snapshot.state
        return STATE_PRIORITY.get(next_state, 0) >= STATE_PRIORITY.get(current, 0) or current == "success"


def severity_to_event(severity: str) -> AegisEvent:
    return "critical_incident" if severity == "critical" else "incident_detected"


def incident_to_event(incident: dict) -> AegisEvent:
    severity = incident.get("severity", "low")
    incident_type = incident.get("type", "")
    if severity == "critical" or incident_type == "service_crash":
        return "critical_incident"
    return "incident_detected"


def action_result_to_event(result: dict | None) -> AegisEvent:
    return "action_success" if result and result.get("status") == "success" else "action_failed"


def metrics_to_event(metrics: dict | None) -> AegisEvent:
    if not metrics:
        return "metrics_normal"
    highest_load = max(
        float(metrics.get("cpu_percent", 0)),
        float(metrics.get("memory_percent", 0)),
        float(metrics.get("disk_percent", 0)),
    )
    if highest_load >= 95:
        return "metrics_critical"
    if highest_load >= 85 or int(metrics.get("network_connections", 0)) > 700:
        return "metrics_warning"
    return "metrics_normal"
