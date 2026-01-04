"""Pre-generation hooks for cookiecutter template."""

import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

project_slug = "{{ cookiecutter.project_slug }}"

if not re.match(MODULE_REGEX, project_slug):
    print(f"ERROR: '{project_slug}' is not a valid Python module name!")
    print("Please use only letters, numbers, and underscores.")
    print("The name must start with a letter or underscore.")
    sys.exit(1)

print(f"Creating project: {project_slug}")

