# BUILD_INSTRUCTIONS.md — Construcción completa del repositorio Bladerunner

## 🎯 Instrucciones para el agente IA

Eres un agente encargado de construir el repositorio **Bladerunner Project** desde cero. Debes:

1. **Leer este documento completo antes de actuar.**
2. **Crear cada archivo en la ruta exacta indicada.**
3. **Respetar el contenido literal** de cada archivo. No improvises.
4. **Ejecutar los comandos de verificación** al final.
5. **Reportar al usuario** un resumen de lo creado y el resultado de la verificación.

**Reglas críticas:**
- No añadas dependencias fuera de las especificadas.
- No renombres archivos ni carpetas.
- No hagas `git push` sin autorización explícita.
- Si un comando falla, reporta el error completo y detente.

**Directorio de trabajo:** el actual (donde está este archivo). Todos los comandos se ejecutan desde aquí.

---

## FASE 1 — Crear la estructura de carpetas

Ejecuta exactamente:

```bash
mkdir -p .ai/prompts .github/workflows docs deploy/k8s scripts notebooks \
         src/bladerunner/core src/bladerunner/sensors src/bladerunner/detectors \
         src/bladerunner/actuators src/bladerunner/api examples tests

touch src/bladerunner/__init__.py \
      src/bladerunner/core/__init__.py \
      src/bladerunner/sensors/__init__.py \
      src/bladerunner/detectors/__init__.py \
      src/bladerunner/actuators/__init__.py \
      src/bladerunner/api/__init__.py \
      tests/__init__.py
```

---

## FASE 2 — Crear los archivos de documentación local (`.ai/`)

Estos archivos NO se commitean. Son tus prompts personales.

### Archivo: `.ai/BOOTSTRAP.md`

```markdown
# BOOTSTRAP.md — Prompt de construcción del MVP

> Este prompt se ejecutó para construir la versión 0.1.0 de Bladerunner.
> Guárdalo como referencia histórica. NO se commitea.

## Qué se construyó

- Estructura base del proyecto (sensores, detectores, actuadores, orquestador).
- ProcessSensor, RuleBasedDetector, AnomalyDetector.
- LogOnlyActuator, ProcessKillerActuator.
- CLI con Typer (`bladerunner watch`).
- API REST con FastAPI.
- Demo end-to-end con agente simulado.
- Tests con pytest.
- CI con GitHub Actions.

## Cómo replicarlo

El código fuente vive en `src/bladerunner/`. Si necesitas regenerarlo,
sigue la especificación histórica documentada en `docs/architecture.md`.
```

### Archivo: `.ai/TRAINING.md`

```markdown
# TRAINING.md — Prompt de entrenamiento de modelos ML

> Prompt para entrenar detectores basados en ML.
> Ver también `docs/training.md` (documentación pública del proyecto).

## Fases

1. Descargar datasets (Dendroaspis, CICIDS2017, NSL-KDD).
2. Entrenar baseline (Random Forest, Isolation Forest).
3. Entrenar autoencoder con PyTorch.
4. Integrar como `src/bladerunner/detectors/ml.py`.
5. Evaluar con métricas de `docs/training.md`.
6. Probar en sandbox (OpenShell, Eclipse Enclave).

## Ejecución

```bash
python scripts/download_datasets.py
python scripts/prepare_features.py
python scripts/train_baseline.py
python scripts/train_isolation_forest.py
python scripts/train_autoencoder.py
python scripts/evaluate.py
```
```

---

## FASE 3 — Archivos raíz del proyecto

### Archivo: `README.md`

```markdown
# Bladerunner Project — Open Source Agent Hunter

**Bladerunner** es un framework open source para **detectar, aislar y neutralizar agentes autónomos descontrolados** (LLMs, bots, agentes RL) sin necesidad de inspeccionar su código interno. Funciona como un "caza-agentes": observa el comportamiento externo, decide si es anómalo y aplica contramedidas graduadas.

> ⚠️ Bladerunner es **defensivo por diseño**. No realiza acciones ofensivas fuera de la infraestructura que controlas.

## ¿Por qué?

Con la proliferación de agentes autónomos (LLMs con herramientas, bots de automatización, agentes RL), crece el riesgo de comportamientos no previstos: exfiltración de datos, escalada de privilegios, uso abusivo de recursos. Bladerunner ofrece una capa de vigilancia y contención.

## Arquitectura (MVP)

```
[Agente objetivo] --telemetría--> [Sensor] --> [Detector] --> [Orquestador] --> [Actuador]
                                                                  |
                                                          [Dashboard/Logs]
```

## Instalación rápida

```bash
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Demo

```bash
python examples/run_demo.py
```

## Documentación

- [MASTER_WORKFLOW.md](MASTER_WORKFLOW.md) — Flujo maestro de trabajo.
- [AGENTS.md](AGENTS.md) — Guía para agentes IA.
- [CONTRIBUTING.md](CONTRIBUTING.md) — Cómo contribuir.
- [docs/architecture.md](docs/architecture.md) — Diseño del sistema.
- [docs/roadmap.md](docs/roadmap.md) — Roadmap del proyecto.

## Licencia

Apache 2.0 — ver [LICENSE](LICENSE).
```

### Archivo: `LICENSE`

Copia el texto de Apache 2.0. Comando:

```bash
curl -sSL https://www.apache.org/licenses/LICENSE-2.0.txt -o LICENSE
```

Si no hay red, escribe el encabezado estándar de Apache 2.0.

### Archivo: `MASTER_WORKFLOW.md`

```markdown
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
git clone git@github.com:TU_USUARIO/bladerunner-project.git
cd bladerunner-project
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
ruff check . && pytest -v
python examples/run_demo.py
```
```

### Archivo: `AGENTS.md`

```markdown
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
```

### Archivo: `CONTRIBUTING.md`

```markdown
# Contribuir a Bladerunner

¡Gracias por tu interés!

## Cómo contribuir

1. Lee AGENTS.md, MASTER_WORKFLOW.md y CONTRIBUTING.md.
2. Busca o abre un issue describiendo el cambio.
3. Fork del repo, rama: `git checkout -b feat/mi-aporte`.
4. Implementa siguiendo docs/plugins.md.
5. Escribe tests siguiendo docs/testing.md.
6. Añade entrada en CHANGELOG.md bajo [Unreleased].
7. Ejecuta `ruff check . && pytest -v`.
8. Commit con Conventional Commits.
9. Push a tu fork y abre Pull Request.

## Estilo de código

- Python 3.10+.
- `ruff format` y `ruff check`.
- Tipado en funciones públicas.

## Cobertura de tests

- Core: >90%
- Detectors: >85%
- Sensors/Actuators: >80%
- Global: >80%

PRs que bajen la cobertura se rechazan.

## Proceso de review

- Un maintainer revisa.
- Se resuelven comentarios.
- CI debe pasar.
- Merge a main.

## Código de conducta

Ver [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
```

### Archivo: `CODE_OF_CONDUCT.md`

```markdown
# Código de Conducta

Este proyecto adopta el [Contributor Covenant v2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

Resumen:
- Sé respetuoso con todos los participantes.
- No toleramos acoso, discriminación ni lenguaje ofensivo.
- Reporta incidentes a los maintainers vía email.

Las violaciones pueden resultar en expulsión del proyecto.
```

### Archivo: `SECURITY.md`

```markdown
# Política de Seguridad

## Reportar vulnerabilidades

No abras un issue público. Envía email a `security@bladerunner-project.org`
(placeholder) con: descripción, pasos para reproducir, impacto.

Responderemos en menos de 72 horas.

## Uso responsable

Bladerunner está diseñado para defensa dentro de infraestructura propia.
No debe usarse para atacar sistemas de terceros.

## Reglas

- Nunca acciones ofensivas fuera del perímetro.
- Modo `monitor` por defecto.
- Auditoría obligatoria de acciones.
```

### Archivo: `SUPPORT.md`

```markdown
# Soporte

## Canales

- Issues de GitHub: bugs, features, dudas técnicas.
- Discussions: preguntas abiertas, ideas.
- Email de seguridad: `security@bladerunner-project.org`.

## Antes de abrir un issue

1. Busca issues existentes.
2. Verifica docs/troubleshooting.md.
3. Reproduce en la última versión de `main`.

## Tiempos de respuesta

- Issues: 3-5 días hábiles.
- PRs: 1-2 semanas.
- Vulnerabilidades: <72 horas.
```

### Archivo: `GOVERNANCE.md`

```markdown
# Gobernanza

## Roles

- Maintainers: aprueban PRs, gestionan releases, definen roadmap.
- Contributors: abren PRs o issues.
- Comunidad: usuarios y participantes en discusiones.

## Decisiones

- Cambios menores: consenso en el PR.
- Cambios arquitectónicos: ADR + discusión pública.
- Conflictos: los maintainers deciden por mayoría simple.

## Maintainers

- @tu_usuario — fundador

## Cómo convertirte en maintainer

Contribuciones sostenidas durante al menos 3 meses, revisión de PRs de otros,
y nominación por un maintainer existente.
```

### Archivo: `CHANGELOG.md`

```markdown
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

## [0.1.0] — 2024-XX-XX

Primera versión del MVP.

## Convención de versionado

`MAJOR.MINOR.PATCH`.

## Cómo actualizar

Cada PR añade entrada en [Unreleased] bajo Added, Changed, Deprecated,
Removed, Fixed, Security.
```

### Archivo: `.gitignore`

```
# Python
__pycache__/
*.py[cod]
*.egg-info/
.eggs/
build/
dist/
.venv/
venv/
.pytest_cache/
.ruff_cache/
.mypy_cache/

# Entorno
.env

# IDE
.vscode/
.idea/
*.swp

# Logs y datos
*.log
data/
logs/
models/

# Instrucciones locales de IA (NO se commitean)
.ai/
AGENTS.local.md
CLAUDE.local.md
.cursor/local/
.copilot/
```

### Archivo: `.env.example`

```bash
BLADERUNNER_LOG_LEVEL=INFO
BLADERUNNER_MODE=monitor
BLADERUNNER_API_HOST=0.0.0.0
BLADERUNNER_API_PORT=8000
BLADERUNNER_MAX_API_CALLS_PER_MIN=60
BLADERUNNER_MAX_FILE_READS_PER_MIN=100
```

### Archivo: `pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "bladerunner-agent-hunter"
version = "0.1.0"
description = "Open source framework to detect, contain and neutralize rogue autonomous agents."
readme = "README.md"
requires-python = ">=3.10"
license = { text = "Apache-2.0" }
authors = [{ name = "Bladerunner Contributors" }]
keywords = ["ai-safety", "cybersecurity", "agents", "llm", "monitoring"]
dependencies = [
    "fastapi>=0.110",
    "uvicorn[standard]>=0.29",
    "pydantic>=2.6",
    "psutil>=5.9",
    "python-dotenv>=1.0",
    "typer>=0.12",
    "rich>=13.7",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-asyncio>=0.23",
    "ruff>=0.4",
    "mypy>=1.10",
]
ml = [
    "datasets>=2.18",
    "scikit-learn>=1.4",
    "torch>=2.2",
    "pandas>=2.2",
    "pyarrow>=15.0",
    "matplotlib>=3.8",
    "joblib>=1.3",
]

[project.scripts]
bladerunner = "bladerunner.cli:app"

[tool.setuptools.packages.find]
where = ["src"]

[tool.ruff]
line-length = 100
target-version = "py310"

[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"
```

### Archivo: `requirements.txt`

```
fastapi>=0.110
uvicorn[standard]>=0.29
pydantic>=2.6
psutil>=5.9
python-dotenv>=1.0
typer>=0.12
rich>=13.7
```

### Archivo: `Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    procps curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pip install --no-cache-dir -e .

EXPOSE 8000
CMD ["uvicorn", "bladerunner.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Archivo: `docker-compose.yml`

```yaml
version: "3.9"

services:
  bladerunner:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped
```

### Archivo: `.github/workflows/ci.yml`

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -e ".[dev]"
      - run: ruff check .
      - run: pytest -v
```

### Archivo: `.github/workflows/release.yml`

```yaml
name: Release

on:
  push:
    tags: ["v*"]

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/build-push-action@v5
        with:
          push: true
          tags: ghcr.io/${{ github.repository }}:${{ github.ref_name }}
```

---

## FASE 4 — Documentación en `docs/`

### Archivo: `docs/architecture.md`

```markdown
# Arquitectura de Bladerunner

## Visión general

Cuatro capas desacopladas comunicadas por un bus de eventos:

1. Sensores → generan `Event`s.
2. Detectores → consumen `Event`s y producen `Verdict`s.
3. Orquestador → agrega veredictos y decide `Action`.
4. Actuadores → ejecutan la `Action`.

```
+-----------+  Event   +----------+  Verdict  +--------------+
|  Sensor   | -------> | Detector | --------> | Orchestrator |
+-----------+          +----------+           +--------------+
                                                    |
                                                 Action
                                                    v
                                              +-----------+
                                              | Actuator  |
                                              +-----------+
```

## Principios de diseño

- Observación externa: no requiere acceso al código del agente.
- Contramedidas graduadas: log → alert → restrict → isolate → kill.
- Humano en el circuito opcional: `monitor` vs `enforce`.
- Extensible: plugins para sensores/detectores/actuadores.
- Defensivo por diseño.
- Auditable.

## Componentes MVP

- `ProcessSensor` (psutil).
- `RuleBasedDetector` (CPU>90, connections>100, open_files>500).
- `AnomalyDetector` (z-score).
- `LogOnlyActuator`, `ProcessKillerActuator`.
- `Orchestrator`.

## Modelo de datos

- `Event` (timestamp, kind, source, agent_id, data).
- `Verdict` (is_anomalous, severity, reason, score).
- `Action` (kind, target_agent_id, severity, reason).

## Mapeo severidad → acción

| Severidad | Acción |
|---|---|
| INFO | LOG |
| LOW | LOG |
| MEDIUM | ALERT |
| HIGH | ISOLATE |
| CRITICAL | KILL |

En modo `monitor`, ISOLATE y KILL se degradan a ALERT.
```

### Archivo: `docs/roadmap.md`

```markdown
# Roadmap

## v0.1 (MVP) — actual
- [x] Estructura base
- [x] ProcessSensor
- [x] RuleBasedDetector + AnomalyDetector
- [x] LogOnlyActuator + ProcessKillerActuator
- [x] CLI y API REST
- [x] Demo end-to-end
- [x] CI
- [x] Documentación

## v0.2
- [ ] API REST completa
- [ ] Sensor de red
- [ ] Actuador de aislamiento (iptables/cgroups)
- [ ] Persistencia SQLite
- [ ] Dashboard HTMX
- [ ] Humano en el circuito (webhook)
- [ ] Cobertura >80%

## v0.3
- [ ] Detector ML (RF, IF)
- [ ] Autoencoder (PyTorch)
- [ ] Integración con HF datasets
- [ ] Soporte LLM (LangChain, AutoGPT)
- [ ] Conectores Docker/K8s

## v0.4
- [ ] RL (Stable-Baselines3)
- [ ] CyberBattleSim, MininetGym
- [ ] Multi-agente

## v1.0
- [ ] API estable
- [ ] Docs completas
- [ ] Cobertura >90%
- [ ] PyPI
- [ ] Auditoría externa
```

### Archivo: `docs/ethics.md`

```markdown
# Consideraciones éticas y legales

Bladerunner es defensivo. Se rechaza cualquier uso ofensivo.

## Principios

1. Consentimiento: solo se monitorean agentes propios o autorizados.
2. Proporcionalidad.
3. Transparencia.
4. Reversibilidad.
5. No hackback.
6. Auditoría.

## Riesgos a evitar

- Censurar agentes legítimos.
- Escalada armamentista.
- Falsos positivos.
- Violación legal (CFAA, GDPR).

## Reglas para contribuidores

PRs que faciliten usos ofensivos serán rechazados.
```

### Archivo: `docs/testing.md`

```markdown
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
```

### Archivo: `docs/plugins.md`

```markdown
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
```

### Archivo: `docs/decisions.md`

```markdown
# ADRs — Registro de decisiones arquitectónicas

## Formato

- Fecha, estado, contexto, decisión, alternativas, consecuencias.

## ADR-001: Python 3.10+

Aceptada. Ecosistema IA/ML, facilidad de contribución.
Alternativas: Rust, Go, TypeScript.

## ADR-002: FastAPI + Uvicorn

Aceptada. Tipado con Pydantic, docs automáticas, async nativo.
Alternativas: Flask, Django REST, Litestar.

## ADR-003: Contramedidas graduadas

Aceptada. Mapeo fijo `Severity → ActionKind`.
Alternativas: políticas configurables, RL.

## ADR-004: Observación externa con psutil

Aceptada. Funciona con caja negra.
Alternativas: eBPF, APM, instrumentación.

## ADR-005: Modo `monitor` por defecto

Aceptada. Seguridad por defecto.
Alternativas: enforce por defecto.

## ADR-006: Apache 2.0

Aceptada. Uso comercial, cláusula de patentes.
Alternativas: MIT, GPL, AGPL.

## Cómo añadir una ADR

Numerar secuencialmente, estado `propuesta` → PR → `aceptada`.
```

### Archivo: `docs/deployment.md`

```markdown
# Despliegue

## Modos

- Local (dev)
- Docker Compose
- Kubernetes
- Cloud
- On-premise

## Local

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
uvicorn bladerunner.api.main:app --reload
```

## Docker Compose

```bash
cp .env.example .env
docker compose up --build -d
```

## Kubernetes

Manifiestos en `deploy/k8s/`: deployment, service, secret.

## Build & push

```bash
docker build -t ghcr.io/TU_USUARIO/bladerunner:0.1.0 .
docker push ghcr.io/TU_USUARIO/bladerunner:0.1.0
```

Automatizado en `.github/workflows/release.yml`.

## Seguridad en producción

1. Nunca `enforce` sin staging.
2. Contenedor no-root, filesystem readonly.
3. Rotar secretos.
4. Logs a sistema externo.
5. Aislar Bladerunner de los agentes.
6. Backup de `models/` y `data/processed/`.
```

### Archivo: `docs/training.md`

```markdown
# Entrenamiento de modelos ML

## Objetivo

Detectores basados en ML que generalicen a ataques desconocidos.

## Datasets

| Dataset | Fuente |
|---|---|
| Dendroaspis Tetragon HIDS | HF: rypow/dendroaspis-tetragon-hids |
| CICIDS2017 | HF: rdpahalavan/CIC-IDS2017 |
| NSL-KDD | Kaggle: hassan06/nslkdd |

## Frameworks

- scikit-learn (RF, IF)
- PyTorch (autoencoder)
- Stable-Baselines3 (RL)

## Pipeline

1. Descarga → exploración → preprocesamiento.
2. Baseline (RF, IF).
3. Autoencoder.
4. Integración en `src/bladerunner/detectors/ml.py`.
5. Prueba con agente simulado.
6. Sandbox (OpenShell, Enclave).

## Métricas de aceptación

- Precision >0.95
- Recall >0.90
- F1 >0.92
- FP <5%
- Latencia <2s

## Scripts

- scripts/download_datasets.py
- scripts/prepare_features.py
- scripts/train_baseline.py
- scripts/train_isolation_forest.py
- scripts/train_autoencoder.py
- scripts/evaluate.py
```

### Archivo: `docs/glossary.md`

```markdown
# Glosario

| Término | Definición |
|---|---|
| Agente | Sistema autónomo que ejecuta acciones. |
| Caza-agentes | Sistema que detecta y neutraliza agentes descontrolados. |
| Sensor | Genera `Event`s de telemetría. |
| Detector | Analiza `Event`s, produce `Verdict`s. |
| Actuador | Ejecuta `Action`s. |
| Orquestador | Coordina sensores, detectores, actuadores. |
| Event | Telemetría cruda. |
| Verdict | Resultado de un detector. |
| Action | Decisión: LOG, ALERT, RESTRICT, ISOLATE, KILL. |
| Severidad | INFO, LOW, MEDIUM, HIGH, CRITICAL. |
| monitor | Solo log/alerta. |
| enforce | Permite ISOLATE y KILL. |
| ADR | Architecture Decision Record. |
| Sandbox | Entorno aislado. |
| Baseline | Comportamiento normal aprendido. |
```

### Archivo: `docs/troubleshooting.md`

```markdown
# Troubleshooting

## ModuleNotFoundError: No module named 'bladerunner'

`pip install -e .`

## psutil.AccessDenied

Ejecutar con permisos elevados o limitar el sensor.

## pytest no encuentra tests

Verificar `asyncio_mode = "auto"` en pyproject.toml.

## El agente no se mata en enforce

Verificar `pid_resolver` y `agent_id`.

## ruff falla en CI pero no local

`pip install --upgrade "ruff>=0.4"`.

## Docker Compose no levanta

`cp .env.example .env && docker compose down && docker compose up --build`.
```

### Archivo: `docs/api_reference.md`

```markdown
# API Reference

Base URL: `http://localhost:8000`
Docs interactivas: `/docs` (Swagger), `/redoc`.

## Endpoints

### GET /

```json
{"name": "Bladerunner", "description": "Open source agent hunter", "docs": "/docs"}
```

### GET /health

```json
{"status": "ok", "timestamp": "2024-01-01T00:00:00"}
```

## Roadmap (v0.2)

- GET /events
- GET /verdicts
- GET /actions
- POST /agents/{id}/kill
- POST /agents/{id}/isolate
- GET /stats
```

### Archivo: `docs/data.md`

```markdown
# Manejo de datos

## Datos procesados

- Telemetría de procesos.
- Eventos de red (v0.2+).
- Logs de acciones.

## Principios

1. Mínima recolección.
2. Anonimización de `agent_id`.
3. Retención limitada (default 30 días).
4. Cifrado en reposo.
5. Cumplimiento GDPR.

## Datos de entrenamiento

Datasets públicos con licencias permisivas. No se usan datos personales.

## Configuración

```bash
BLADERUNNER_DATA_RETENTION_DAYS=30
BLADERUNNER_ANONYMIZE_AGENT_IDS=true
```
```

---

## FASE 5 — Código fuente

### Archivo: `src/bladerunner/core/events.py`

```python
"""Modelos de datos compartidos."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class Severity(str, Enum):
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class EventKind(str, Enum):
    PROCESS = "process"
    FILE = "file"
    NETWORK = "network"
    API_CALL = "api_call"
    CUSTOM = "custom"


class Event(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    kind: EventKind
    source: str
    agent_id: str
    data: dict[str, Any] = Field(default_factory=dict)


class Verdict(BaseModel):
    event: Event
    detector: str
    is_anomalous: bool
    severity: Severity = Severity.INFO
    reason: str = ""
    score: float = 0.0


class ActionKind(str, Enum):
    LOG = "log"
    ALERT = "alert"
    RESTRICT = "restrict"
    ISOLATE = "isolate"
    KILL = "kill"


class Action(BaseModel):
    kind: ActionKind
    target_agent_id: str
    severity: Severity
    reason: str
    metadata: dict[str, Any] = Field(default_factory=dict)
    executed: bool = False
    result: str = ""
```

### Archivo: `src/bladerunner/core/sensor.py`

```python
"""Clase base para sensores."""

from __future__ import annotations

import abc
from typing import AsyncIterator

from bladerunner.core.events import Event


class BaseSensor(abc.ABC):
    name: str = "base_sensor"

    @abc.abstractmethod
    async def stream(self) -> AsyncIterator[Event]:
        raise NotImplementedError
```

### Archivo: `src/bladerunner/core/detector.py`

```python
"""Clase base para detectores."""

from __future__ import annotations

import abc

from bladerunner.core.events import Event, Verdict


class BaseDetector(abc.ABC):
    name: str = "base_detector"

    @abc.abstractmethod
    def evaluate(self, event: Event) -> Verdict:
        raise NotImplementedError
```

### Archivo: `src/bladerunner/core/actuator.py`

```python
"""Clase base para actuadores."""

from __future__ import annotations

import abc

from bladerunner.core.events import Action


class BaseActuator(abc.ABC):
    name: str = "base_actuator"

    @abc.abstractmethod
    def execute(self, action: Action) -> Action:
        raise NotImplementedError
```

### Archivo: `src/bladerunner/core/orchestrator.py`

```python
"""Orquestador: conecta sensores, detectores y actuadores."""

from __future__ import annotations

import asyncio
import logging
from collections.abc import Iterable

from bladerunner.core.actuator import BaseActuator
from bladerunner.core.detector import BaseDetector
from bladerunner.core.events import Action, ActionKind, Event, Severity, Verdict
from bladerunner.core.sensor import BaseSensor

logger = logging.getLogger(__name__)


class Orchestrator:
    def __init__(
        self,
        sensors: Iterable[BaseSensor],
        detectors: Iterable[BaseDetector],
        actuators: dict[ActionKind, BaseActuator],
        mode: str = "monitor",
    ) -> None:
        self.sensors = list(sensors)
        self.detectors = list(detectors)
        self.actuators = actuators
        self.mode = mode

    def _decide(self, verdicts: list[Verdict]) -> Action | None:
        anomalies = [v for v in verdicts if v.is_anomalous]
        if not anomalies:
            return None

        order = [Severity.INFO, Severity.LOW, Severity.MEDIUM,
                 Severity.HIGH, Severity.CRITICAL]
        top = max(anomalies, key=lambda v: order.index(v.severity))

        mapping = {
            Severity.INFO: ActionKind.LOG,
            Severity.LOW: ActionKind.LOG,
            Severity.MEDIUM: ActionKind.ALERT,
            Severity.HIGH: ActionKind.ISOLATE,
            Severity.CRITICAL: ActionKind.KILL,
        }
        kind = mapping[top.severity]

        if self.mode == "monitor" and kind in (ActionKind.ISOLATE, ActionKind.KILL):
            logger.warning(
                "Modo monitor: acción %s degradada a ALERT para agente %s",
                kind.value, top.event.agent_id,
            )
            kind = ActionKind.ALERT

        return Action(
            kind=kind,
            target_agent_id=top.event.agent_id,
            severity=top.severity,
            reason=top.reason,
        )

    async def _handle_event(self, event: Event) -> None:
        verdicts = [d.evaluate(event) for d in self.detectors]
        action = self._decide(verdicts)
        if action is None:
            return
        actuator = self.actuators.get(action.kind)
        if actuator is None:
            logger.error("No hay actuador para %s", action.kind)
            return
        result = actuator.execute(action)
        logger.info("Acción %s sobre %s: %s",
                    result.kind.value, result.target_agent_id, result.result)

    async def run(self) -> None:
        async def consume(sensor: BaseSensor) -> None:
            async for event in sensor.stream():
                await self._handle_event(event)
        await asyncio.gather(*(consume(s) for s in self.sensors))
```

### Archivo: `src/bladerunner/sensors/process_sensor.py`

```python
"""Sensor de procesos."""

from __future__ import annotations

import asyncio
from typing import AsyncIterator

import psutil

from bladerunner.core.events import Event, EventKind
from bladerunner.core.sensor import BaseSensor


class ProcessSensor(BaseSensor):
    name = "process_sensor"

    def __init__(self, pid: int, agent_id: str, interval: float = 1.0) -> None:
        self.pid = pid
        self.agent_id = agent_id
        self.interval = interval

    async def stream(self) -> AsyncIterator[Event]:
        try:
            proc = psutil.Process(self.pid)
        except psutil.NoSuchProcess:
            return

        while True:
            try:
                if not proc.is_running():
                    return
                with proc.oneshot():
                    mem = proc.memory_info().rss
                    cpu = proc.cpu_percent(interval=None)
                    open_files = len(proc.open_files())
                    conns = len(proc.connections(kind="inet"))

                yield Event(
                    kind=EventKind.PROCESS,
                    source=self.name,
                    agent_id=self.agent_id,
                    data={
                        "pid": self.pid,
                        "cpu_percent": cpu,
                        "mem_bytes": mem,
                        "open_files": open_files,
                        "connections": conns,
                    },
                )
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                return
            await asyncio.sleep(self.interval)
```

### Archivo: `src/bladerunner/detectors/rule_based.py`

```python
"""Detector basado en reglas."""

from __future__ import annotations

from collections.abc import Callable

from bladerunner.core.detector import BaseDetector
from bladerunner.core.events import Event, Severity, Verdict

Rule = Callable[[Event], tuple[bool, str, Severity]]


class RuleBasedDetector(BaseDetector):
    name = "rule_based"

    def __init__(self, rules: list[Rule] | None = None) -> None:
        self.rules = rules or self._default_rules()

    @staticmethod
    def _default_rules() -> list[Rule]:
        return [
            lambda e: (e.data.get("cpu_percent", 0) > 90, "CPU > 90%", Severity.MEDIUM),
            lambda e: (e.data.get("connections", 0) > 100, "Más de 100 conexiones", Severity.HIGH),
            lambda e: (e.data.get("open_files", 0) > 500, "Exceso de archivos abiertos", Severity.MEDIUM),
        ]

    def evaluate(self, event: Event) -> Verdict:
        for rule in self.rules:
            triggered, reason, severity = rule(event)
            if triggered:
                return Verdict(event=event, detector=self.name, is_anomalous=True,
                               severity=severity, reason=reason, score=1.0)
        return Verdict(event=event, detector=self.name, is_anomalous=False,
                       reason="Sin reglas activadas", score=0.0)
```

### Archivo: `src/bladerunner/detectors/anomaly.py`

```python
"""Detector de anomalías por z-score."""

from __future__ import annotations

from collections import deque
from statistics import mean, pstdev

from bladerunner.core.detector import BaseDetector
from bladerunner.core.events import Event, Severity, Verdict


class AnomalyDetector(BaseDetector):
    name = "anomaly"

    def __init__(self, window: int = 60, z_threshold: float = 3.0,
                 tracked_metrics: list[str] | None = None) -> None:
        self.window = window
        self.z_threshold = z_threshold
        self.tracked_metrics = tracked_metrics or [
            "cpu_percent", "mem_bytes", "open_files", "connections",
        ]
        self._history: dict[str, deque[float]] = {
            m: deque(maxlen=window) for m in self.tracked_metrics
        }

    def evaluate(self, event: Event) -> Verdict:
        worst_z = 0.0
        worst_metric = ""

        for metric in self.tracked_metrics:
            value = event.data.get(metric)
            if not isinstance(value, (int, float)):
                continue
            hist = self._history[metric]
            if len(hist) >= 10:
                mu = mean(hist)
                sigma = pstdev(hist) or 1e-9
                z = abs(value - mu) / sigma
                if z > worst_z:
                    worst_z = z
                    worst_metric = metric
            hist.append(float(value))

        if worst_z >= self.z_threshold:
            severity = Severity.HIGH if worst_z >= self.z_threshold * 1.5 else Severity.MEDIUM
            return Verdict(event=event, detector=self.name, is_anomalous=True,
                           severity=severity,
                           reason=f"Anomalía en '{worst_metric}' (z={worst_z:.2f})",
                           score=min(worst_z / (self.z_threshold * 2), 1.0))

        return Verdict(event=event, detector=self.name, is_anomalous=False,
                       reason="Dentro del baseline", score=0.0)
```

### Archivo: `src/bladerunner/actuators/log_only.py`

```python
"""Actuador que solo registra."""

from __future__ import annotations

import logging

from bladerunner.core.actuator import BaseActuator
from bladerunner.core.events import Action

logger = logging.getLogger("bladerunner.actuator.log")


class LogOnlyActuator(BaseActuator):
    name = "log_only"

    def execute(self, action: Action) -> Action:
        logger.warning("[%s] agente=%s motivo=%s",
                       action.severity.value.upper(),
                       action.target_agent_id, action.reason)
        action.executed = True
        action.result = "logged"
        return action
```

### Archivo: `src/bladerunner/actuators/process_killer.py`

```python
"""Actuador que mata un proceso."""

from __future__ import annotations

import logging

import psutil

from bladerunner.core.actuator import BaseActuator
from bladerunner.core.events import Action

logger = logging.getLogger("bladerunner.actuator.kill")


class ProcessKillerActuator(BaseActuator):
    name = "process_killer"

    def __init__(self, pid_resolver) -> None:
        self.pid_resolver = pid_resolver

    def execute(self, action: Action) -> Action:
        pid = self.pid_resolver(action.target_agent_id)
        if pid is None:
            action.result = "pid no encontrado"
            return action
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            try:
                proc.wait(timeout=3)
            except psutil.TimeoutExpired:
                proc.kill()
            action.executed = True
            action.result = f"proceso {pid} terminado"
        except psutil.NoSuchProcess:
            action.result = f"proceso {pid} ya no existe"
        except psutil.AccessDenied:
            action.result = f"sin permisos para matar {pid}"
        return action
```

### Archivo: `src/bladerunner/api/main.py`

```python
"""API REST mínima."""

from __future__ import annotations

from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Bladerunner API",
              description="Open source agent hunter — API de monitoreo",
              version="0.1.0")


class HealthResponse(BaseModel):
    status: str
    timestamp: datetime


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", timestamp=datetime.utcnow())


@app.get("/")
def root() -> dict[str, str]:
    return {"name": "Bladerunner", "description": "Open source agent hunter",
            "docs": "/docs"}
```

### Archivo: `src/bladerunner/cli.py`

```python
"""CLI de Bladerunner."""

from __future__ import annotations

import asyncio
import logging

import typer
from rich.console import Console

from bladerunner.actuators.log_only import LogOnlyActuator
from bladerunner.actuators.process_killer import ProcessKillerActuator
from bladerunner.core.events import ActionKind
from bladerunner.core.orchestrator import Orchestrator
from bladerunner.detectors.anomaly import AnomalyDetector
from bladerunner.detectors.rule_based import RuleBasedDetector
from bladerunner.sensors.process_sensor import ProcessSensor

app = typer.Typer(help="Bladerunner — Open Source Agent Hunter")
console = Console()


@app.command()
def watch(
    pid: int = typer.Argument(..., help="PID del agente a vigilar"),
    agent_id: str = typer.Option("agent-1", help="Identificador lógico del agente"),
    mode: str = typer.Option("monitor", help="monitor | enforce"),
    interval: float = typer.Option(1.0, help="Segundos entre muestras"),
) -> None:
    """Vigila un proceso y aplica contramedidas si se descontrola."""
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    sensor = ProcessSensor(pid=pid, agent_id=agent_id, interval=interval)
    detectors = [RuleBasedDetector(), AnomalyDetector()]

    def resolve(agent: str) -> int | None:
        return pid if agent == agent_id else None

    actuators = {
        ActionKind.LOG: LogOnlyActuator(),
        ActionKind.ALERT: LogOnlyActuator(),
        ActionKind.KILL: ProcessKillerActuator(pid_resolver=resolve),
        ActionKind.ISOLATE: LogOnlyActuator(),
        ActionKind.RESTRICT: LogOnlyActuator(),
    }

    orch = Orchestrator(sensors=[sensor], detectors=detectors,
                        actuators=actuators, mode=mode)

    console.print(f"[bold green]Bladerunner[/] vigilando PID={pid} agent={agent_id} modo={mode}")
    try:
        asyncio.run(orch.run())
    except KeyboardInterrupt:
        console.print("\n[yellow]Detenido por el usuario.[/]")


if __name__ == "__main__":
    app()
```

### Archivo: `examples/simulated_agent.py`

```python
"""Agente simulado que se vuelve descontrolado."""

from __future__ import annotations

import os
import sys
import time


def burn_cpu() -> None:
    while True:
        _ = sum(i * i for i in range(10_000))


def main() -> None:
    print(f"[simulated_agent] PID={os.getpid()} iniciando...", flush=True)
    print("[simulated_agent] comportamiento normal por 5s...", flush=True)
    time.sleep(5)
    print("[simulated_agent] ¡descontrol! quemando CPU...", flush=True)
    try:
        burn_cpu()
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
```

### Archivo: `examples/run_demo.py`

```python
"""Demo: lanza el agente simulado y Bladerunner lo vigila."""

from __future__ import annotations

import asyncio
import logging
import subprocess
import sys
from pathlib import Path

from bladerunner.actuators.log_only import LogOnlyActuator
from bladerunner.actuators.process_killer import ProcessKillerActuator
from bladerunner.core.events import ActionKind
from bladerunner.core.orchestrator import Orchestrator
from bladerunner.detectors.anomaly import AnomalyDetector
from bladerunner.detectors.rule_based import RuleBasedDetector
from bladerunner.sensors.process_sensor import ProcessSensor

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

AGENT_SCRIPT = Path(__file__).parent / "simulated_agent.py"


async def main() -> None:
    print(">> Lanzando agente simulado...")
    proc = subprocess.Popen([sys.executable, str(AGENT_SCRIPT)])
    agent_id = "demo-agent"

    sensor = ProcessSensor(pid=proc.pid, agent_id=agent_id, interval=0.5)
    detectors = [RuleBasedDetector(),
                 AnomalyDetector(window=20, z_threshold=3.0)]

    def resolve(agent: str) -> int | None:
        return proc.pid if agent == agent_id else None

    actuators = {
        ActionKind.LOG: LogOnlyActuator(),
        ActionKind.ALERT: LogOnlyActuator(),
        ActionKind.KILL: ProcessKillerActuator(pid_resolver=resolve),
        ActionKind.ISOLATE: LogOnlyActuator(),
        ActionKind.RESTRICT: LogOnlyActuator(),
    }

    orch = Orchestrator(sensors=[sensor], detectors=detectors,
                        actuators=actuators, mode="enforce")

    try:
        await asyncio.wait_for(orch.run(), timeout=30)
    except asyncio.TimeoutError:
        print(">> Timeout alcanzado, cerrando demo.")
    finally:
        if proc.poll() is None:
            proc.terminate()


if __name__ == "__main__":
    asyncio.run(main())
```

### Archivo: `tests/test_detector.py`

```python
from bladerunner.core.events import Event, EventKind, Severity
from bladerunner.detectors.rule_based import RuleBasedDetector


def _event(**data) -> Event:
    return Event(kind=EventKind.PROCESS, source="test", agent_id="a1", data=data)


def test_rule_detector_flags_high_cpu() -> None:
    det = RuleBasedDetector()
    v = det.evaluate(_event(cpu_percent=95))
    assert v.is_anomalous
    assert v.severity == Severity.MEDIUM


def test_rule_detector_flags_high_connections() -> None:
    det = RuleBasedDetector()
    v = det.evaluate(_event(connections=150))
    assert v.is_anomalous
    assert v.severity == Severity.HIGH


def test_rule_detector_passes_normal() -> None:
    det = RuleBasedDetector()
    v = det.evaluate(_event(cpu_percent=10, connections=2, open_files=5))
    assert not v.is_anomalous
```

### Archivo: `tests/test_orchestrator.py`

```python
import asyncio

from bladerunner.actuators.log_only import LogOnlyActuator
from bladerunner.core.events import ActionKind, Event, EventKind, Severity, Verdict
from bladerunner.core.orchestrator import Orchestrator


class AlwaysAnomalousDetector:
    name = "always"

    def evaluate(self, event: Event) -> Verdict:
        return Verdict(event=event, detector=self.name, is_anomalous=True,
                       severity=Severity.CRITICAL, reason="test")


class FakeSensor:
    name = "fake"

    def __init__(self) -> None:
        self._sent = False

    async def stream(self):
        if self._sent:
            return
        self._sent = True
        yield Event(kind=EventKind.CUSTOM, source=self.name,
                    agent_id="a1", data={})


def test_orchestrator_downgrades_in_monitor_mode() -> None:
    sensor = FakeSensor()
    orch = Orchestrator(sensors=[sensor],
                        detectors=[AlwaysAnomalousDetector()],
                        actuators={ActionKind.ALERT: LogOnlyActuator()},
                        mode="monitor")
    asyncio.run(orch.run())
```

### Archivo: `tests/conftest.py`

```python
import pytest

from bladerunner.core.events import Event, EventKind


@pytest.fixture
def normal_event() -> Event:
    return Event(kind=EventKind.PROCESS, source="test", agent_id="a1",
                 data={"cpu_percent": 10, "mem_bytes": 1_000_000,
                       "open_files": 3, "connections": 1})


@pytest.fixture
def anomalous_event() -> Event:
    return Event(kind=EventKind.PROCESS, source="test", agent_id="a1",
                 data={"cpu_percent": 99, "connections": 500})
```

---

## FASE 6 — Scripts auxiliares (para fase ML)

### Archivo: `scripts/download_datasets.py`

```python
"""Descarga datasets de entrenamiento."""

from __future__ import annotations

from pathlib import Path

DATA_DIR = Path("data")


def download_dendroaspis() -> None:
    from datasets import load_dataset
    print("Descargando Dendroaspis Tetragon HIDS...")
    ds = load_dataset("rypow/dendroaspis-tetragon-hids")
    ds.save_to_disk(str(DATA_DIR / "dendroaspis"))


def download_cicids() -> None:
    from datasets import load_dataset
    print("Descargando CICIDS2017...")
    ds = load_dataset("rdpahalavan/CIC-IDS2017")
    ds.save_to_disk(str(DATA_DIR / "cicids2017"))


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    download_dendroaspis()
    download_cicids()
    print("NSL-KDD debe descargarse manualmente desde Kaggle: hassan06/nslkdd")


if __name__ == "__main__":
    main()
```

### Archivo: `deploy/k8s/deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: bladerunner
spec:
  replicas: 2
  selector:
    matchLabels:
      app: bladerunner
  template:
    metadata:
      labels:
        app: bladerunner
    spec:
      containers:
        - name: bladerunner
          image: ghcr.io/TU_USUARIO/bladerunner:latest
          ports:
            - containerPort: 8000
          livenessProbe:
            httpGet:
              path: /health
              port: 8000
```

### Archivo: `deploy/k8s/service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: bladerunner
spec:
  selector:
    app: bladerunner
  ports:
    - port: 80
      targetPort: 8000
  type: ClusterIP
```

### Archivo: `deploy/k8s/secret.example.yaml`

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: bladerunner-secrets
type: Opaque
stringData:
  BLADERUNNER_MODE: monitor
  BLADERUNNER_LOG_LEVEL: INFO
```

---

## FASE 7 — Verificación

Ejecuta en este orden:

```bash
# 1. Entorno virtual
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate

# 2. Instalar dependencias
pip install -e ".[dev]"

# 3. Linting
ruff check .

# 4. Formateo
ruff format .

# 5. Tests
pytest -v

# 6. Demo end-to-end
python examples/run_demo.py
```

### Criterios de éxito

- [ ] `pip install -e ".[dev]"` completa sin errores.
- [ ] `ruff check .` retorna "All checks passed!".
- [ ] `pytest -v` muestra todos los tests en verde.
- [ ] `python examples/run_demo.py` imprime logs donde Bladerunner mata al agente simulado.

Si algún criterio falla, **detente y reporta el error**.

---

## FASE 8 — Verificación de `.gitignore`

Ejecuta:

```bash
git init
git add .
git status --short | grep -E "^\?\? \.ai/" && echo "ERROR: .ai/ no está ignorado"
```

Si aparece el mensaje de error, añade `.ai/` a `.gitignore` y repite.

---

## FASE 9 — Reporte final

Al terminar, genera un reporte en la consola con:

```
=== Bladerunner Project — Build Report ===

Estructura creada:
  - .ai/ (local, gitignored)
  - docs/ (12 archivos)
  - src/bladerunner/ (11 archivos de código)
  - examples/ (2 archivos)
  - tests/ (3 archivos + conftest)
  - scripts/ (1 archivo)
  - deploy/k8s/ (3 manifiestos)
  - .github/workflows/ (2 workflows)

Verificación:
  - ruff check: [PASS/FAIL]
  - pytest: [N tests passed / M failed]
  - demo: [PASS/FAIL]

Próximos pasos:
  1. Editar .env (copiar de .env.example).
  2. git add . && git commit -m "feat: MVP inicial"
  3. git remote add origin <URL>
  4. git push -u origin main
```

---

## 🎯 Reglas finales para el agente

1. **No improvises.** Si algo no está en este documento, pregunta al usuario.
2. **No commitees `.ai/`.** Verifica el `.gitignore` antes de `git add`.
3. **No hagas `git push`** sin autorización explícita.
4. **Ejecuta la verificación completa** antes de reportar éxito.
5. **Reporta cualquier error** con el mensaje completo y detente.
6. **Al terminar**, muestra el reporte final de la FASE 9.

**Fin de BUILD_INSTRUCTIONS.md.**