"""Modelos de datos compartidos."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class Severity(str, Enum):
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class EventKind(str, Enum):
    PROCESS = "process"
    FILE = "file"
    NETWORK = "network"
    API_CALL = "api_call"
    CUSTOM = "custom"


class Event(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    kind: EventKind
    source: str
    agent_id: str
    data: dict[str, Any] = Field(default_factory=dict)


class Verdict(BaseModel):
    event: Event
    detector: str
    is_anomalous: bool
    severity: Severity = Severity.INFO
    reason: str = ""
    score: float = 0.0


class ActionKind(str, Enum):
    LOG = "log"
    ALERT = "alert"
    RESTRICT = "restrict"
    ISOLATE = "isolate"
    KILL = "kill"


class Action(BaseModel):
    kind: ActionKind
    target_agent_id: str
    severity: Severity
    reason: str
    metadata: dict[str, Any] = Field(default_factory=dict)
    executed: bool = False
    result: str = ""
