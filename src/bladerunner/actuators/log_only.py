"""Actuador que solo registra."""

from __future__ import annotations

import logging

from bladerunner.core.actuator import BaseActuator
from bladerunner.core.events import Action

logger = logging.getLogger("bladerunner.actuator.log")


class LogOnlyActuator(BaseActuator):
    name = "log_only"

    def execute(self, action: Action) -> Action:
        logger.warning(
            "[%s] agente=%s motivo=%s",
            action.severity.value.upper(),
            action.target_agent_id,
            action.reason,
        )
        action.executed = True
        action.result = "logged"
        return action
