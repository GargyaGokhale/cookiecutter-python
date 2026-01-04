# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Quick Start

```bash
# Install
uv sync
uv run pre-commit install
cp .env.example .env

# Run
make run
```

## Commands

| Command | Description |
|---------|-------------|
| `make install` | Install dependencies |
| `make run` | Run application |
| `make test` | Run tests |
| `make format` | Format code |
| `make lint` | Lint code |
{%- if cookiecutter.include_api == "yes" %}
| `make api` | Start API (http://localhost:8000) |
{%- endif %}
{%- if cookiecutter.include_frontend == "yes" %}
| `make frontend` | Start frontend (http://localhost:8080) |
{%- endif %}
{%- if cookiecutter.include_docs == "yes" %}
| `make docs` | Serve docs |
{%- endif %}

## Docker

```bash
make docker-build
make docker-up
```

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── src/{{ cookiecutter.project_slug }}/   # Main package
├── tests/                                  # Tests
├── data/                                   # Data files
├── notebooks/                              # Jupyter notebooks
├── configs/                                # Config files
├── scripts/                                # Utility scripts
├── docker/                                 # Docker config
{%- if cookiecutter.include_api == "yes" %}
├── api/                                    # FastAPI app
{%- endif %}
{%- if cookiecutter.include_frontend == "yes" %}
├── frontend/                               # NiceGUI app
{%- endif %}
{%- if cookiecutter.include_docs == "yes" %}
├── docs/                                   # Documentation
{%- endif %}
└── pyproject.toml
```

## License

{{ cookiecutter.license }}
