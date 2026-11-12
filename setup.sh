#!/usr/bin/env bash
# ====================================================================
# AI Cybersecurity Lab - 100% Pure Local CLI Setup Script
# Configures local virtual environment and dependencies (No Jupyter/Colab needed)
# ====================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "======================================================================"
echo "🛡️  AI Cybersecurity Lab: Pure Local Terminal Setup"
echo "======================================================================"

# Step 1: Detect Python 3
if command -v python3 &>/dev/null; then
    PYTHON_CMD="python3"
elif command -v python &>/dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ Error: Python 3 is not installed or not in PATH."
    exit 1
fi

echo "✅ Python detected: $($PYTHON_CMD --version)"

# Step 2: Create Virtual Environment if not exists
if [ ! -d ".venv" ]; then
    echo "📦 Creating local virtual environment (.venv)..."
    $PYTHON_CMD -m venv .venv
else
    echo "ℹ️ Existing local .venv detected. Using current environment."
fi

VENV_PY="$SCRIPT_DIR/.venv/bin/python"
VENV_PIP="$SCRIPT_DIR/.venv/bin/pip"

# Step 3: Upgrade pip and install PyTorch
echo "⬇️ Checking and configuring PyTorch..."
if command -v nvidia-smi &>/dev/null; then
    echo "🎮 NVIDIA GPU detected. Configuring PyTorch with CUDA support..."
    $VENV_PIP install --upgrade pip
    $VENV_PIP install torch --timeout 120 --retries 10
else
    echo "🖥️ CPU environment detected. Configuring CPU-optimized PyTorch..."
    $VENV_PIP install --upgrade pip
    $VENV_PIP install --timeout 120 --retries 10 --extra-index-url https://download.pytorch.org/whl/cpu torch
fi

# Step 4: Install Dependencies from requirements.txt
echo "📦 Installing AI libraries (transformers, peft, datasets, accelerate)..."
$VENV_PIP install -r requirements.txt --timeout 120 --retries 10

# Step 5: Ensure execution permissions for CLI tools
chmod +x lab lab_runner.py lab.py run_step.sh setup.sh 2>/dev/null || true

echo "======================================================================"
echo "🎉 Pure Local Setup Complete! Verifying environment with Step 1..."
echo "======================================================================"

$VENV_PY "$SCRIPT_DIR/lab_runner.py" 1
