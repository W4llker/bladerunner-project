# AGENTS.md — Guía para agentes IA que trabajen en Bladerunner

## 1. Contexto

Bladerunner es un framework de ciberseguridad defensiva. Lee primero
README.md, MASTER_WORKFLOW.md y docs/architecture.md.

## 2. Estructura

```
src/bladerunner/
├── core/       → Event, Sensor, Detector, Actuator, Orchestrator
├── sensors/    → implementaciones de sensores
├── detectors/  → implementaciones de detectores
├── actuators/  → implementaciones de actuadores
├── api/        → API REST (FastAPI)
└── cli.py      → CLI (Typer)
```

## 3. Convenciones obligatorias

### Código
- Python 3.10+, tipado estricto en funciones públicas.
- Formato: `ruff format`. Lint: `ruff check`. Tests: `pytest`.
- Un componente = un archivo + un test.
- No añadir dependencias sin justificar en el PR.
- Modelos ML se cargan en `__init__`, nunca en `evaluate`.

### Documentación
- Decisiones arquitectónicas → ADR en docs/decisions.md antes de implementar.
- Cada PR añade entrada en CHANGELOG.md bajo [Unreleased].
- Cada feature se documenta en docs/.

### Git
- Ramas: `feat/`, `fix/`, `docs/`, `chore/`, `test/`, `security/`.
- Commits: Conventional Commits.
- Nunca `git push` sin autorización.
- Nunca commitear secretos, `.env`, `.ai/` ni datos.

## 4. Flujo al añadir una feature

1. Leer docs/architecture.md y docs/decisions.md.
2. Si afecta a más de un módulo → crear ADR.
3. Implementar siguiendo clases base en core/.
4. Escribir tests siguiendo docs/testing.md.
5. Añadir entrada en CHANGELOG.md.
6. Actualizar docs/ si aplica.
7. Ejecutar `ruff check . && pytest -v`.

## 5. Flujo al añadir un componente

Sigue docs/plugins.md. Checklist:
- [ ] Hereda de clase base.
- [ ] Tiene `name` único.
- [ ] Maneja errores sin propagar excepciones.
- [ ] Tiene test unitario.
- [ ] Registrado en cli.py si aplica.
- [ ] Documentado en docs/architecture.md.
- [ ] `ruff check .` y `pytest -v` pasan.

## 6. Reglas de seguridad (no negociables)

- Nunca acciones ofensivas fuera del perímetro.
- Nunca `enforce` sin probar en `monitor`.
- Nunca commitear secretos.
- Nunca deshabilitar `monitor` por defecto.
- Nunca "hackback".
- Preferir reversibles sobre destructivas.
- Auditar toda acción ejecutada.

## 7. Si no sabes qué hacer

1. Consulta docs/roadmap.md.
2. Busca issues con `good first issue`.
3. Abre un issue describiendo la duda.
4. Ante ambigüedad, elige la opción más conservadora y defensiva.
