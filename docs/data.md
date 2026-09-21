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
