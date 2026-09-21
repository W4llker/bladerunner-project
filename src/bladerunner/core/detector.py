"""Clase base para detectores."""

from __future__ import annotations

import abc

from bladerunner.core.events import Event, Verdict


class BaseDetector(abc.ABC):
    name: str = "base_detector"

    @abc.abstractmethod
    def evaluate(self, event: Event) -> Verdict:
        raise NotImplementedError
