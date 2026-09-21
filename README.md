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
