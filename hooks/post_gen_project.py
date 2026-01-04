"""Post-generation hooks for cookiecutter template."""

import os
import shutil

include_frontend = "{{ cookiecutter.include_frontend }}" == "yes"
include_api = "{{ cookiecutter.include_api }}" == "yes"
include_docs = "{{ cookiecutter.include_docs }}" == "yes"


def remove_dir(path: str) -> None:
    """Remove a directory if it exists."""
    if os.path.exists(path):
        shutil.rmtree(path)


def remove_file(path: str) -> None:
    """Remove a file if it exists."""
    if os.path.exists(path):
        os.remove(path)


if not include_frontend:
    remove_dir("frontend")

if not include_api:
    remove_dir("api")

if not include_docs:
    remove_dir("docs")
    remove_file("mkdocs.yml")

print("\n✨ Project created!")
print("\nNext steps:")
print("  cd {{ cookiecutter.project_slug }}")
print("  uv sync")
print("  uv run pre-commit install")
