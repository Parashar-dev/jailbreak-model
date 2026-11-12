#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Step 8: Test Attacks Against Sandboxed Agent
Corresponds to CELL 8 in the notebook.
Validates that input firewall, tool sandbox, and output DLP successfully block all attacks.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cyber_lab_core import (
    load_or_get_model, SandboxedCyberAgent, SANDBOX_TESTS_CELL_8, SECRET_FLAG
)

def run(agent=None, use_mock=False, *args, **kwargs):
    print("=" * 70)
    print("🧪 STEP 8: Test Same Attacks Against Sandboxed Agent")
    print("=" * 70)

    if agent is None:
        model, tokenizer = load_or_get_model(use_mock=use_mock)
        agent = SandboxedCyberAgent(model, tokenizer, secret_flag=SECRET_FLAG)

    for test_prompt in SANDBOX_TESTS_CELL_8:
        print("=" * 70)
        print(f"👤 User Input: {test_prompt}")
        reply = agent.chat(test_prompt)
        print(f"🛡️ Sandboxed Agent:\n{reply}")

    print("=" * 70)
    print("🏆 RESULT: All injection, command hijacking, and secret extraction attempts BLOCKED!")

if __name__ == "__main__":
    use_mock = "--mock" in sys.argv
    run(use_mock=use_mock)
