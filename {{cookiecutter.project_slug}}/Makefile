.PHONY: help install format lint check test run clean docker-build docker-up docker-down

.DEFAULT_GOAL := help

help: ## Show this help
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z_-]+:.*##/ { printf "  %-15s %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

install: ## Install dependencies
	uv sync
	uv run pre-commit install

format: ## Format code
	uv run ruff format .
	uv run ruff check --fix .

lint: ## Lint code
	uv run ruff check .

check: lint ## Run all checks

test: ## Run tests
	uv run pytest

test-cov: ## Run tests with coverage
	uv run pytest --cov=src/{{ cookiecutter.project_slug }} --cov-report=term-missing

run: ## Run the application
	uv run python -m {{ cookiecutter.project_slug }}

{% if cookiecutter.include_api == "yes" -%}
api: ## Start FastAPI server
	uv run uvicorn api.main:app --reload

{% endif -%}
{% if cookiecutter.include_frontend == "yes" -%}
frontend: ## Start NiceGUI frontend
	uv run python -m frontend.app

{% endif -%}
{% if cookiecutter.include_docs == "yes" -%}
docs: ## Serve documentation
	uv run mkdocs serve

{% endif -%}
docker-build: ## Build Docker image
	docker build -f docker/Dockerfile.dev -t {{ cookiecutter.project_slug }}:dev .

docker-up: ## Start Docker services
	docker compose -f docker/docker-compose.yml up -d

docker-down: ## Stop Docker services
	docker compose -f docker/docker-compose.yml down

docker-logs: ## View Docker logs
	docker compose -f docker/docker-compose.yml logs -f

clean: ## Clean build artifacts
	rm -rf build/ dist/ *.egg-info/ .pytest_cache/ .ruff_cache/ .coverage htmlcov/
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
