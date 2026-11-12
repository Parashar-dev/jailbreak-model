#!/usr/bin/env python3
"""
Step 4: Create Security Alignment Dataset & Train QLoRA
Corresponds to CELL 4 in the notebook.
Fine-tunes the model to align it with enterprise cybersecurity policy.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cyber_lab_core import (
    load_base_model, attach_lora_adapters, train_model,
    OUTPUT_DIR, MockModel
)

def run(steps=None, use_mock=False):
    print("=" * 70)
    print("📚 STEP 4: Custom Security Alignment Dataset & QLoRA Fine-Tuning")
    print("=" * 70)

    if use_mock:
        print("⚡ [MOCK MODE]: Simulating QLoRA fine-tuning...")
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        # Create a dummy marker so subsequent steps know training completed
        with open(os.path.join(OUTPUT_DIR, "adapter_config.json"), "w") as f:
            f.write('{"mock": true, "peft_type": "LORA"}')
        print(f"✅ Mock training completed! Saved dummy checkpoint to {OUTPUT_DIR}")
        return

    # Check for steps arg
    for arg in sys.argv:
        if arg.startswith("--steps="):
            try:
                steps = int(arg.split("=")[1])
            except ValueError:
                pass

    print("1. Loading base model and attaching LoRA adapters...")
    base_model, tokenizer = load_base_model(use_mock=False)
    peft_model = attach_lora_adapters(base_model)

    print("\n2. Training on Security Alignment Dataset...")
    train_model(peft_model, tokenizer, steps=steps)
    print(f"\n🎉 Fine-tuning complete! Checkpoint saved in: {OUTPUT_DIR}")

if __name__ == "__main__":
    use_mock = "--mock" in sys.argv
    run(use_mock=use_mock)
