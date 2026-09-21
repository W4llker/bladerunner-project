"""Clase base para sensores."""

from __future__ import annotations

import abc
from collections.abc import AsyncIterator

from bladerunner.core.events import Event


class BaseSensor(abc.ABC):
    name: str = "base_sensor"

    @abc.abstractmethod
    async def stream(self) -> AsyncIterator[Event]:
        raise NotImplementedError
