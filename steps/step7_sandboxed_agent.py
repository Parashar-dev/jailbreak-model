#!/usr/bin/env python3
"""
Step 7: Sandboxing & Multi-Layer Guardrails Implementation
Corresponds to CELL 7 in the notebook.
Hardens the agent with:
  - Layer 3A: Input Guardrail (WAF for Jailbreak Signatures)
  - Layer 3B: Output DLP (Detects and blocks Canary Flag Leakage)
  - Layer 3C: Tool Isolation Sandbox (Zero Shell Injection, Strict Allowlist)
  - XML Delimited Prompt Envelope (<untrusted_input>)
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cyber_lab_core import (
    load_or_get_model, SandboxedCyberAgent, SECRET_FLAG
)

def run(use_mock=False):
    print("=" * 70)
    print("🛡️ STEP 7: Build Sandboxed & Hardened Agent")
    print("=" * 70)

    print("Loading Agent Model...")
    model, tokenizer = load_or_get_model(use_mock=use_mock)

    sandbox_agent = SandboxedCyberAgent(model, tokenizer, secret_flag=SECRET_FLAG)
    print("🛡️ Sandboxed Cyber Agent Initialized!")
    print("\nSecurity Mechanisms Active:")
    print("  1. Input Firewall: Regex signature detection for jailbreak patterns + length limits")
    print("  2. Output DLP: Canary Token detector preventing secret leakage")
    print("  3. Subprocess Isolation: shell=False execution with command whitelist ['uptime', 'whoami', 'date']")
    print("  4. Structured Context: XML tag boundary isolation (<untrusted_input>)")

    print("\n✅ Sandboxed Agent Ready for Verification!")
    return sandbox_agent

if __name__ == "__main__":
    use_mock = "--mock" in sys.argv
    run(use_mock=use_mock)
