# MASTER_WORKFLOW.md — Flujo maestro de Bladerunner

> Punto de entrada único para cualquier persona que trabaje en Bladerunner.

## 1. ¿Qué es Bladerunner?

Framework de ciberseguridad defensiva para detectar, aislar y neutralizar
agentes autónomos descontrolados sin inspeccionar su código interno.

## 2. Mapa de documentación

### Entender el proyecto
- [README.md](README.md)
- [docs/architecture.md](docs/architecture.md)
- [docs/ethics.md](docs/ethics.md)
- [docs/roadmap.md](docs/roadmap.md)
- [docs/glossary.md](docs/glossary.md)

### Contribuir
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [docs/testing.md](docs/testing.md)
- [docs/plugins.md](docs/plugins.md)
- [docs/decisions.md](docs/decisions.md)
- [CHANGELOG.md](CHANGELOG.md)

### Desplegar
- [docs/deployment.md](docs/deployment.md)
- [SECURITY.md](SECURITY.md)

### Entrenar modelos
- [docs/training.md](docs/training.md)

### Para agentes IA
- [AGENTS.md](AGENTS.md)

## 3. Flujo del desarrollador

1. Leer README.md, AGENTS.md, docs/architecture.md.
2. Elegir issue del roadmap o abrir uno nuevo.
3. `git checkout -b feat/mi-aporte`.
4. Si es decisión arquitectónica → ADR en docs/decisions.md.
5. Implementar siguiendo docs/plugins.md.
6. Escribir tests siguiendo docs/testing.md.
7. Añadir entrada en CHANGELOG.md [Unreleased].
8. Ejecutar `ruff check . && pytest -v`.
9. Commit con Conventional Commits, push, abrir PR.
10. Review por maintainer, merge a main.

## 4. Flujo del agente IA

1. Leer AGENTS.md primero.
2. Consultar docs/decisions.md antes de cambios estructurales.
3. Seguir docs/testing.md y docs/plugins.md.
4. Actualizar CHANGELOG.md en cada PR.
5. Ejecutar `ruff check . && pytest -v` antes de declarar éxito.
6. Nunca `git push` sin autorización.
7. Nunca acciones ofensivas fuera del perímetro.

## 5. Fases del proyecto

- ✅ Fase 0 — Bootstrap (completada).
- 🟡 Fase 1 — MVP estable (actual).
- 🔵 Fase 2 — Detección con ML.
- 🟣 Fase 3 — Políticas adaptativas (RL).
- 🟢 Fase 4 — Integraciones.
- 🔴 Fase 5 — Producción.

## 6. Convenciones

### Ramas
- `main`, `feat/*`, `fix/*`, `docs/*`, `chore/*`, `test/*`, `security/*`.

### Commits (Conventional Commits)
- `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`, `security:`

### Versionado (SemVer)
`MAJOR.MINOR.PATCH`.

## 7. Estructura del código

```
src/bladerunner/
├── core/       → clases base
├── sensors/    → sensores
├── detectors/  → detectores
├── actuators/  → actuadores
├── api/        → API REST
└── cli.py      → CLI
```

## 8. Primeros pasos

```bash
git clone git@github.com:W4llker/bladerunner-project.git
cd bladerunner-project
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
ruff check . && pytest -v
python examples/run_demo.py
```
