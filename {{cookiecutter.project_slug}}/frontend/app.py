"""{{ cookiecutter.project_name }} - NiceGUI Frontend.

Run with: uv run python -m frontend.app
Access: http://localhost:8080
"""

import os

from nicegui import ui

HOST = os.getenv("FRONTEND_HOST", "0.0.0.0")
PORT = int(os.getenv("FRONTEND_PORT", "8080"))


@ui.page("/")
def home():
    """Home page."""
    with ui.column().classes("w-full max-w-2xl mx-auto p-8 gap-4"):
        ui.label("{{ cookiecutter.project_name }}").classes("text-3xl font-bold")
        ui.label("{{ cookiecutter.project_description }}").classes("text-gray-600")

        with ui.card().classes("w-full p-4"):
            ui.label("Getting Started").classes("text-xl font-semibold mb-2")
            ui.markdown("Edit `frontend/app.py` to customize this page.")

        ui.button("Click me", on_click=lambda: ui.notify("Hello! 👋"))


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(host=HOST, port=PORT, title="{{ cookiecutter.project_name }}")
