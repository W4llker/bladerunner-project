"""Sensor de procesos."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator

import psutil

from bladerunner.core.events import Event, EventKind
from bladerunner.core.sensor import BaseSensor


class ProcessSensor(BaseSensor):
    name = "process_sensor"

    def __init__(self, pid: int, agent_id: str, interval: float = 1.0) -> None:
        self.pid = pid
        self.agent_id = agent_id
        self.interval = interval

    async def stream(self) -> AsyncIterator[Event]:
        try:
            proc = psutil.Process(self.pid)
        except psutil.NoSuchProcess:
            return

        while True:
            try:
                if not proc.is_running():
                    return
                with proc.oneshot():
                    mem = proc.memory_info().rss
                    cpu = proc.cpu_percent(interval=None)
                    open_files = len(proc.open_files())
                    conns = len(proc.connections(kind="inet"))

                yield Event(
                    kind=EventKind.PROCESS,
                    source=self.name,
                    agent_id=self.agent_id,
                    data={
                        "pid": self.pid,
                        "cpu_percent": cpu,
                        "mem_bytes": mem,
                        "open_files": open_files,
                        "connections": conns,
                    },
                )
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                return
            await asyncio.sleep(self.interval)
