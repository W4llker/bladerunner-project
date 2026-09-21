"""CLI de Bladerunner."""

from __future__ import annotations

import asyncio
import logging

import typer
from rich.console import Console

from bladerunner.actuators.log_only import LogOnlyActuator
from bladerunner.actuators.process_killer import ProcessKillerActuator
from bladerunner.core.events import ActionKind
from bladerunner.core.orchestrator import Orchestrator
from bladerunner.detectors.anomaly import AnomalyDetector
from bladerunner.detectors.rule_based import RuleBasedDetector
from bladerunner.sensors.process_sensor import ProcessSensor

app = typer.Typer(help="Bladerunner — Open Source Agent Hunter")
console = Console()


@app.command()
def watch(
    pid: int = typer.Argument(..., help="PID del agente a vigilar"),
    agent_id: str = typer.Option("agent-1", help="Identificador lógico del agente"),
    mode: str = typer.Option("monitor", help="monitor | enforce"),
    interval: float = typer.Option(1.0, help="Segundos entre muestras"),
) -> None:
    """Vigila un proceso y aplica contramedidas si se descontrola."""
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    sensor = ProcessSensor(pid=pid, agent_id=agent_id, interval=interval)
    detectors = [RuleBasedDetector(), AnomalyDetector()]

    def resolve(agent: str) -> int | None:
        return pid if agent == agent_id else None

    actuators = {
        ActionKind.LOG: LogOnlyActuator(),
        ActionKind.ALERT: LogOnlyActuator(),
        ActionKind.KILL: ProcessKillerActuator(pid_resolver=resolve),
        ActionKind.ISOLATE: LogOnlyActuator(),
        ActionKind.RESTRICT: LogOnlyActuator(),
    }

    orch = Orchestrator(sensors=[sensor], detectors=detectors, actuators=actuators, mode=mode)

    console.print(f"[bold green]Bladerunner[/] vigilando PID={pid} agent={agent_id} modo={mode}")
    try:
        asyncio.run(orch.run())
    except KeyboardInterrupt:
        console.print("\n[yellow]Detenido por el usuario.[/]")


if __name__ == "__main__":
    app()
