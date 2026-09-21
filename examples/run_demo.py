"""Demo: lanza el agente simulado y Bladerunner lo vigila."""

from __future__ import annotations

import asyncio
import logging
import sys
from pathlib import Path

from bladerunner.actuators.log_only import LogOnlyActuator
from bladerunner.actuators.process_killer import ProcessKillerActuator
from bladerunner.core.events import ActionKind
from bladerunner.core.orchestrator import Orchestrator
from bladerunner.detectors.anomaly import AnomalyDetector
from bladerunner.detectors.rule_based import RuleBasedDetector
from bladerunner.sensors.process_sensor import ProcessSensor

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

AGENT_SCRIPT = Path(__file__).parent / "simulated_agent.py"


async def main() -> None:
    print(">> Lanzando agente simulado...")
    proc = await asyncio.create_subprocess_exec(sys.executable, str(AGENT_SCRIPT))
    agent_id = "demo-agent"

    sensor = ProcessSensor(pid=proc.pid, agent_id=agent_id, interval=0.5)
    detectors = [RuleBasedDetector(), AnomalyDetector(window=20, z_threshold=3.0)]

    def resolve(agent: str) -> int | None:
        return proc.pid if agent == agent_id else None

    actuators = {
        ActionKind.LOG: LogOnlyActuator(),
        ActionKind.ALERT: LogOnlyActuator(),
        ActionKind.KILL: ProcessKillerActuator(pid_resolver=resolve),
        ActionKind.ISOLATE: LogOnlyActuator(),
        ActionKind.RESTRICT: LogOnlyActuator(),
    }

    orch = Orchestrator(sensors=[sensor], detectors=detectors, actuators=actuators, mode="enforce")

    try:
        await asyncio.wait_for(orch.run(), timeout=30)
    except asyncio.TimeoutError:
        print(">> Timeout alcanzado, cerrando demo.")
    finally:
        if proc.returncode is None:
            proc.terminate()


if __name__ == "__main__":
    asyncio.run(main())
