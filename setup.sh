#!/usr/bin/env bash
# ====================================================================
# AI Cybersecurity Lab - One-Click Environment Setup Script
# Installs all required packages, virtual environment, and Jupyter kernel
# ====================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "======================================================================"
echo "🛡️  AI Cybersecurity Lab: Environment Setup"
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
    echo "📦 Creating virtual environment (.venv)..."
    $PYTHON_CMD -m venv .venv
else
    echo "ℹ️ Existing .venv detected. Using current virtual environment."
fi

VENV_PY="$SCRIPT_DIR/.venv/bin/python"
VENV_PIP="$SCRIPT_DIR/.venv/bin/pip"

# Step 3: Upgrade pip and install PyTorch
echo "⬇️ Checking and installing PyTorch..."
if command -v nvidia-smi &>/dev/null; then
    echo "🎮 NVIDIA GPU detected. Installing PyTorch with CUDA support..."
    $VENV_PIP install --upgrade pip
    $VENV_PIP install torch --timeout 120 --retries 10
else
    echo "🖥️ CPU environment detected. Installing CPU-optimized PyTorch..."
    $VENV_PIP install --upgrade pip
    $VENV_PIP install --timeout 120 --retries 10 --extra-index-url https://download.pytorch.org/whl/cpu torch
fi

# Step 4: Install Dependencies from requirements.txt
echo "📦 Installing AI libraries (transformers, peft, datasets, accelerate, ipykernel)..."
$VENV_PIP install -r requirements.txt --timeout 120 --retries 10

# Step 5: Register Jupyter Kernel for Notebooks
echo "📓 Registering Jupyter Kernel 'Python (AI Cyber Lab)'..."
$VENV_PY -m ipykernel install --user --name=ai_lab_venv --display-name "Python (AI Cyber Lab)"

# Step 6: Make executable scripts
chmod +x lab lab_runner.py lab.py run_step.sh setup.sh 2>/dev/null || true

echo "======================================================================"
echo "🎉 Setup Complete! Verifying environment with Step 1..."
echo "======================================================================"

$VENV_PY "$SCRIPT_DIR/lab_runner.py" 1
