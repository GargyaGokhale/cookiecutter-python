"""Logging configuration for {{ cookiecutter.project_name }}."""
{%- if cookiecutter.use_loguru == "yes" %}

import os
import sys

from loguru import logger


def setup_logging(level: str | None = None) -> None:
    """Configure logging with loguru."""
    logger.remove()
    level = level or os.getenv("LOG_LEVEL", "INFO")
    logger.add(sys.stderr, level=level, colorize=True)


def get_logger(name: str | None = None):
    """Get a logger instance."""
    return logger.bind(name=name) if name else logger


# Auto-setup on import
setup_logging()
{%- else %}

import logging
import os


def setup_logging(level: str | None = None) -> None:
    """Configure logging with standard library."""
    level = level or os.getenv("LOG_LEVEL", "INFO")
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def get_logger(name: str | None = None) -> logging.Logger:
    """Get a logger instance."""
    return logging.getLogger(name or __name__)


# Auto-setup on import
setup_logging()
{%- endif %}
