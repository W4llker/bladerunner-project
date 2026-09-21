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
