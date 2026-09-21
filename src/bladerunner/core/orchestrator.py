"""Orquestador: conecta sensores, detectores y actuadores."""

from __future__ import annotations

import asyncio
import logging
from collections.abc import Iterable

from bladerunner.core.actuator import BaseActuator
from bladerunner.core.detector import BaseDetector
from bladerunner.core.events import Action, ActionKind, Event, Severity, Verdict
from bladerunner.core.sensor import BaseSensor

logger = logging.getLogger(__name__)


class Orchestrator:
    def __init__(
        self,
        sensors: Iterable[BaseSensor],
        detectors: Iterable[BaseDetector],
        actuators: dict[ActionKind, BaseActuator],
        mode: str = "monitor",
    ) -> None:
        self.sensors = list(sensors)
        self.detectors = list(detectors)
        self.actuators = actuators
        self.mode = mode

    def _decide(self, verdicts: list[Verdict]) -> Action | None:
        anomalies = [v for v in verdicts if v.is_anomalous]
        if not anomalies:
            return None

        order = [Severity.INFO, Severity.LOW, Severity.MEDIUM, Severity.HIGH, Severity.CRITICAL]
        top = max(anomalies, key=lambda v: order.index(v.severity))

        mapping = {
            Severity.INFO: ActionKind.LOG,
            Severity.LOW: ActionKind.LOG,
            Severity.MEDIUM: ActionKind.ALERT,
            Severity.HIGH: ActionKind.ISOLATE,
            Severity.CRITICAL: ActionKind.KILL,
        }
        kind = mapping[top.severity]

        if self.mode == "monitor" and kind in (ActionKind.ISOLATE, ActionKind.KILL):
            logger.warning(
                "Modo monitor: acción %s degradada a ALERT para agente %s",
                kind.value,
                top.event.agent_id,
            )
            kind = ActionKind.ALERT

        return Action(
            kind=kind,
            target_agent_id=top.event.agent_id,
            severity=top.severity,
            reason=top.reason,
        )

    async def _handle_event(self, event: Event) -> None:
        verdicts = [d.evaluate(event) for d in self.detectors]
        action = self._decide(verdicts)
        if action is None:
            return
        actuator = self.actuators.get(action.kind)
        if actuator is None:
            logger.error("No hay actuador para %s", action.kind)
            return
        result = actuator.execute(action)
        logger.info(
            "Acción %s sobre %s: %s", result.kind.value, result.target_agent_id, result.result
        )

    async def run(self) -> None:
        async def consume(sensor: BaseSensor) -> None:
            async for event in sensor.stream():
                await self._handle_event(event)

        await asyncio.gather(*(consume(s) for s in self.sensors))
