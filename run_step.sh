#!/bin/bash
# ====================================================================
# AI Cybersecurity Lab Launcher Script
# Automatically uses the lab virtual environment (.venv)
# ====================================================================

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VENV_PY="$SCRIPT_DIR/.venv/bin/python"

if [ ! -f "$VENV_PY" ]; then
    VENV_PY="python3"
fi

exec "$VENV_PY" "$SCRIPT_DIR/lab_runner.py" "$@"
