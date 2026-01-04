# Frontend

NiceGUI application for {{ cookiecutter.project_name }}.

## Quick Start

```bash
make frontend
# or
uv run python -m frontend.app
```

Access at: http://localhost:8080

## Adding Pages

```python
@ui.page("/my-page")
def my_page():
    ui.label("My Page")
```

## Resources

- [NiceGUI Docs](https://nicegui.io/documentation)
