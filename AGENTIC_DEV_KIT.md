# AGENTIC_DEV_KIT.md — Fase B: Andamiaje agéntico

## 🎯 Instrucciones para el agente IA

Este documento **extiende `BUILD_INSTRUCTIONS.md`**. Asume que el MVP ya está construido y verificado.

Debes crear los archivos listados a continuación en sus rutas exactas, respetando el contenido literal. Al terminar, ejecuta la verificación de la FASE B-10.

**Reglas:**
- No improvises contenido.
- No modifiques archivos existentes salvo los indicados explícitamente en B-9.
- Si un archivo ya existe, sobrescríbelo solo si se indica.
- Reporta al final un resumen de lo creado.

---

## FASE B-1 — `TASKS.md`

**Ruta:** `TASKS.md` (raíz)

```markdown
# TASKS.md — Backlog vivo de Bladerunner

> **Instrucciones para el agente IA:** este es tu backlog. Al inicio de cada
> sesión, busca la sección **"🎯 Tarea actual"** y trabaja en ella. Al
> terminarla, muévela a **"✅ Completadas"** y promueve la siguiente de
> **"📋 Pendientes"** a **"🎯 Tarea actual"**.
>
> Formato de cada tarea:
> ```
> ### [TASK-NNN] Título corto
> - **Tipo:** feature | bugfix | docs | refactor | test | chore | security
> - **Milestone:** v0.2 | v0.3 | ...
> - **Prioridad:** alta | media | baja
> - **Esfuerzo:** S (horas) | M (días) | L (semanas)
> - **Depende de:** [TASK-XXX] (opcional)
> - **Descripción:** qué hay que hacer.
> - **Criterios de aceptación:** lista verificable.
> - **Documentos a actualizar:** CHANGELOG.md, docs/X.md, etc.
> ```

---

## 🎯 Tarea actual

### [TASK-001] Sensor de red (network_sensor.py)
- **Tipo:** feature
- **Milestone:** v0.2
- **Prioridad:** alta
- **Esfuerzo:** M
- **Depende de:** —
- **Descripción:** crear `src/bladerunner/sensors/network_sensor.py` que
  monitorice las conexiones de red salientes de un proceso y emita `Event`s
  con dominios/IPs visitadas, puertos y volumen de tráfico.
- **Criterios de aceptación:**
  - [ ] Archivo creado en la ruta correcta.
  - [ ] Hereda de `BaseSensor`.
  - [ ] Tiene `name = "network_sensor"`.
  - [ ] Emite eventos con `kind=EventKind.NETWORK`.
  - [ ] Test unitario en `tests/test_network_sensor.py` con al menos 3 casos.
  - [ ] Registrado en `cli.py::watch` como opción `--network`.
  - [ ] Documentado en `docs/architecture.md`.
- **Documentos a actualizar:** `CHANGELOG.md`, `docs/architecture.md`, `TASKS.md`.

---

## 📋 Pendientes (ordenadas por prioridad)

### [TASK-002] Actuador de aislamiento (isolation_actuator.py)
- **Tipo:** feature
- **Milestone:** v0.2
- **Prioridad:** alta
- **Esfuerzo:** M
- **Depende de:** TASK-001
- **Descripción:** crear `src/bladerunner/actuators/isolation_actuator.py`
  que aísle un proceso bloqueando su tráfico saliente vía `iptables` (Linux)
  o `pfctl` (macOS). Debe ser reversible.
- **Criterios de aceptación:**
  - [ ] Hereda de `BaseActuator`.
  - [ ] Implementa `execute()` y `revert()` (idempotente).
  - [ ] Detecta el SO y usa la herramienta correcta.
  - [ ] Fallback seguro si no hay permisos.
  - [ ] Test unitario con mock de subprocess.
  - [ ] Documentado en `docs/plugins.md` como ejemplo avanzado.
- **Documentos a actualizar:** `CHANGELOG.md`, `docs/architecture.md`.

### [TASK-003] Persistencia SQLite
- **Tipo:** feature
- **Milestone:** v0.2
- **Prioridad:** media
- **Esfuerzo:** M
- **Depende de:** —
- **Descripción:** añadir capa de persistencia con SQLite para eventos,
  veredictos y acciones. Usar SQLModel o SQLAlchemy.
- **Criterios de aceptación:**
  - [ ] Módulo `src/bladerunner/core/storage.py`.
  - [ ] Tablas: `events`, `verdicts`, `actions`.
  - [ ] Orquestador persiste cada acción ejecutada.
  - [ ] Tests de integración con SQLite en memoria.
- **Documentos a actualizar:** `CHANGELOG.md`, `docs/architecture.md`.

### [TASK-004] API REST completa
- **Tipo:** feature
- **Milestone:** v0.2
- **Prioridad:** media
- **Esfuerzo:** M
- **Depende de:** TASK-003
- **Descripción:** ampliar `src/bladerunner/api/main.py` con endpoints:
  `GET /events`, `GET /verdicts`, `GET /actions`, `GET /stats`,
  `POST /agents/{id}/kill`, `POST /agents/{id}/isolate`.
- **Criterios de aceptación:**
  - [ ] Endpoints implementados con Pydantic models.
  - [ ] Documentación automática en `/docs`.
  - [ ] Tests de integración con TestClient.
  - [ ] Actualizar `docs/api_reference.md`.
- **Documentos a actualizar:** `CHANGELOG.md`, `docs/api_reference.md`.

### [TASK-005] Detector ML — Random Forest
- **Tipo:** feature
- **Milestone:** v0.3
- **Prioridad:** media
- **Esfuerzo:** L
- **Depende de:** —
- **Descripción:** implementar `src/bladerunner/detectors/ml.py` con
  `RandomForestDetector` que cargue un modelo entrenado y evalúe eventos.
- **Criterios de aceptación:**
  - [ ] Clase `RandomForestDetector(BaseDetector)`.
  - [ ] Carga modelo en `__init__`, no en `evaluate`.
  - [ ] Test unitario con modelo dummy.
  - [ ] Script `scripts/train_baseline.py` que entrene con NSL-KDD.
  - [ ] Documentado en `docs/training.md`.
- **Documentos a actualizar:** `CHANGELOG.md`, `docs/training.md`.

### [TASK-006] Dashboard web mínimo (HTMX)
- **Tipo:** feature
- **Milestone:** v0.2
- **Prioridad:** baja
- **Esfuerzo:** M
- **Depende de:** TASK-004
- **Descripción:** crear dashboard web simple con HTMX + Jinja2 que muestre
  eventos, veredictos y acciones en tiempo real.
- **Criterios de aceptación:**
  - [ ] Ruta `/dashboard` en FastAPI.
  - [ ] Tabla auto-actualizable cada 5s.
  - [ ] Sin dependencias JS pesadas.
- **Documentos a actualizar:** `CHANGELOG.md`, `README.md`.

### [TASK-007] Humano en el circuito (webhook de aprobación)
- **Tipo:** feature
- **Milestone:** v0.2
- **Prioridad:** media
- **Esfuerzo:** M
- **Depende de:** TASK-002
- **Descripción:** añadir modo `approval` donde las acciones destructivas
  (ISOLATE, KILL) requieren aprobación manual vía webhook.
- **Criterios de aceptación:**
  - [ ] Nuevo modo `approval` en `Orchestrator`.
  - [ ] Envía webhook con payload de la acción propuesta.
  - [ ] Espera respuesta con timeout configurable.
  - [ ] Documentar en `docs/architecture.md`.
- **Documentos a actualizar:** `CHANGELOG.md`, `docs/architecture.md`.

### [TASK-008] Cobertura de tests >80%
- **Tipo:** test
- **Milestone:** v0.2
- **Prioridad:** alta
- **Esfuerzo:** M
- **Depende de:** —
- **Descripción:** añadir tests faltantes hasta alcanzar la cobertura
  objetivo definida en `docs/testing.md`.
- **Criterios de aceptación:**
  - [ ] `pytest --cov=src/bladerunner` reporta >80% global.
  - [ ] `core/` >90%, `detectors/` >85%, `sensors/` >80%.
  - [ ] CI bloquea PRs que bajen la cobertura.
- **Documentos a actualizar:** `CHANGELOG.md`.

### [TASK-009] Documentación de ejemplos avanzados
- **Tipo:** docs
- **Milestone:** v0.2
- **Prioridad:** baja
- **Esfuerzo:** S
- **Depende de:** —
- **Descripción:** añadir `examples/` con casos de uso reales:
  vigilancia de un bot de Discord, contención de un script de scraping,
  monitorización de un agente LLM con LangChain.
- **Criterios de aceptación:**
  - [ ] 3 ejemplos funcionales en `examples/`.
  - [ ] Cada uno con su README.
  - [ ] Documentados en `README.md`.
- **Documentos a actualizar:** `README.md`, `CHANGELOG.md`.

### [TASK-010] Auditoría de seguridad interna
- **Tipo:** security
- **Milestone:** v0.2
- **Prioridad:** alta
- **Esfuerzo:** M
- **Depende de:** —
- **Descripción:** revisar todos los puntos de ejecución de comandos
  (`subprocess`, `os.system`) y garantizar que no hay inyección posible.
- **Criterios de aceptación:**
  - [ ] Lista de puntos de ejecución en `docs/security_review.md`.
  - [ ] Todos usan argumentos como lista, no strings.
  - [ ] Sin `shell=True` salvo justificación explícita.
  - [ ] Añadir test de regresión para cada punto crítico.
- **Documentos a actualizar:** `docs/security_review.md` (nuevo), `CHANGELOG.md`.

---

## ✅ Completadas

(vacío por ahora)

---

## 🚫 Descartadas / Bloqueadas

(vacío por ahora)

---

## 📝 Cómo actualizar este archivo

1. Al terminar la "Tarea actual":
   - Moverla a "✅ Completadas" con la fecha de fin.
   - Marcar todos los criterios de aceptación con `[x]`.
2. Promover la siguiente tarea de "📋 Pendientes" a "🎯 Tarea actual".
3. Si una tarea nueva surge durante el desarrollo, añadirla a "📋 Pendientes"
   con el formato estándar.
4. Si una tarea se bloquea, moverla a "🚫 Descartadas / Bloqueadas" con
   la razón.

## 🔄 Regla de oro

**Nunca trabajes en dos tareas a la vez.** Termina, verifica, documenta,
cierra, y solo entonces pasa a la siguiente.
```

---

## FASE B-2 — `DEFINITION_OF_DONE.md`

**Ruta:** `DEFINITION_OF_DONE.md` (raíz)

```markdown
# DEFINITION_OF_DONE.md — Criterios de "terminado"

> **Instrucciones para el agente IA:** una tarea está terminada **solo si
> cumple TODOS los criterios de su tipo**. Si falta uno, la tarea no está
> terminada. No la muevas a "✅ Completadas" hasta cumplirlos todos.

---

## Criterios por tipo de tarea

### 🟢 Feature (nueva funcionalidad)

- [ ] Código implementado en la ruta correcta.
- [ ] Hereda de la clase base correspondiente (si aplica).
- [ ] Tiene `name` único (si es componente).
- [ ] Maneja errores sin propagar excepciones al orquestador.
- [ ] Test unitario con al menos 3 casos (éxito, fallo, borde).
- [ ] Test de integración si afecta al flujo sensor→detector→actuador.
- [ ] Registrado en `cli.py` si debe usarse por defecto.
- [ ] Documentado en `docs/architecture.md` o `docs/plugins.md`.
- [ ] Entrada en `CHANGELOG.md` bajo `[Unreleased] / Added`.
- [ ] `ruff check .` pasa.
- [ ] `pytest -v` pasa.
- [ ] Cobertura global no baja.
- [ ] Tarea movida a "✅ Completadas" en `TASKS.md`.

### 🔴 Bugfix

- [ ] Bug reproducido con un test de regresión (falla antes del fix).
- [ ] Fix implementado.
- [ ] Test de regresión ahora pasa.
- [ ] No se rompen otros tests.
- [ ] Causa raíz documentada en el PR.
- [ ] Entrada en `CHANGELOG.md` bajo `[Unreleased] / Fixed`.
- [ ] `ruff check .` y `pytest -v` pasan.
- [ ] Tarea movida a "✅ Completadas" en `TASKS.md`.

### 📚 Docs (solo documentación)

- [ ] Contenido escrito con ejemplos ejecutables cuando aplique.
- [ ] Enlaces internos verificados (sin links roscos).
- [ ] Ortografía y gramática revisadas.
- [ ] Si describe comportamiento, coincide con el código actual.
- [ ] Entrada en `CHANGELOG.md` bajo `[Unreleased] / Changed` o `Added`.
- [ ] Tarea movida a "✅ Completadas" en `TASKS.md`.

### ♻️ Refactor

- [ ] Sin cambios funcionales (tests existentes siguen pasando sin cambios).
- [ ] Si cambia comportamiento, se trata como feature.
- [ ] Cobertura de tests no baja.
- [ ] Documentación actualizada si aplica.
- [ ] Entrada en `CHANGELOG.md` bajo `[Unreleased] / Changed`.
- [ ] `ruff check .` y `pytest -v` pasan.
- [ ] Tarea movida a "✅ Completadas" en `TASKS.md`.

### 🧪 Test (solo tests)

- [ ] Tests añadidos cubren el caso especificado.
- [ ] Cobertura global sube o se mantiene.
- [ ] No se modifican tests existentes para "hacerlos pasar".
- [ ] Si el test descubre un bug, se abre un issue o una nueva tarea.
- [ ] Entrada en `CHANGELOG.md` si aporta valor visible.
- [ ] Tarea movida a "✅ Completadas" en `TASKS.md`.

### 🔧 Chore (mantenimiento)

- [ ] Cambio mínimo y localizado.
- [ ] No rompe build, lint ni tests.
- [ ] Documentado en el PR si afecta a otros contribuidores.
- [ ] Tarea movida a "✅ Completadas" en `TASKS.md`.

### 🔒 Security

- [ ] Vulnerabilidad identificada y documentada.
- [ ] Fix implementado con test de regresión.
- [ ] Aviso a maintainers si es crítica (ver `SECURITY.md`).
- [ ] Entrada en `CHANGELOG.md` bajo `[Unreleased] / Security`.
- [ ] Tarea movida a "✅ Completadas" en `TASKS.md`.

---

## Criterios transversales (aplican a TODO tipo)

- [ ] Rama con nombre correcto (`feat/`, `fix/`, `docs/`, etc.).
- [ ] Commits con Conventional Commits.
- [ ] PR abierto con la plantilla completa.
- [ ] CI (GitHub Actions) pasa en verde.
- [ ] Al menos un revisor asignado (o self-review con checklist marcada).
- [ ] Sin `TODO` sin issue asociado.
- [ ] Sin secretos, `.env`, `.ai/` ni datos personales en el diff.
- [ ] Sin código comentado "por si acaso".
- [ ] Sin dependencias nuevas sin justificar en el PR.

---

## Anti-criterios (la tarea NO está terminada si...)

- ❌ El test "pasa" pero no prueba realmente lo que dice probar.
- ❌ Se silencia un error con `try/except: pass`.
- ❌ Se añade `# type: ignore` sin justificación.
- ❌ Se baja la cobertura global.
- ❌ Se comenta código sin issue que lo rastree.
- ❌ Se hace `git push --force` a `main`.
- ❌ Se mergea sin CI verde.
- ❌ Se mergea sin actualizar `CHANGELOG.md`.
- ❌ Se mergea sin actualizar `TASKS.md`.
- ❌ Se deja el modo `enforce` como default.

---

## Regla final

**Cuando dudes, pregúntate:** "¿si otro contribuidor clona el repo mañana,
entiende qué se hizo, por qué, y puede verificarlo?" Si la respuesta es no,
la tarea no está terminada.
```

---

## FASE B-3 — `.github/pull_request_template.md`

**Ruta:** `.github/pull_request_template.md`

```markdown
## ¿Qué hace este PR?

<!-- Descripción breve y clara. Una o dos frases. -->

## ¿Por qué?

<!-- Contexto: qué problema resuelve, qué issue cierra. -->

Closes #<!-- número de issue -->

## Tipo de cambio

<!-- Marca con [x] lo que aplique. -->

- [ ] 🟢 Feature (nueva funcionalidad)
- [ ] 🔴 Bugfix (corrección de bug)
- [ ] 📚 Docs (solo documentación)
- [ ] ♻️ Refactor (sin cambio funcional)
- [ ] 🧪 Test (solo tests)
- [ ] 🔧 Chore (mantenimiento)
- [ ] 🔒 Security (parche de seguridad)

## Checklist (Definition of Done)

Ver [DEFINITION_OF_DONE.md](../DEFINITION_OF_DONE.md) para criterios completos.

- [ ] Código implementado en la ruta correcta.
- [ ] Tests añadidos o actualizados.
- [ ] `ruff check .` pasa.
- [ ] `pytest -v` pasa.
- [ ] Cobertura global no baja.
- [ ] `CHANGELOG.md` actualizado bajo `[Unreleased]`.
- [ ] `TASKS.md` actualizado (tarea movida a "✅ Completadas").
- [ ] Documentación actualizada (`docs/*.md`, `README.md`, etc.) si aplica.
- [ ] Sin secretos, `.env`, `.ai/` ni datos personales en el diff.
- [ ] Sin dependencias nuevas sin justificar.

## Cómo probar

<!-- Pasos exactos para que un revisor reproduzca el cambio. -->

```bash
# Ejemplo
make test
python examples/run_demo.py
```

## Capturas / logs (si aplica)

<!-- Opcional: capturas, logs, salidas de consola. -->

## Notas para el revisor

<!-- Opcional: decisiones tomadas, dudas, alternativas descartadas. -->
```

---

## FASE B-4 — Plantillas de issues

### `.github/ISSUE_TEMPLATE/feature.md`

**Ruta:** `.github/ISSUE_TEMPLATE/feature.md`

```markdown
---
name: 🟢 Feature request
about: Proponer una nueva funcionalidad
title: "[FEAT] "
labels: ["enhancement", "triage"]
---

## ¿Qué problema resuelve?

<!-- Describe el problema o necesidad. -->

## Solución propuesta

<!-- Cómo imaginas la solución. -->

## Alternativas consideradas

<!-- Otras opciones que hayas pensado. -->

## Criterios de aceptación

<!-- Lista verificable de qué debe cumplirse. -->

- [ ] ...
- [ ] ...

## ¿Requiere ADR?

<!-- Marca si afecta a más de un módulo, cambia el stack o es difícil de revertir. -->

- [ ] Sí → crear ADR en `docs/decisions.md` antes de implementar.
- [ ] No.

## Contexto adicional

<!-- Referencias, ejemplos, screenshots. -->
```

### `.github/ISSUE_TEMPLATE/bug.md`

**Ruta:** `.github/ISSUE_TEMPLATE/bug.md`

```markdown
---
name: 🔴 Bug report
about: Reportar un comportamiento incorrecto
title: "[BUG] "
labels: ["bug", "triage"]
---

## Descripción

<!-- Qué ocurre y qué se esperaba que ocurriera. -->

## Pasos para reproducir

1. ...
2. ...
3. ...

## Comportamiento esperado

<!-- Qué debería pasar. -->

## Comportamiento observado

<!-- Qué pasa realmente. Incluye el error completo. -->

```
# Stacktrace / logs
```

## Entorno

- SO: <!-- ej. Ubuntu 22.04 -->
- Python: <!-- ej. 3.11.5 -->
- Bladerunner: <!-- ej. 0.1.0 -->
- Modo: <!-- monitor | enforce -->

## ¿Reproducible siempre?

- [ ] Siempre
- [ ] Intermitente
- [ ] Solo una vez

## Contexto adicional

<!-- Configuración, dependencias, cualquier cosa relevante. -->
```

### `.github/ISSUE_TEMPLATE/docs.md`

**Ruta:** `.github/ISSUE_TEMPLATE/docs.md`

```markdown
---
name: 📚 Documentation
about: Mejorar o añadir documentación
title: "[DOCS] "
labels: ["documentation", "triage"]
---

## ¿Qué documentación falta o está mal?

<!-- Ruta del archivo o sección. -->

## ¿Qué debería decir?

<!-- Descripción del contenido correcto. -->

## Contexto

<!-- Por qué importa, quién lo necesita. -->
```

### `.github/ISSUE_TEMPLATE/config.yml`

**Ruta:** `.github/ISSUE_TEMPLATE/config.yml`

```yaml
blank_issues_enabled: false
contact_links:
  - name: 🛡️ Reportar vulnerabilidad de seguridad
    url: https://github.com/TU_USUARIO/bladerunner-project/security/advisories/new
    about: NO abras un issue público. Ver SECURITY.md.
  - name: 💬 Discusiones
    url: https://github.com/TU_USUARIO/bladerunner-project/discussions
    about: Preguntas abiertas, ideas, mostrar tu setup.
```

---

## FASE B-5 — `.pre-commit-config.yaml`

**Ruta:** `.pre-commit-config.yaml`

```yaml
# Pre-commit hooks para Bladerunner
# Instalación: pre-commit install
# Ejecutar manualmente: pre-commit run --all-files

repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-toml
      - id: check-added-large-files
        args: ["--maxkb=500"]
      - id: check-merge-conflict
      - id: detect-private-key

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.10
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.10.0
    hooks:
      - id: mypy
        additional_dependencies:
          - pydantic>=2.6
          - types-psutil
        args: [--ignore-missing-imports]
        exclude: ^(tests/|examples/|scripts/)
```

---

## FASE B-6 — `Makefile`

**Ruta:** `Makefile`

```makefile
.PHONY: help install install-dev lint format test test-cov demo api docker clean pre-commit pre-commit-install

help:  ## Muestra esta ayuda
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Instala el paquete en modo editable
	pip install -e .

install-dev:  ## Instala con dependencias de desarrollo
	pip install -e ".[dev]"

install-ml:  ## Instala con dependencias de ML
	pip install -e ".[dev,ml]"

lint:  ## Ejecuta ruff check
	ruff check .

format:  ## Formatea con ruff
	ruff format .

test:  ## Ejecuta los tests
	pytest -v

test-cov:  ## Tests con cobertura
	pytest --cov=src/bladerunner --cov-report=term-missing --cov-report=html

demo:  ## Ejecuta la demo end-to-end
	python examples/run_demo.py

api:  ## Levanta la API REST
	uvicorn bladerunner.api.main:app --reload

docker:  ## Levanta con Docker Compose
	docker compose up --build

pre-commit-install:  ## Instala los hooks de pre-commit
	pre-commit install

pre-commit:  ## Ejecuta pre-commit en todos los archivos
	pre-commit run --all-files

clean:  ## Limpia artefactos de build y caches
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .ruff_cache -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ .coverage htmlcov/
```

---

## FASE B-7 — `tests/e2e/test_demo.py`

**Ruta:** `tests/e2e/test_demo.py`

```python
"""Test end-to-end: verifica que la demo funciona de punta a punta.

Este test lanza el agente simulado, ejecuta Bladerunner en modo enforce
con un timeout corto, y verifica que el agente es terminado.
"""

from __future__ import annotations

import asyncio
import subprocess
import sys
from pathlib import Path

import pytest

from bladerunner.actuators.log_only import LogOnlyActuator
from bladerunner.actuators.process_killer import ProcessKillerActuator
from bladerunner.core.events import ActionKind
from bladerunner.core.orchestrator import Orchestrator
from bladerunner.detectors.rule_based import RuleBasedDetector
from bladerunner.sensors.process_sensor import ProcessSensor

AGENT_SCRIPT = Path(__file__).parent.parent.parent / "examples" / "simulated_agent.py"


async def _run_e2e(timeout: float = 20.0) -> bool:
    """Lanza el agente simulado y Bladerunner. Devuelve True si lo mata."""
    assert AGENT_SCRIPT.exists(), f"Falta {AGENT_SCRIPT}"

    proc = subprocess.Popen([sys.executable, str(AGENT_SCRIPT)])
    agent_id = "e2e-agent"

    sensor = ProcessSensor(pid=proc.pid, agent_id=agent_id, interval=0.3)
    detectors = [RuleBasedDetector()]

    def resolve(agent: str) -> int | None:
        return proc.pid if agent == agent_id else None

    actuators = {
        ActionKind.LOG: LogOnlyActuator(),
        ActionKind.ALERT: LogOnlyActuator(),
        ActionKind.KILL: ProcessKillerActuator(pid_resolver=resolve),
        ActionKind.ISOLATE: LogOnlyActuator(),
        ActionKind.RESTRICT: LogOnlyActuator(),
    }

    orch = Orchestrator(
        sensors=[sensor],
        detectors=detectors,
        actuators=actuators,
        mode="enforce",
    )

    try:
        await asyncio.wait_for(orch.run(), timeout=timeout)
    except asyncio.TimeoutError:
        pass
    finally:
        # Verificar si el proceso sigue vivo
        still_alive = proc.poll() is None
        if still_alive:
            proc.terminate()
            try:
                proc.wait(timeout=3)
            except subprocess.TimeoutExpired:
                proc.kill()

    # El test pasa si el proceso fue terminado por Bladerunner
    return not still_alive


@pytest.mark.e2e
def test_demo_kills_rogue_agent() -> None:
    """El agente simulado debe ser terminado por Bladerunner."""
    killed = asyncio.run(_run_e2e(timeout=20.0))
    assert killed, "Bladerunner no mató al agente simulado en 20s"
```

### `pytest.ini` o añadir marca en `pyproject.toml`

**Modificar** `pyproject.toml` (sección `[tool.pytest.ini_options]`) para añadir:

```toml
markers = [
    "e2e: test end-to-end (lento, lanza subprocesos)",
]
```

---

## FASE B-8 — `docs/agent_workflow.md`

**Ruta:** `docs/agent_workflow.md`

```markdown
# agent_workflow.md — Cómo trabaja un agente IA en este repositorio

Esta guía define el flujo operativo que debe seguir **cualquier agente IA**
(Claude Code, Cursor, Cline, Aider, Continue, etc.) al trabajar en Bladerunner.

Si eres un agente IA, sigue estos pasos **en orden** en cada sesión.

---

## Paso 0 — Preparación (solo la primera vez)

1. Verifica que el repo está clonado y el entorno virtual activo.
2. Ejecuta `make install-dev` para instalar dependencias.
3. Ejecuta `make pre-commit-install` para instalar los hooks.
4. Verifica con `make test` que todos los tests pasan.

---

## Paso 1 — Orientación

Al inicio de CADA sesión:

1. Lee `AGENTS.md` completo.
2. Lee `MASTER_WORKFLOW.md` para el contexto general.
3. Lee `TASKS.md` y localiza la sección **"🎯 Tarea actual"**.
4. Lee `DEFINITION_OF_DONE.md` para saber cuándo la tarea estará terminada.
5. Si la tarea involucra un componente nuevo, lee `docs/plugins.md`.
6. Si la tarea involucra tests, lee `docs/testing.md`.
7. Si la tarea involucra una decisión arquitectónica, lee `docs/decisions.md`.

**Salida esperada:** sabes exactamente en qué tarea vas a trabajar y cuáles
son los criterios de aceptación.

---

## Paso 2 — Preparación de la rama

```bash
# Actualiza main
git checkout main
git pull origin main

# Crea rama según el tipo de tarea
git checkout -b feat/task-NNN-descripcion-corta
# o fix/, docs/, chore/, test/, security/ según corresponda
```

---

## Paso 3 — Implementación

1. Si la tarea requiere una decisión arquitectónica:
   - Añade una ADR en `docs/decisions.md` con estado `propuesta`.
2. Implementa el código siguiendo las convenciones de `AGENTS.md`.
3. Añade tests siguiendo `docs/testing.md`.
4. Añade entrada en `CHANGELOG.md` bajo `[Unreleased]` en la categoría correcta.
5. Actualiza la documentación en `docs/` si aplica.

---

## Paso 4 — Verificación local

Ejecuta en orden:

```bash
make lint         # ruff check
make test-cov     # pytest con cobertura
make demo         # demo end-to-end (opcional pero recomendado)
```

**Criterios de paso:**
- [ ] `make lint` pasa sin errores.
- [ ] `make test-cov` pasa y la cobertura no bajó.
- [ ] `make demo` funciona si la tarea afecta al flujo principal.

Si algo falla, **arregla antes de continuar**. No acumules errores.

---

## Paso 5 — Actualizar TASKS.md

1. Marca todos los criterios de aceptación de la tarea con `[x]`.
2. Mueve la tarea de **"🎯 Tarea actual"** a **"✅ Completadas"**.
3. Añade la fecha de fin: `(completada YYYY-MM-DD)`.
4. Promueve la siguiente tarea de **"📋 Pendientes"** a **"🎯 Tarea actual"**.

---

## Paso 6 — Commit

```bash
git add .
git commit -m "feat(task-NNN): descripción corta

- Punto 1 del cambio
- Punto 2 del cambio

Cierra #NNN"
```

**Reglas:**
- Usa Conventional Commits.
- Una línea de asunto de <72 caracteres.
- Cuerpo con detalles si es necesario.
- Referencia el issue con `Closes #NNN` o `Refs #NNN`.

**Los hooks de pre-commit se ejecutan automáticamente.** Si fallan,
arréglalos y repite el commit.

---

## Paso 7 — Push y PR

```bash
git push origin feat/task-NNN-descripcion-corta
```

Abre un PR en GitHub **usando la plantilla** (se carga automáticamente).
Rellena todos los campos.

**Espera a que CI pase.** Si falla, arregla y vuelve a hacer push.

---

## Paso 8 — Reporte al usuario

Al terminar la sesión, reporta:

```
=== Sesión de trabajo — Bladerunner ===

Tarea completada: [TASK-NNN] Título
Rama: feat/task-NNN-descripcion
PR: #NNN (URL)

Cambios:
  - Archivos modificados: N
  - Tests añadidos: N
  - Cobertura: X% (antes Y%)

Verificación:
  - make lint: PASS
  - make test-cov: PASS
  - make demo: PASS

Próxima tarea: [TASK-NNN+1] Título

Dudas / bloqueos:
  - (ninguno)
```

---

## Reglas especiales

### Si encuentras un bug mientras trabajas en otra cosa

1. Abre un issue con la plantilla de bug.
2. Añade una tarea nueva en `TASKS.md` en "📋 Pendientes".
3. **No arregles el bug en la rama actual.** Termina la tarea en curso.

### Si la tarea es demasiado grande (>1 día de trabajo)

1. Divide la tarea en subtareas en `TASKS.md`.
2. Trabaja en una subtarea a la vez.
3. Marca la tarea original como "🚫 Bloqueada hasta que se completen las subtareas".

### Si la tarea requiere una decisión arquitectónica

1. Detente.
2. Escribe una ADR en `docs/decisions.md` con estado `propuesta`.
3. Pregunta al usuario antes de implementar.
4. No sigas hasta tener aprobación.

### Si no sabes qué hacer

1. Consulta `TASKS.md`, `docs/roadmap.md`, `docs/decisions.md`.
2. Si sigue sin estar claro, **detente y pregunta al usuario**.
3. **Nunca improvises** una solución no especificada.

### Si rompes algo

1. No entres en pánico.
2. Identifica qué rompiste: `git diff`, `git log`.
3. Si no puedes arreglarlo en 15 minutos, revierte:
   ```bash
   git checkout main
   git branch -D feat/task-NNN-descripcion
   ```
4. Reporta al usuario qué pasó.

---

## Anti-patrones (lo que NUNCA debes hacer)

- ❌ Trabajar en dos tareas a la vez.
- ❌ Commitear sin tests.
- ❌ Commitear sin actualizar `CHANGELOG.md` y `TASKS.md`.
- ❌ Silenciar errores con `try/except: pass`.
- ❌ Bajar la cobertura de tests.
- ❌ Añadir dependencias sin justificar.
- ❌ Hacer `git push --force` a `main`.
- ❌ Modificar `.ai/` o `.env`.
- ❌ Modo `enforce` por defecto.
- ❌ Ejecutar acciones ofensivas fuera del perímetro.
- ❌ Improvisar cuando hay ambigüedad.

---

## Ciclo completo (resumen visual)

```
┌──────────────────────────────────────────────────────┐
│ 1. Orientación                                       │
│    AGENTS.md → MASTER_WORKFLOW.md → TASKS.md → DoD   │
├──────────────────────────────────────────────────────┤
│ 2. Rama                                              │
│    git checkout -b feat/task-NNN-descripcion         │
├──────────────────────────────────────────────────────┤
│ 3. Implementación                                    │
│    código + tests + CHANGELOG + docs                 │
├──────────────────────────────────────────────────────┤
│ 4. Verificación                                      │
│    make lint && make test-cov && make demo           │
├──────────────────────────────────────────────────────┤
│ 5. Actualizar TASKS.md                               │
│    marcar completada, promover siguiente             │
├──────────────────────────────────────────────────────┤
│ 6. Commit                                            │
│    git commit -m "feat(task-NNN): ..."               │
├──────────────────────────────────────────────────────┤
│ 7. Push y PR                                         │
│    git push → abrir PR con plantilla                 │
├──────────────────────────────────────────────────────┤
│ 8. Reporte                                           │
│    resumen al usuario                                │
└──────────────────────────────────────────────────────┘
```
```

---

## FASE B-9 — Actualizar archivos existentes

### B-9.1 — `pyproject.toml`

**Modificar** la sección `[project.optional-dependencies]` para añadir `pre-commit` y actualizar `[tool.pytest.ini_options]`.

Reemplaza:

```toml
[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-asyncio>=0.23",
    "ruff>=0.4",
    "mypy>=1.10",
]
```

Por:

```toml
[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-asyncio>=0.23",
    "pytest-cov>=5.0",
    "ruff>=0.4",
    "mypy>=1.10",
    "pre-commit>=3.7",
]
```

Y reemplaza:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"
```

Por:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"
markers = [
    "e2e: test end-to-end (lento, lanza subprocesos)",
]
```

### B-9.2 — `.gitignore`

**Añadir** al final:

```
# Pre-commit
.pre-commit-config.yaml.bak

# Cobertura
.coverage
htmlcov/
coverage.xml
```

### B-9.3 — `README.md`

**Añadir** una sección antes de "## Licencia":

```markdown
## Desarrollo

```bash
make install-dev       # Instala con dependencias de desarrollo
make pre-commit-install # Instala los hooks de pre-commit
make test-cov          # Tests con cobertura
make lint              # Linting
make demo              # Demo end-to-end
make help              # Ver todos los comandos disponibles
```

Ver [TASKS.md](TASKS.md) para el backlog y [DEFINITION_OF_DONE.md](DEFINITION_OF_DONE.md)
para los criterios de aceptación. Si eres un agente IA, empieza por
[docs/agent_workflow.md](docs/agent_workflow.md).
```

### B-9.4 — `AGENTS.md`

**Añadir** al final del archivo, en la sección "Documentación relacionada":

```markdown
| [TASKS.md](TASKS.md) | Backlog vivo — busca siempre "🎯 Tarea actual" |
| [DEFINITION_OF_DONE.md](DEFINITION_OF_DONE.md) | Cuándo una tarea está terminada |
| [docs/agent_workflow.md](docs/agent_workflow.md) | Flujo operativo completo del agente |
```

### B-9.5 — `CHANGELOG.md`

**Añadir** bajo `[Unreleased] / Added`:

```markdown
- Andamiaje agéntico: `TASKS.md`, `DEFINITION_OF_DONE.md`, plantillas de
  issues y PR, `.pre-commit-config.yaml`, `Makefile`, test e2e y
  `docs/agent_workflow.md`.
```

---

## FASE B-10 — Verificación

Ejecuta en orden:

```bash
# 1. Reinstalar con las nuevas dependencias de dev
pip install -e ".[dev]"

# 2. Instalar pre-commit
pre-commit install

# 3. Ejecutar pre-commit en todos los archivos
pre-commit run --all-files

# 4. Verificar Makefile
make help

# 5. Lint
make lint

# 6. Tests (excluyendo e2e para rapidez)
pytest -v -m "not e2e"

# 7. Test e2e (más lento)
pytest -v -m "e2e"

# 8. Verificar que TASKS.md y DEFINITION_OF_DONE.md existen
test -f TASKS.md && test -f DEFINITION_OF_DONE.md && echo "OK"
```

### Criterios de éxito

- [ ] `pip install -e ".[dev]"` completa sin errores.
- [ ] `pre-commit run --all-files` pasa o corrige automáticamente.
- [ ] `make help` lista todos los comandos.
- [ ] `make lint` pasa.
- [ ] `pytest -m "not e2e"` pasa.
- [ ] `pytest -m e2e` pasa (o está marcado como skip si el entorno no lo permite).
- [ ] `TASKS.md` y `DEFINITION_OF_DONE.md` existen y no están vacíos.

Si algo falla, **detente y reporta el error completo**.

---

## FASE B-11 — Commit final

```bash
git add .
git commit -m "chore: añadir andamiaje agéntico (Fase B)

- TASKS.md con backlog de v0.2
- DEFINITION_OF_DONE.md con criterios de aceptación
- Plantillas de issues y PR
- Pre-commit hooks
- Makefile con comandos comunes
- Test e2e de la demo
- docs/agent_workflow.md con flujo operativo del agente
- Actualización de pyproject.toml, .gitignore, README.md, AGENTS.md, CHANGELOG.md"
```

---

## FASE B-12 — Reporte final

Al terminar, imprime:

```
=== Bladerunner Project — Fase B completada ===

Archivos creados:
  - TASKS.md
  - DEFINITION_OF_DONE.md
  - .github/pull_request_template.md
  - .github/ISSUE_TEMPLATE/feature.md
  - .github/ISSUE_TEMPLATE/bug.md
  - .github/ISSUE_TEMPLATE/docs.md
  - .github/ISSUE_TEMPLATE/config.yml
  - .pre-commit-config.yaml
  - Makefile
  - tests/e2e/test_demo.py
  - docs/agent_workflow.md

Archivos modificados:
  - pyproject.toml (deps + markers)
  - .gitignore (pre-commit, cobertura)
  - README.md (sección Desarrollo)
  - AGENTS.md (referencias nuevas)
  - CHANGELOG.md (entrada Added)

Verificación:
  - pre-commit: [PASS/FAIL]
  - make lint: [PASS/FAIL]
  - pytest (not e2e): [N passed]
  - pytest e2e: [PASS/FAIL/SKIP]

Estado del proyecto:
  ✅ MVP funcional (Fase A)
  ✅ Andamiaje agéntico (Fase B)
  🎯 Listo para desarrollo agéntico sostenido

Próximo paso:
  - El agente debe leer TASKS.md y empezar por [TASK-001].
  - Comando: "lee TASKS.md y trabaja en la tarea actual"
```

---

## 🎯 Reglas finales para el agente

1. **No modifiques archivos fuera de los listados** salvo los indicados en B-9.
2. **Respeta el contenido literal.** No "mejores" los textos.
3. **Ejecuta la verificación completa** antes de reportar éxito.
4. **Si algo falla, detente y reporta.**
5. **Al terminar, haz el commit de B-11** (sin push).
6. **No hagas `git push`** sin autorización explícita.

**Fin de AGENTIC_DEV_KIT.md — Fase B.**