# Cómo extender Bladerunner

## Reglas

1. Heredar de clase base en `core/`.
2. Archivo `snake_case` con sufijo `_sensor.py`, `_detector.py` o `_actuator.py`.
3. Test en `tests/`.
4. Documentar en `docs/architecture.md`.

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
        if <condición>:
            return Verdict(event=event, detector=self.name,
                           is_anomalous=True, severity=Severity.MEDIUM,
                           reason="...", score=1.0)
        return Verdict(event=event, detector=self.name, is_anomalous=False)
```

## Actuador

```python
from bladerunner.core.actuator import BaseActuator
from bladerunner.core.events import Action

class MyActuator(BaseActuator):
    name = "my_actuator"

    def execute(self, action: Action) -> Action:
        try:
            # lógica
            action.executed = True
            action.result = "resultado"
        except Exception as e:
            action.result = f"error: {e}"
        return action
```

## Registro en CLI

Añadir a la lista correspondiente en `cli.py::watch`.

## Checklist

- [ ] Carpeta correcta, sufijo correcto.
- [ ] Hereda de clase base.
- [ ] `name` único.
- [ ] Maneja errores sin propagar excepciones.
- [ ] Test unitario.
- [ ] Registrado en cli.py si aplica.
- [ ] Documentado.
- [ ] `ruff check .` y `pytest -v` pasan.
