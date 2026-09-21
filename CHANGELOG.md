# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).
Versionado: [Semantic Versioning](https://semver.org/lang/es/).

## [Unreleased]

### Added
- Estructura base del proyecto.
- ProcessSensor, RuleBasedDetector, AnomalyDetector.
- LogOnlyActuator, ProcessKillerActuator.
- CLI `bladerunner watch`.
- API REST con `/health`.
- Demo examples/run_demo.py.
- CI con GitHub Actions.
- Documentación completa.
- Andamiaje agéntico: `TASKS.md`, `DEFINITION_OF_DONE.md`, plantillas de
  issues y PR, `.pre-commit-config.yaml`, `Makefile`, test e2e y
  `docs/agent_workflow.md`.
- Regla CRITICAL en `RuleBasedDetector` (CPU > 95%) para que el modo
  `enforce` pueda disparar KILL.

### Fixed
- `BaseSensor.stream()` ya no se declara `async def` (mypy lo tipaba como
  `Coroutine` en vez de `AsyncIterator`, rompiendo `ruff`/`mypy`).
- `tests/e2e/test_demo.py` usa `asyncio.create_subprocess_exec` en vez de
  `subprocess.Popen` (ASYNC220).

## [0.1.0] — 2024-XX-XX

Primera versión del MVP.

## Convención de versionado

`MAJOR.MINOR.PATCH`.

## Cómo actualizar

Cada PR añade entrada en [Unreleased] bajo Added, Changed, Deprecated,
Removed, Fixed, Security.
