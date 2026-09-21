"""Detector de anomalías por z-score."""

from __future__ import annotations

from collections import deque
from statistics import mean, pstdev

from bladerunner.core.detector import BaseDetector
from bladerunner.core.events import Event, Severity, Verdict


class AnomalyDetector(BaseDetector):
    name = "anomaly"

    def __init__(
        self, window: int = 60, z_threshold: float = 3.0, tracked_metrics: list[str] | None = None
    ) -> None:
        self.window = window
        self.z_threshold = z_threshold
        self.tracked_metrics = tracked_metrics or [
            "cpu_percent",
            "mem_bytes",
            "open_files",
            "connections",
        ]
        self._history: dict[str, deque[float]] = {
            m: deque(maxlen=window) for m in self.tracked_metrics
        }

    def evaluate(self, event: Event) -> Verdict:
        worst_z = 0.0
        worst_metric = ""

        for metric in self.tracked_metrics:
            value = event.data.get(metric)
            if not isinstance(value, (int, float)):
                continue
            hist = self._history[metric]
            if len(hist) >= 10:
                mu = mean(hist)
                sigma = pstdev(hist) or 1e-9
                z = abs(value - mu) / sigma
                if z > worst_z:
                    worst_z = z
                    worst_metric = metric
            hist.append(float(value))

        if worst_z >= self.z_threshold:
            severity = Severity.HIGH if worst_z >= self.z_threshold * 1.5 else Severity.MEDIUM
            return Verdict(
                event=event,
                detector=self.name,
                is_anomalous=True,
                severity=severity,
                reason=f"Anomalía en '{worst_metric}' (z={worst_z:.2f})",
                score=min(worst_z / (self.z_threshold * 2), 1.0),
            )

        return Verdict(
            event=event,
            detector=self.name,
            is_anomalous=False,
            reason="Dentro del baseline",
            score=0.0,
        )
