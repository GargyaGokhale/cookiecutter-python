# Frontend

NiceGUI web interface.

## Quick Start

```bash
make frontend
```

Access: http://localhost:8080

## Adding Pages

Edit `frontend/app.py`:

```python
@ui.page("/my-page")
def my_page():
    ui.label("My Page")
    ui.button("Click", on_click=lambda: ui.notify("Clicked!"))
```

## Resources

- [NiceGUI Docs](https://nicegui.io/documentation)

