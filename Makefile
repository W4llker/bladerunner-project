.PHONY: help install install-dev lint format test test-cov demo api docker clean pre-commit pre-commit-install

help:  ## Muestra esta ayuda
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Instala el paquete en modo editable
	pip install -e .

install-dev:  ## Instala con dependencias de desarrollo
	pip install -e ".[dev]"

install-ml:  ## Instala con dependencias de ML
	pip install -e ".[dev,ml]"

lint:  ## Ejecuta ruff check
	ruff check .

format:  ## Formatea con ruff
	ruff format .

test:  ## Ejecuta los tests
	pytest -v

test-cov:  ## Tests con cobertura
	pytest --cov=src/bladerunner --cov-report=term-missing --cov-report=html

demo:  ## Ejecuta la demo end-to-end
	python examples/run_demo.py

api:  ## Levanta la API REST
	uvicorn bladerunner.api.main:app --reload

docker:  ## Levanta con Docker Compose
	docker compose up --build

pre-commit-install:  ## Instala los hooks de pre-commit
	pre-commit install

pre-commit:  ## Ejecuta pre-commit en todos los archivos
	pre-commit run --all-files

clean:  ## Limpia artefactos de build y caches
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .ruff_cache -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ .coverage htmlcov/
