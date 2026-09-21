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
