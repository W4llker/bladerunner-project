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
