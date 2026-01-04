# Docker

Development Docker setup for {{ cookiecutter.project_name }}.

## Quick Start

```bash
# Build and run
make docker-build
make docker-up

# View logs
make docker-logs

# Stop
make docker-down
```

## Files

- `Dockerfile.dev` - Development image with hot reload
- `docker-compose.yml` - Service configuration

## Volumes

Source code is mounted for hot reload:
- `src/` → `/app/src`
{%- if cookiecutter.include_api == "yes" %}
- `api/` → `/app/api`
{%- endif %}
{%- if cookiecutter.include_frontend == "yes" %}
- `frontend/` → `/app/frontend`
{%- endif %}
- `data/` → `/app/data`
