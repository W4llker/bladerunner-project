# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Marcelo Báez Cerda and Bladerunner Contributors

"""Clase base para actuadores."""

from __future__ import annotations

import abc

from bladerunner.core.events import Action


class BaseActuator(abc.ABC):
    name: str = "base_actuator"

    @abc.abstractmethod
    def execute(self, action: Action) -> Action:
        raise NotImplementedError
