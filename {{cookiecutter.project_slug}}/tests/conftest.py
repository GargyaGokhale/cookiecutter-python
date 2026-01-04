"""Pytest fixtures for {{ cookiecutter.project_name }}."""

from pathlib import Path

import pytest


@pytest.fixture
def project_root() -> Path:
    """Project root directory."""
    return Path(__file__).parent.parent


@pytest.fixture
def data_dir(project_root: Path) -> Path:
    """Data directory."""
    return project_root / "data"
