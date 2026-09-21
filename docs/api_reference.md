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
