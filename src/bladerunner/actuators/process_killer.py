"""Actuador que mata un proceso."""

from __future__ import annotations

import logging

import psutil

from bladerunner.core.actuator import BaseActuator
from bladerunner.core.events import Action

logger = logging.getLogger("bladerunner.actuator.kill")


class ProcessKillerActuator(BaseActuator):
    name = "process_killer"

    def __init__(self, pid_resolver) -> None:
        self.pid_resolver = pid_resolver

    def execute(self, action: Action) -> Action:
        pid = self.pid_resolver(action.target_agent_id)
        if pid is None:
            action.result = "pid no encontrado"
            return action
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            try:
                proc.wait(timeout=3)
            except psutil.TimeoutExpired:
                proc.kill()
            action.executed = True
            action.result = f"proceso {pid} terminado"
        except psutil.NoSuchProcess:
            action.result = f"proceso {pid} ya no existe"
        except psutil.AccessDenied:
            action.result = f"sin permisos para matar {pid}"
        return action
