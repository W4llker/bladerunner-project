# Testing strategy

## Stack

- pytest + pytest-asyncio
- pytest-cov (minimum 80%)
- unittest.mock

## Conventions

- `tests/test_<module>.py`
- `test_<behavior>`
- Arrange–Act–Assert

## Async tests

`async def` directly (`auto` mode in pyproject).

## Shared fixtures (conftest.py)

`normal_event` and `anomalous_event` events.

## Categories

- Unit: `tests/test_*.py`
- Integration: `tests/integration/`
- E2E: `tests/e2e/`
- Regression: `tests/regression/`

## Coverage

```bash
pytest --cov=src/bladerunner --cov-report=term-missing
```

Thresholds:
- core: >90%
- detectors: >85%
- sensors/actuators: >80%
- global: >80%

## Rules

1. Every feature includes tests.
2. Every bug fix includes a regression test.
3. Use fixtures.
4. Don't delete tests without justification.
