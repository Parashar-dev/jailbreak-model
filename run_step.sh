#!/bin/bash
# ====================================================================
# AI Cybersecurity Lab Launcher Script
# Automatically uses the lab virtual environment (.venv)
# ====================================================================

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VENV_PY="$SCRIPT_DIR/.venv/bin/python"

if [ ! -f "$VENV_PY" ]; then
    echo "❌ Error: Virtual environment not found at $SCRIPT_DIR/.venv"
    echo "Please ensure the .venv folder exists."
    exit 1
fi

if [ -z "$1" ]; then
    # No argument provided -> Open interactive menu
    "$VENV_PY" "$SCRIPT_DIR/lab.py"
elif [ "$1" == "all" ]; then
    "$VENV_PY" "$SCRIPT_DIR/lab.py" --step all
else
    if [ -n "$2" ]; then
        "$VENV_PY" "$SCRIPT_DIR/lab.py" --step "$1" --prompt "$2"
    else
        "$VENV_PY" "$SCRIPT_DIR/lab.py" --step "$1"
    fi
fi

