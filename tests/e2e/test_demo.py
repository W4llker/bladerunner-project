"""Test end-to-end: verifica que la demo funciona de punta a punta.

Este test lanza el agente simulado, ejecuta Bladerunner en modo enforce
con un timeout corto, y verifica que el agente es terminado.
"""

from __future__ import annotations

import asyncio
import subprocess
import sys
from pathlib import Path

import pytest

from bladerunner.actuators.log_only import LogOnlyActuator
from bladerunner.actuators.process_killer import ProcessKillerActuator
from bladerunner.core.events import ActionKind
from bladerunner.core.orchestrator import Orchestrator
from bladerunner.detectors.rule_based import RuleBasedDetector
from bladerunner.sensors.process_sensor import ProcessSensor

AGENT_SCRIPT = Path(__file__).parent.parent.parent / "examples" / "simulated_agent.py"


async def _run_e2e(timeout: float = 20.0) -> bool:
    """Lanza el agente simulado y Bladerunner. Devuelve True si lo mata."""
    assert AGENT_SCRIPT.exists(), f"Falta {AGENT_SCRIPT}"

    proc = subprocess.Popen([sys.executable, str(AGENT_SCRIPT)])
    agent_id = "e2e-agent"

    sensor = ProcessSensor(pid=proc.pid, agent_id=agent_id, interval=0.3)
    detectors = [RuleBasedDetector()]

    def resolve(agent: str) -> int | None:
        return proc.pid if agent == agent_id else None

    actuators = {
        ActionKind.LOG: LogOnlyActuator(),
        ActionKind.ALERT: LogOnlyActuator(),
        ActionKind.KILL: ProcessKillerActuator(pid_resolver=resolve),
        ActionKind.ISOLATE: LogOnlyActuator(),
        ActionKind.RESTRICT: LogOnlyActuator(),
    }

    orch = Orchestrator(
        sensors=[sensor],
        detectors=detectors,
        actuators=actuators,
        mode="enforce",
    )

    try:
        await asyncio.wait_for(orch.run(), timeout=timeout)
    except asyncio.TimeoutError:
        pass
    finally:
        # Verificar si el proceso sigue vivo
        still_alive = proc.poll() is None
        if still_alive:
            proc.terminate()
            try:
                proc.wait(timeout=3)
            except subprocess.TimeoutExpired:
                proc.kill()

    # El test pasa si el proceso fue terminado por Bladerunner
    return not still_alive


@pytest.mark.e2e
def test_demo_kills_rogue_agent() -> None:
    """El agente simulado debe ser terminado por Bladerunner."""
    killed = asyncio.run(_run_e2e(timeout=20.0))
    assert killed, "Bladerunner no mató al agente simulado en 20s"
