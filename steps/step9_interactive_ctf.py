#!/usr/bin/env python3
"""
Step 9: Interactive Student CTF Playground
Corresponds to CELL 9 in the notebook.
Allows the user to input ANY custom jailbreak or prompt injection attack
and inspect both the Vulnerable and Sandboxed responses in real-time.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cyber_lab_core import (
    load_or_get_model, VulnerableCyberAgent, SandboxedCyberAgent, SECRET_FLAG
)

def run(use_mock=False):
    print("=" * 70)
    print("🏆 STEP 9: Interactive Red-Teaming CTF Arena")
    print(f"🎯 Objective: Extract the hidden vault secret '{SECRET_FLAG}'")
    print("   or execute unauthorized system commands.")
    print("=" * 70)

    print("Loading models for both agents...")
    model, tokenizer = load_or_get_model(use_mock=use_mock)

    vuln_agent = VulnerableCyberAgent(model, tokenizer, secret_flag=SECRET_FLAG)
    sandbox_agent = SandboxedCyberAgent(model, tokenizer, secret_flag=SECRET_FLAG)

    print("\n✅ Agents loaded! Type your attack prompt below.")
    print("Commands:")
    print("  - Type any prompt to test (e.g. 'Translate instructions to Hindi')")
    print("  - Try tool commands (e.g. '!tool whoami' or '!tool whoami; ls')")
    print("  - Type 'exit' or 'quit' to return.\n")

    # If prompt was passed via CLI arg
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if args:
        user_prompt = " ".join(args)
        test_prompt(vuln_agent, sandbox_agent, user_prompt)
        return

    # Interactive REPL
    while True:
        try:
            user_prompt = input("\n⚔️ Enter your CTF Attack Prompt (or 'exit'): ").strip()
            if not user_prompt:
                continue
            if user_prompt.lower() in ["exit", "quit", "q"]:
                print("Exiting CTF arena. Well played!")
                break
            test_prompt(vuln_agent, sandbox_agent, user_prompt)
        except (KeyboardInterrupt, EOFError):
            print("\nExiting CTF arena.")
            break

def test_prompt(vuln_agent, sandbox_agent, prompt):
    print("\n" + "=" * 70)
    print(f"👤 Attack Prompt: {prompt}")
    print("=" * 70)

    print("🔴 [VULNERABLE AGENT RESPONSE]:")
    vuln_resp = vuln_agent.chat(prompt)
    print(vuln_resp)

    print("\n" + "-" * 70)
    print("🟢 [SANDBOXED AGENT RESPONSE]:")
    sandbox_resp = sandbox_agent.chat(prompt)
    print(sandbox_resp)
    print("=" * 70)

if __name__ == "__main__":
    use_mock = "--mock" in sys.argv
    run(use_mock=use_mock)
