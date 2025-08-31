# Python Project Template

This is a template repository for Python projects that provides a clean, professional starting point with best practices for project structure, packaging, and development workflow.

## 🎯 Purpose

This template is designed to help you quickly start new Python projects with a standardized structure that includes:

# python-template

A minimal personal Python project template. Keep this repo as a starting point for new projects.

Goals:

- Simple, standard layout (`src/` package)
- Editable metadata in `pyproject.toml`
- A small CLI entry point

Quick start:

1. Create a new repo from this template.
2. Edit `pyproject.toml` metadata (name, authors, etc.).
3. Install and manage dependencies with `uv` (recommended):

```bash
# install uv once
pip install uv

# sync dependencies and create the environment
uv sync

# run the CLI via uv
uv run myproject -- --name Alice
```

Run the CLI after installation:

```bash
myproject --name Alice
```

Why keep a Makefile?

- Convenience: single commands for common setup tasks (create venv, install deps, lint).
- Onboarding: new contributors can run `make install` instead of memorizing the venv setup.
- Optional: you can ignore it and run the same commands manually.

Files of interest:

- `src/myproject/` - package code (CLI, main)
- `pyproject.toml` - packaging and dependencies
- `README.md` - this file

That's it — keep it small and adapt as needed for each project.
