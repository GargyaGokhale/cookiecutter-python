"""Example tests for {{ cookiecutter.project_name }}."""

from {{ cookiecutter.project_slug }} import __version__
from {{ cookiecutter.project_slug }}.utils.logging import get_logger


def test_version():
    """Version is defined."""
    assert __version__ is not None


def test_logger():
    """Logger works."""
    logger = get_logger(__name__)
    assert logger is not None
