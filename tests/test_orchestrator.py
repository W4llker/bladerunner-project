import asyncio

from bladerunner.actuators.log_only import LogOnlyActuator
from bladerunner.core.events import ActionKind, Event, EventKind, Severity, Verdict
from bladerunner.core.orchestrator import Orchestrator


class AlwaysAnomalousDetector:
    name = "always"

    def evaluate(self, event: Event) -> Verdict:
        return Verdict(
            event=event,
            detector=self.name,
            is_anomalous=True,
            severity=Severity.CRITICAL,
            reason="test",
        )


class FakeSensor:
    name = "fake"

    def __init__(self) -> None:
        self._sent = False

    async def stream(self):
        if self._sent:
            return
        self._sent = True
        yield Event(kind=EventKind.CUSTOM, source=self.name, agent_id="a1", data={})


def test_orchestrator_downgrades_in_monitor_mode() -> None:
    sensor = FakeSensor()
    orch = Orchestrator(
        sensors=[sensor],
        detectors=[AlwaysAnomalousDetector()],
        actuators={ActionKind.ALERT: LogOnlyActuator()},
        mode="monitor",
    )
    asyncio.run(orch.run())
