# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Marcelo Báez Cerda and Bladerunner Contributors

"""Clase base para detectores."""

from __future__ import annotations

import abc

from bladerunner.core.events import Event, Verdict


class BaseDetector(abc.ABC):
    name: str = "base_detector"

    @abc.abstractmethod
    def evaluate(self, event: Event) -> Verdict:
        raise NotImplementedError
