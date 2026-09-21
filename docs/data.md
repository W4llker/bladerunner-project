# Data handling

## Data processed

- Process telemetry.
- Network events (v0.2+).
- Action logs.

## Principles

1. Minimal collection.
2. Anonymization of `agent_id`.
3. Limited retention (default 30 days).
4. Encryption at rest.
5. GDPR compliance.

## Training data

Public datasets with permissive licenses. No personal data is used.

## Configuration

```bash
BLADERUNNER_DATA_RETENTION_DAYS=30
BLADERUNNER_ANONYMIZE_AGENT_IDS=true
```
