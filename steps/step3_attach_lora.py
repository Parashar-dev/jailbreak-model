#!/usr/bin/env python3
"""
Step 3: Attach LoRA Adapters (LoRA of QLoRA)
Corresponds to CELL 3 in the notebook.
Configures Low-Rank Adaptation (LoRA) matrix layers.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cyber_lab_core import load_base_model, attach_lora_adapters, MockModel

def run(base_model=None, tokenizer=None, use_mock=False):
    print("=" * 70)
    print("🔧 STEP 3: Attach LoRA Adapters (LoRA of QLoRA)")
    print("=" * 70)

    if base_model is None or tokenizer is None:
        if use_mock:
            print("⚡ [MOCK MODE]: Simulating base model loading...")
            base_model, tokenizer = load_base_model(use_mock=True)
        else:
            print("⏳ Loading base model...")
            base_model, tokenizer = load_base_model(use_mock=False)

    if isinstance(base_model, MockModel):
        print("✅ Mock LoRA Adapters attached! (Simulated trainable parameters: 0.1%)")
        return base_model, tokenizer

    print("Attaching LoRA (Rank=8, Alpha=16, Targets=['q_proj', 'v_proj'])...")
    peft_model = attach_lora_adapters(base_model)

    print("\n📊 Parameter Efficiency Summary:")
    peft_model.print_trainable_parameters()
    print("✅ Step 3 Complete: LoRA Adapters attached successfully!")
    return peft_model, tokenizer

if __name__ == "__main__":
    use_mock = "--mock" in sys.argv
    run(use_mock=use_mock)
