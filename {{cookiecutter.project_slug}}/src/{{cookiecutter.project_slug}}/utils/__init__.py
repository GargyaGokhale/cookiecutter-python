"""Utility modules."""

from {{ cookiecutter.project_slug }}.utils.logging import get_logger, setup_logging

__all__ = ["get_logger", "setup_logging"]
