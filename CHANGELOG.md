# Changelog

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- Base project structure.
- ProcessSensor, RuleBasedDetector, AnomalyDetector.
- LogOnlyActuator, ProcessKillerActuator.
- CLI `bladerunner watch`.
- REST API with `/health`.
- Demo examples/run_demo.py.
- CI with GitHub Actions.
- Complete documentation.
- Agentic development scaffolding: `TASKS.md`, `DEFINITION_OF_DONE.md`, issue
  and PR templates, `.pre-commit-config.yaml`, `Makefile`, e2e test, and
  `docs/agent_workflow.md`.
- CRITICAL rule in `RuleBasedDetector` (CPU > 95%) so that `enforce` mode
  can trigger KILL.
- `NOTICE` file and `CITATION.cff` with author attribution
  (Marcelo Báez Cerda).
- Developer Certificate of Origin (DCO) sign-off requirement in
  `CONTRIBUTING.md`.

### Changed
- `LICENSE` now contains the full Apache 2.0 text, with copyright
  "Marcelo Báez Cerda and Bladerunner Contributors".
- `pyproject.toml`: author and maintainer set to Marcelo Báez Cerda.
- `README.md`: new "Author and citation" section.
- SPDX license and copyright headers on all Python source files.
- `GOVERNANCE.md`: founder listed by full name.

### Fixed
- `BaseSensor.stream()` is no longer declared `async def` (mypy inferred it
  as `Coroutine` instead of `AsyncIterator`, breaking `ruff`/`mypy`).
- `tests/e2e/test_demo.py` now uses `asyncio.create_subprocess_exec` instead
  of `subprocess.Popen` (ASYNC220).

## [0.1.0] — 2024-XX-XX

First MVP release.

## Versioning convention

`MAJOR.MINOR.PATCH`.

## How to update

Every PR adds an entry under [Unreleased], in Added, Changed, Deprecated,
Removed, Fixed, or Security.
