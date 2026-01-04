"""Post-generation hooks for cookiecutter template."""

import os
import shutil
import subprocess

# Template options
include_frontend = "{{ cookiecutter.include_frontend }}" == "yes"
include_api = "{{ cookiecutter.include_api }}" == "yes"
include_docs = "{{ cookiecutter.include_docs }}" == "yes"
auto_setup = "{{ cookiecutter.auto_setup }}" == "yes"
init_git = "{{ cookiecutter.init_git }}" == "yes"
github_repo_url = "{{ cookiecutter.github_repo_url }}".strip()


def remove_dir(path: str) -> None:
    """Remove a directory if it exists."""
    if os.path.exists(path):
        shutil.rmtree(path)


def remove_file(path: str) -> None:
    """Remove a file if it exists."""
    if os.path.exists(path):
        os.remove(path)


def run_command(cmd: list[str], capture: bool = True) -> tuple[bool, str]:
    """Run a command and return (success, output)."""
    try:
        result = subprocess.run(cmd, capture_output=capture, text=True)
        return result.returncode == 0, result.stderr or result.stdout or ""
    except FileNotFoundError:
        return False, f"Command not found: {cmd[0]}"


def check_command(cmd: str) -> bool:
    """Check if a command is available."""
    return shutil.which(cmd) is not None


def main() -> None:
    """Main post-generation hook."""
    # Remove optional directories based on choices
    if not include_frontend:
        remove_dir("frontend")

    if not include_api:
        remove_dir("api")

    if not include_docs:
        remove_dir("docs")
        remove_file("mkdocs.yml")

    print("\n✨ Project '{{ cookiecutter.project_slug }}' created!")

    # Check for required tools
    has_uv = check_command("uv")
    has_git = check_command("git")

    git_initialized = False
    setup_done = False

    # Warn about missing tools
    if auto_setup and not has_uv:
        print("\n⚠️  'uv' not found. Install: https://github.com/astral-sh/uv")

    if init_git and not has_git:
        print("\n⚠️  'git' not found. Please install git.")

    # Step 1: Initialize git first (needed for pre-commit)
    if init_git and has_git:
        print("\n🔧 Initializing git...")
        success, _ = run_command(["git", "init"])
        if success:
            print("    ✅ Git initialized")
            git_initialized = True

    # Step 2: Install dependencies
    if auto_setup and has_uv:
        print("\n📦 Installing dependencies...")
        success, _ = run_command(["uv", "sync", "--all-extras"])
        if success:
            print("    ✅ Dependencies installed")
            setup_done = True

            # Install pre-commit hooks (requires git)
            if git_initialized:
                success, _ = run_command(["uv", "run", "pre-commit", "install"])
                if success:
                    print("    ✅ Pre-commit hooks installed")

    # Step 3: Create initial commit
    if git_initialized:
        print("\n📝 Creating initial commit...")

        # Stage all files
        run_command(["git", "add", "-A"])

        # First commit attempt - pre-commit may modify files
        success, output = run_command(["git", "commit", "-m", "🎉 Initial commit"])

        if not success and "files were modified" in output:
            # Pre-commit modified files, re-stage and commit
            print("    → Pre-commit fixed some files, re-committing...")
            run_command(["git", "add", "-A"])
            success, _ = run_command(["git", "commit", "-m", "🎉 Initial commit"])

        if success:
            print("    ✅ Initial commit created")
        else:
            # Try without pre-commit hooks as fallback
            success, _ = run_command(["git", "commit", "-m", "🎉 Initial commit", "--no-verify"])
            if success:
                print("    ✅ Initial commit created")

        # Add remote if provided
        if github_repo_url:
            success, _ = run_command(["git", "remote", "add", "origin", github_repo_url])
            if success:
                print(f"    ✅ Remote added: {github_repo_url}")

    # Final instructions
    print("\n" + "=" * 50)
    print("🚀 Ready to go!")
    print("=" * 50)
    print(f"\n  cd {{ cookiecutter.project_slug }}")

    if not setup_done:
        print("  uv sync")

    if not git_initialized:
        print("  git init && git add . && git commit -m 'Initial commit'")
    elif not setup_done:
        print("  uv run pre-commit install")

    if git_initialized and github_repo_url:
        print("  git push -u origin main")

    print("  make run\n")


if __name__ == "__main__":
    main()
