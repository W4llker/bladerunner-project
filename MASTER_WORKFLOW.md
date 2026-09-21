# MASTER_WORKFLOW.md — Bladerunner's master workflow

> Single entry point for anyone working on Bladerunner.

## 1. What is Bladerunner?

A defensive cybersecurity framework to detect, isolate, and neutralize
rogue autonomous agents without inspecting their internal code.

## 2. Documentation map

### Understanding the project
- [README.md](README.md)
- [docs/architecture.md](docs/architecture.md)
- [docs/ethics.md](docs/ethics.md)
- [docs/roadmap.md](docs/roadmap.md)
- [docs/glossary.md](docs/glossary.md)

### Contributing
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [docs/testing.md](docs/testing.md)
- [docs/plugins.md](docs/plugins.md)
- [docs/decisions.md](docs/decisions.md)
- [CHANGELOG.md](CHANGELOG.md)

### Deploying
- [docs/deployment.md](docs/deployment.md)
- [SECURITY.md](SECURITY.md)

### Training models
- [docs/training.md](docs/training.md)

### For AI agents
- [AGENTS.md](AGENTS.md)

## 3. Developer workflow

1. Read README.md, AGENTS.md, docs/architecture.md.
2. Pick an issue from the roadmap or open a new one.
3. `git checkout -b feat/my-contribution`.
4. If it's an architectural decision → ADR in docs/decisions.md.
5. Implement following docs/plugins.md.
6. Write tests following docs/testing.md.
7. Add an entry to CHANGELOG.md [Unreleased].
8. Run `ruff check . && pytest -v`.
9. Commit using Conventional Commits, push, open a PR.
10. Review by a maintainer, merge to main.

## 4. AI agent workflow

1. Read AGENTS.md first.
2. Check docs/decisions.md before structural changes.
3. Follow docs/testing.md and docs/plugins.md.
4. Update CHANGELOG.md on every PR.
5. Run `ruff check . && pytest -v` before declaring success.
6. Never `git push` without authorization.
7. Never offensive actions outside the perimeter.

## 5. Project phases

- ✅ Phase 0 — Bootstrap (completed).
- 🟡 Phase 1 — Stable MVP (current).
- 🔵 Phase 2 — ML-based detection.
- 🟣 Phase 3 — Adaptive policies (RL).
- 🟢 Phase 4 — Integrations.
- 🔴 Phase 5 — Production.

## 6. Conventions

### Branches
- `main`, `feat/*`, `fix/*`, `docs/*`, `chore/*`, `test/*`, `security/*`.

### Commits (Conventional Commits)
- `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`, `security:`

### Versioning (SemVer)
`MAJOR.MINOR.PATCH`.

## 7. Code structure

```
src/bladerunner/
├── core/       → base classes
├── sensors/    → sensors
├── detectors/  → detectors
├── actuators/  → actuators
├── api/        → REST API
└── cli.py      → CLI
```

## 8. Getting started

```bash
git clone git@github.com:W4llker/bladerunner-project.git
cd bladerunner-project
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
ruff check . && pytest -v
python examples/run_demo.py
```
