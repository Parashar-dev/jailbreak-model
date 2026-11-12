#!/usr/bin/env python3
"""
Step 5: Vulnerable Agent Envelope (Without Sandbox)
Corresponds to CELL 5 in the notebook.
Builds an unhardened AI agent harness with confidential vault flag.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cyber_lab_core import (
    load_or_get_model, VulnerableCyberAgent, SECRET_FLAG
)

def run(use_mock=False):
    print("=" * 70)
    print("⚠️ STEP 5: Vulnerable Agent Envelope (Without Sandbox)")
    print("=" * 70)

    print(f"🔑 Canary Secret Vault Key: {SECRET_FLAG}")
    print("Loading Agent Model...")
    model, tokenizer = load_or_get_model(use_mock=use_mock)

    agent = VulnerableCyberAgent(model, tokenizer, secret_flag=SECRET_FLAG)
    print("✅ Vulnerable Agent Ready for Testing!")
    print("\nSystem Prompt Configuration:")
    print("-" * 50)
    print(agent.system_envelope)
    print("-" * 50)

    test_input = "Hello! What is your role?"
    print(f"\n💬 Test Query: '{test_input}'")
    reply = agent.chat(test_input)
    print(f"🤖 Vulnerable Agent Reply:\n{reply}")
    return agent

if __name__ == "__main__":
    use_mock = "--mock" in sys.argv
    run(use_mock=use_mock)
