# Estrategia de pruebas

## Stack

- pytest + pytest-asyncio
- pytest-cov (mínimo 80%)
- unittest.mock

## Convenciones

- `tests/test_<módulo>.py`
- `test_<comportamiento>`
- Arrange–Act–Assert

## Tests async

`async def` directo (modo `auto` en pyproject).

## Fixtures compartidas (conftest.py)

Eventos `normal_event` y `anomalous_event`.

## Categorías

- Unitarios: `tests/test_*.py`
- Integración: `tests/integration/`
- E2E: `tests/e2e/`
- Regresión: `tests/regression/`

## Cobertura

```bash
pytest --cov=src/bladerunner --cov-report=term-missing
```

Umbrales:
- core: >90%
- detectors: >85%
- sensors/actuators: >80%
- global: >80%

## Reglas

1. Cada feature incluye tests.
2. Cada bug fix incluye test de regresión.
3. Usar fixtures.
4. No borrar tests sin justificar.
