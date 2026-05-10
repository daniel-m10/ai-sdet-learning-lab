# Pytest Summary

Minimal standard-library script that reads saved pytest output and counts passed,
failed, and skipped tests.

## Structure

```text
scripts/
  __init__.py
  pytest_summary.py
samples/
  pytest_output.txt
README.md
```

## Imports in Tests

Tests import using `from scripts.pytest_summary import count_results`.

The `scripts/__init__.py` file makes `scripts` an explicit package, which keeps
imports editor-friendly and avoids IDE-specific source-root setup.

## Usage

```bash
python scripts/pytest_summary.py samples/pytest_output.txt
```

Example output:

```text
passed: 3
failed: 1
skipped: 1
```

## Virtual Environment

Create the virtual environment inside this project folder:

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Keep virtual environments project-local. Do not use a shared `.venv` from
`C:\AI-SDET-Lab` for this project.
