import pytest

from bladerunner.core.events import Event, EventKind


@pytest.fixture
def normal_event() -> Event:
    return Event(
        kind=EventKind.PROCESS,
        source="test",
        agent_id="a1",
        data={"cpu_percent": 10, "mem_bytes": 1_000_000, "open_files": 3, "connections": 1},
    )


@pytest.fixture
def anomalous_event() -> Event:
    return Event(
        kind=EventKind.PROCESS,
        source="test",
        agent_id="a1",
        data={"cpu_percent": 99, "connections": 500},
    )
