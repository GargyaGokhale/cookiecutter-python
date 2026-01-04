"""{{ cookiecutter.project_name }} - FastAPI Application.

Run with: uv run uvicorn api.main:app --reload
Docs: http://localhost:8000/docs
"""

from datetime import datetime

from fastapi import FastAPI

from {{ cookiecutter.project_slug }} import __version__

app = FastAPI(
    title="{{ cookiecutter.project_name }} API",
    version=__version__,
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {"name": "{{ cookiecutter.project_name }}", "docs": "/docs"}


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": __version__,
        "timestamp": datetime.utcnow().isoformat(),
    }
