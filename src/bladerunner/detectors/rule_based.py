"""Detector basado en reglas."""

from __future__ import annotations

from collections.abc import Callable

from bladerunner.core.detector import BaseDetector
from bladerunner.core.events import Event, Severity, Verdict

Rule = Callable[[Event], tuple[bool, str, Severity]]


class RuleBasedDetector(BaseDetector):
    name = "rule_based"

    def __init__(self, rules: list[Rule] | None = None) -> None:
        self.rules = rules or self._default_rules()

    @staticmethod
    def _default_rules() -> list[Rule]:
        return [
            lambda e: (e.data.get("cpu_percent", 0) > 90, "CPU > 90%", Severity.MEDIUM),
            lambda e: (e.data.get("connections", 0) > 100, "Más de 100 conexiones", Severity.HIGH),
            lambda e: (
                e.data.get("open_files", 0) > 500,
                "Exceso de archivos abiertos",
                Severity.MEDIUM,
            ),
        ]

    def evaluate(self, event: Event) -> Verdict:
        for rule in self.rules:
            triggered, reason, severity = rule(event)
            if triggered:
                return Verdict(
                    event=event,
                    detector=self.name,
                    is_anomalous=True,
                    severity=severity,
                    reason=reason,
                    score=1.0,
                )
        return Verdict(
            event=event,
            detector=self.name,
            is_anomalous=False,
            reason="Sin reglas activadas",
            score=0.0,
        )
