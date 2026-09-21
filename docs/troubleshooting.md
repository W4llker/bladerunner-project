# Troubleshooting

## ModuleNotFoundError: No module named 'bladerunner'

`pip install -e .`

## psutil.AccessDenied

Run with elevated permissions or restrict the sensor's scope.

## pytest can't find tests

Check `asyncio_mode = "auto"` in pyproject.toml.

## The agent isn't killed in enforce mode

Check `pid_resolver` and `agent_id`.

## ruff fails in CI but not locally

`pip install --upgrade "ruff>=0.4"`.

## Docker Compose won't start

`cp .env.example .env && docker compose down && docker compose up --build`.
