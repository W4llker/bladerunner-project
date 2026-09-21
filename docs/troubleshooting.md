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
