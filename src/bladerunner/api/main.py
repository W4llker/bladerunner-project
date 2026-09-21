"""API REST mínima."""

from __future__ import annotations

from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Bladerunner API",
    description="Open source agent hunter — API de monitoreo",
    version="0.1.0",
)


class HealthResponse(BaseModel):
    status: str
    timestamp: datetime


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", timestamp=datetime.now(timezone.utc))


@app.get("/")
def root() -> dict[str, str]:
    return {"name": "Bladerunner", "description": "Open source agent hunter", "docs": "/docs"}
