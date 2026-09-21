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
docker build -t ghcr.io/W4llker/bladerunner:0.1.0 .
docker push ghcr.io/W4llker/bladerunner:0.1.0
```

Automatizado en `.github/workflows/release.yml`.

## Seguridad en producción

1. Nunca `enforce` sin staging.
2. Contenedor no-root, filesystem readonly.
3. Rotar secretos.
4. Logs a sistema externo.
5. Aislar Bladerunner de los agentes.
6. Backup de `models/` y `data/processed/`.
