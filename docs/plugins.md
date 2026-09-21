# How to extend Bladerunner

## Rules

1. Inherit from the base class in `core/`.
2. `snake_case` file with the suffix `_sensor.py`, `_detector.py`, or
   `_actuator.py`.
3. A test in `tests/`.
4. Document it in `docs/architecture.md`.

## Sensor

```python
from typing import AsyncIterator
from bladerunner.core.events import Event, EventKind
from bladerunner.core.sensor import BaseSensor

class MySensor(BaseSensor):
    name = "my_sensor"

    def __init__(self, /* params */) -> None: ...

    async def stream(self) -> AsyncIterator[Event]:
        while True:
            yield Event(kind=EventKind.CUSTOM, source=self.name,
                        agent_id="...", data={...})
            await asyncio.sleep(self.interval)
```

## Detector

```python
from bladerunner.core.detector import BaseDetector
from bladerunner.core.events import Event, Severity, Verdict

class MyDetector(BaseDetector):
    name = "my_detector"

    def evaluate(self, event: Event) -> Verdict:
        if <condition>:
            return Verdict(event=event, detector=self.name,
                           is_anomalous=True, severity=Severity.MEDIUM,
                           reason="...", score=1.0)
        return Verdict(event=event, detector=self.name, is_anomalous=False)
```

## Actuator

```python
from bladerunner.core.actuator import BaseActuator
from bladerunner.core.events import Action

class MyActuator(BaseActuator):
    name = "my_actuator"

    def execute(self, action: Action) -> Action:
        try:
            # logic
            action.executed = True
            action.result = "result"
        except Exception as e:
            action.result = f"error: {e}"
        return action
```

## CLI registration

Add it to the corresponding list in `cli.py::watch`.

## Checklist

- [ ] Correct folder, correct suffix.
- [ ] Inherits from the base class.
- [ ] Unique `name`.
- [ ] Handles errors without propagating exceptions.
- [ ] Unit test.
- [ ] Registered in cli.py if applicable.
- [ ] Documented.
- [ ] `ruff check .` and `pytest -v` pass.
