"""Incident API routes — REST + WebSocket."""

import asyncio
import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pydantic import BaseModel

from app.models.incident import Incident
from app.services.incident_engine import incident_engine

router = APIRouter(prefix="/api/incidents", tags=["incidents"])


class IncidentCreate(BaseModel):
    """Schema for creating a custom incident."""
    type: str
    severity: str
    source_ip: str
    affected_service: str
    description: str


@router.get("/", response_model=list[Incident])
async def list_incidents(limit: int = 20):
    """Get the most recent incidents."""
    return incident_engine.get_recent(limit=limit)


@router.get("/{incident_id}", response_model=Incident | None)
async def get_incident(incident_id: str):
    """Get a specific incident by ID."""
    return incident_engine.get_by_id(incident_id)


@router.post("/simulate", response_model=Incident)
async def simulate_incident(incident_data: IncidentCreate):
    """Create and broadcast a simulated incident (for testing/demos)."""
    return await incident_engine.create_incident(
        incident_type=incident_data.type,
        severity=incident_data.severity,
        source_ip=incident_data.source_ip,
        affected_service=incident_data.affected_service,
        description=incident_data.description,
    )


@router.websocket("/ws")
async def incident_websocket(websocket: WebSocket):
    """WebSocket endpoint for live incident streaming."""
    await websocket.accept()
    queue = incident_engine.subscribe()

    try:
        while True:
            incident: Incident = await queue.get()
            await websocket.send_text(
                json.dumps(incident.model_dump(), default=str)
            )
    except WebSocketDisconnect:
        pass
    except Exception:
        pass
    finally:
        incident_engine.unsubscribe(queue)

