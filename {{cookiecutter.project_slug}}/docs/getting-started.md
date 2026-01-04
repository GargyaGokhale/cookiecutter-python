# Getting Started

## Installation

```bash
# Clone and enter
git clone <repository-url>
cd {{ cookiecutter.project_slug }}

# Install dependencies
uv sync

# Set up pre-commit
uv run pre-commit install

# Configure environment
cp .env.example .env
```

## Common Commands

| Command | Description |
|---------|-------------|
| `make run` | Run application |
| `make test` | Run tests |
| `make format` | Format code |
| `make lint` | Lint code |
{%- if cookiecutter.include_api == "yes" %}
| `make api` | Start API |
{%- endif %}
{%- if cookiecutter.include_frontend == "yes" %}
| `make frontend` | Start frontend |
{%- endif %}

## Docker

```bash
make docker-build
make docker-up
make docker-logs
```

## Configuration

Edit `.env` for settings:

```ini
LOG_LEVEL=INFO
{%- if cookiecutter.include_api == "yes" %}
API_PORT=8000
{%- endif %}
{%- if cookiecutter.include_frontend == "yes" %}
FRONTEND_PORT=8080
{%- endif %}
```

