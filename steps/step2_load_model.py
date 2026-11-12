#!/usr/bin/env python3
"""
Step 2: Load Pre-trained Model (TinyLlama-1.1B)
Corresponds to CELL 2 in the notebook.
Loads TinyLlama-1.1B-Chat-v1.0 with auto-detection for GPU (4-bit QLoRA) or CPU.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cyber_lab_core import load_base_model, MODEL_ID, get_device

def run(use_mock=False):
    print("=" * 70)
    print("📥 STEP 2: Load Pre-trained Base Model (TinyLlama-1.1B)")
    print("=" * 70)
    print(f"Target Model: {MODEL_ID}")

    device, has_cuda = get_device()
    print(f"🖥️ Execution Target: {device.upper()}")

    if use_mock:
        print("⚡ [MOCK MODE]: Simulating model loading for fast test...")
        model, tokenizer = load_base_model(use_mock=True)
        print("✅ Mock Model ready!")
        return model, tokenizer

    try:
        model, tokenizer = load_base_model(use_mock=False)
        total_params = sum(p.numel() for p in model.parameters())
        print(f"\n📊 Model Statistics:")
        print(f"  • Total Parameters: {total_params:,}")
        print(f"  • Vocab Size:       {tokenizer.vocab_size:,}")
        print("\n✅ Step 2 Complete: Base Model and Tokenizer are ready!")
        return model, tokenizer
    except Exception as e:
        print(f"\n❌ Error loading model: {e}")
        print("💡 TIP: You can run in instant test mode using: ./lab 2 --mock")
        sys.exit(1)

if __name__ == "__main__":
    use_mock = "--mock" in sys.argv
    run(use_mock=use_mock)
