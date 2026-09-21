"""Agente simulado que se vuelve descontrolado."""

from __future__ import annotations

import os
import sys
import time


def burn_cpu() -> None:
    while True:
        _ = sum(i * i for i in range(10_000))


def main() -> None:
    print(f"[simulated_agent] PID={os.getpid()} iniciando...", flush=True)
    print("[simulated_agent] comportamiento normal por 5s...", flush=True)
    time.sleep(5)
    print("[simulated_agent] ¡descontrol! quemando CPU...", flush=True)
    try:
        burn_cpu()
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
