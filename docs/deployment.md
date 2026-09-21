# Deployment

## Modes

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

Manifests in `deploy/k8s/`: deployment, service, secret.

## Build & push

```bash
docker build -t ghcr.io/W4llker/bladerunner:0.1.0 .
docker push ghcr.io/W4llker/bladerunner:0.1.0
```

Automated in `.github/workflows/release.yml`.

## Production security

1. Never `enforce` without staging first.
2. Non-root container, read-only filesystem.
3. Rotate secrets.
4. Ship logs to an external system.
5. Isolate Bladerunner from the agents it watches.
6. Back up `models/` and `data/processed/`.
