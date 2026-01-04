# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Features

- Python {{ cookiecutter.python_version }}+ with [uv](https://github.com/astral-sh/uv)
- [Ruff](https://github.com/astral-sh/ruff) for linting and formatting
- [pytest](https://pytest.org/) for testing
- Pre-commit hooks
{%- if cookiecutter.include_api == "yes" %}
- FastAPI REST API
{%- endif %}
{%- if cookiecutter.include_frontend == "yes" %}
- NiceGUI frontend
{%- endif %}
- Docker development setup

## Quick Start

```bash
# Install
uv sync
uv run pre-commit install

# Run
make run
{%- if cookiecutter.include_api == "yes" %}
make api      # Start API
{%- endif %}
{%- if cookiecutter.include_frontend == "yes" %}
make frontend # Start frontend
{%- endif %}

# Test
make test
```

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── src/{{ cookiecutter.project_slug }}/   # Main package
├── tests/                                  # Tests
├── data/                                   # Data files
├── notebooks/                              # Jupyter notebooks
├── docker/                                 # Docker config
{%- if cookiecutter.include_api == "yes" %}
├── api/                                    # FastAPI app
{%- endif %}
{%- if cookiecutter.include_frontend == "yes" %}
├── frontend/                               # NiceGUI app
{%- endif %}
└── pyproject.toml                          # Config
```
