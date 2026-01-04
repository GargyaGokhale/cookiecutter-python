# Cookiecutter Python Template

A minimal Python project template for data science, ML, and dashboards.

## Features

- **uv** - Fast package management
- **Ruff** - Linting and formatting
- **pytest** - Testing
- **pre-commit** - Git hooks
- **Docker** - Development container

### Optional
- **FastAPI** - REST API
- **NiceGUI** - Web frontend
- **MkDocs** - Documentation

## Usage

```bash
uvx cookiecutter gh:yourusername/cookiecutter-python
# or
cookiecutter /path/to/cookiecutter-python
```

## Options

| Option | Description |
|--------|-------------|
| `project_name` | Project name |
| `python_version` | 3.12, 3.11, 3.10 |
| `license` | MIT, Apache-2.0, Proprietary |
| `use_loguru` | Use loguru (yes) or stdlib logging (no) |
| `include_api` | Add FastAPI |
| `include_frontend` | Add NiceGUI |
| `include_docs` | Add MkDocs |

## Generated Structure

```
your_project/
├── src/your_project/      # Main package
│   └── utils/logging.py   # Logging setup
├── tests/                  # Tests
├── data/                   # Data files
├── notebooks/              # Jupyter notebooks
├── docker/                 # Docker config
├── api/                    # FastAPI (optional)
├── frontend/               # NiceGUI (optional)
├── docs/                   # MkDocs (optional)
├── pyproject.toml
├── Makefile
└── .pre-commit-config.yaml
```

## After Generation

```bash
cd your_project
uv sync
uv run pre-commit install
make run
```
