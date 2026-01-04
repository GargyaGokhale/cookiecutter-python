# Template Usage

## Generate a Project

```bash
uvx cookiecutter /path/to/cookiecutter-python
```

## Configuration Options

| Option | Values | Description |
|--------|--------|-------------|
| `project_name` | text | Human-readable name |
| `project_slug` | auto | Python package name |
| `python_version` | 3.12, 3.11, 3.10 | Python version |
| `license` | MIT, Apache-2.0, Proprietary | License |
| `use_loguru` | yes, no | Use loguru or stdlib logging |
| `include_api` | yes, no | Add FastAPI |
| `include_frontend` | yes, no | Add NiceGUI |
| `include_docs` | yes, no | Add MkDocs |

## Post-Generation

```bash
cd your_project
git init
uv sync
uv run pre-commit install
cp .env.example .env
make test
```

## Common Use Cases

### Data Science Project (Minimal)
```
use_loguru: no
include_api: no
include_frontend: no
include_docs: no
```

### API Service
```
use_loguru: yes
include_api: yes
include_docs: yes
```

### Dashboard
```
include_frontend: yes
include_api: yes
```
