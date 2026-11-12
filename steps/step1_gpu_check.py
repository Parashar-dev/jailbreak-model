#!/usr/bin/env python3
"""
Step 1: GPU Check & Environment Verification
Corresponds to CELL 1 in the notebook.
"""

import sys
import os
import subprocess
import torch

def run():
    print("=" * 70)
    print("🔍 STEP 1: GPU Check & Environment Verification")
    print("=" * 70)

    # 1. GPU Check
    has_cuda = torch.cuda.is_available()
    print(f"PyTorch Version: {torch.__version__}")
    print(f"CUDA Available:  {has_cuda}")

    if has_cuda:
        gpu_name = torch.cuda.get_device_name(0)
        gpu_mem = torch.cuda.get_device_properties(0).total_memory / (1024**3)
        print(f"✅ GPU Detected: {gpu_name} ({gpu_mem:.2f} GB VRAM)")
        try:
            nvidia_smi = subprocess.run(["nvidia-smi"], capture_output=True, text=True)
            print(nvidia_smi.stdout)
        except Exception:
            pass
    else:
        print("ℹ️ No CUDA GPU detected. Running in optimized CPU mode.")
        print("💡 The lab scripts automatically adapt training & inference for CPU!")

    # 2. Check essential libraries
    print("\n📦 Checking Required AI Libraries:")
    libs = ["transformers", "peft", "datasets", "accelerate"]
    all_ok = True
    for lib in libs:
        try:
            mod = __import__(lib)
            version = getattr(mod, "__version__", "installed")
            print(f"  ✅ {lib:<15} : {version}")
        except ImportError:
            print(f"  ❌ {lib:<15} : MISSING")
            all_ok = False

    if all_ok:
        print("\n🎉 Environment is READY for the next step!")
    else:
        print("\n⚠️ Some libraries are missing. Run: pip install -r requirements.txt")

if __name__ == "__main__":
    run()
