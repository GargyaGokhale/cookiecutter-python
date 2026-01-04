# Features

## Core

### uv
Fast Python package installer. [Docs](https://github.com/astral-sh/uv)

```bash
uv sync        # Install deps
uv add pandas  # Add package
uv run pytest  # Run in venv
```

### Ruff
Linting and formatting. [Docs](https://docs.astral.sh/ruff/)

```bash
make format  # Format code
make lint    # Check issues
```

### pytest
Testing with fixtures.

```bash
make test      # Run tests
make test-cov  # With coverage
```

### Pre-commit
Git hooks for code quality.

```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

### Logging
Choice of loguru or stdlib logging.

```python
from your_project.utils.logging import get_logger
logger = get_logger(__name__)
logger.info("Hello")
```

## Optional

### FastAPI (`include_api=yes`)
REST API with `/health` endpoint.

```bash
make api  # http://localhost:8000/docs
```

### NiceGUI (`include_frontend=yes`)
Python web frontend.

```bash
make frontend  # http://localhost:8080
```

### MkDocs (`include_docs=yes`)
Documentation with Material theme.

```bash
make docs  # http://localhost:8000
```

## Docker

Development container with hot reload.

```bash
make docker-build
make docker-up
```
