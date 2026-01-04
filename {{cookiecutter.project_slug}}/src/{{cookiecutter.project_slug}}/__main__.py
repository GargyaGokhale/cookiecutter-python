"""Main entry point for {{ cookiecutter.project_name }}.

Run with: python -m {{ cookiecutter.project_slug }}
"""

from {{ cookiecutter.project_slug }}.utils.logging import get_logger

logger = get_logger(__name__)


def main() -> None:
    """Main entry point."""
    logger.info("Starting {{ cookiecutter.project_name }}...")
    print("Hello from {{ cookiecutter.project_name }}! 🚀")


if __name__ == "__main__":
    main()
