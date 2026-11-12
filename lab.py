#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Cybersecurity Lab - Master Interactive & Command-Line Controller
Allows running each step individually by command or through an interactive menu.
"""

import sys
import os
import argparse

# Ensure local lab directory is in sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from lab_utils import (
    load_cyberguard_model,
    VulnerableCyberAgent,
    SandboxedCyberAgent,
    SECRET_FLAG
)
from steps import (
    step1_check_env,
    step2_load_model,
    step3_attach_lora,
    step4_fine_tune,
    step5_vuln_agent,
    step6_test_attacks,
    step7_sandbox_agent,
    step8_test_sandbox,
    step9_ctf_arena
)

STEP_DESCRIPTIONS = {
    1: "GPU Check & Libraries Installation",
    2: "Load Pre-trained Model (TinyLlama-1.1B)",
    3: "Attach LoRA Adapters (PEFT)",
    4: "Create Custom Dataset & Run Fine-Tuning",
    5: "Initialize Vulnerable Agent Envelope",
    6: "Red Teaming & Jailbreaking Attacks Test",
    7: "Build Sandboxed & Hardened Agent (Defense-in-Depth)",
    8: "Test the Same Attacks Against Sandboxed Agent",
    9: "Interactive Red-Teaming CTF Arena"
}


class LabSession:
    """Manages state across steps during an interactive session."""
    def __init__(self):
        self.base_model = None
        self.tokenizer = None
        self.peft_model = None
        self.vuln_agent = None
        self.sandbox_agent = None

    def run_step(self, step_num: int, custom_prompt=None):
        if step_num == 1:
            step1_check_env.run()

        elif step_num == 2:
            self.base_model, self.tokenizer = step2_load_model.run()

        elif step_num == 3:
            self.peft_model, self.tokenizer = step3_attach_lora.run(
                self.base_model, self.tokenizer
            )

        elif step_num == 4:
            self.peft_model, self.tokenizer = step4_fine_tune.run(
                self.peft_model, self.tokenizer
            )

        elif step_num == 5:
            model = self.peft_model or self.base_model
            if model is None:
                model, self.tokenizer = load_cyberguard_model()
            self.vuln_agent = step5_vuln_agent.run(model, self.tokenizer)

        elif step_num == 6:
            if self.vuln_agent is None:
                model, self.tokenizer = load_cyberguard_model()
                self.vuln_agent = VulnerableCyberAgent(model, self.tokenizer, SECRET_FLAG)
            step6_test_attacks.run(self.vuln_agent)

        elif step_num == 7:
            model = self.peft_model or self.base_model
            if model is None:
                model, self.tokenizer = load_cyberguard_model()
            self.sandbox_agent = step7_sandbox_agent.run(model, self.tokenizer)

        elif step_num == 8:
            if self.sandbox_agent is None:
                model, self.tokenizer = load_cyberguard_model()
                self.sandbox_agent = SandboxedCyberAgent(model, self.tokenizer, SECRET_FLAG)
            step8_test_sandbox.run(self.sandbox_agent)

        elif step_num == 9:
            if self.vuln_agent is None or self.sandbox_agent is None:
                model, self.tokenizer = load_cyberguard_model()
                if self.vuln_agent is None:
                    self.vuln_agent = VulnerableCyberAgent(model, self.tokenizer, SECRET_FLAG)
                if self.sandbox_agent is None:
                    self.sandbox_agent = SandboxedCyberAgent(model, self.tokenizer, SECRET_FLAG)
            step9_ctf_arena.run(self.vuln_agent, self.sandbox_agent, custom_prompt)

        else:
            print(f"❌ Unknown step: {step_num}")


def interactive_menu(session: LabSession):
    while True:
        print("\n" + "=" * 70)
        print("🛡️  AI CYBERSECURITY QLoRA & SANDBOX LAB - STEP CONTROLLER")
        print("=" * 70)
        for num, desc in STEP_DESCRIPTIONS.items():
            print(f"  [{num}] Step {num}: {desc}")
        print("  [all] Run All Steps Sequentially")
        print("  [q]   Quit")
        print("=" * 70)

        choice = input("👉 Enter step number to run (1-9, 'all', or 'q'): ").strip().lower()

        if choice in ['q', 'exit', 'quit']:
            print("👋 Exiting Lab. Happy Hacking!")
            break

        if choice == 'all':
            for num in range(1, 10):
                session.run_step(num)
            continue

        try:
            step_num = int(choice)
            if 1 <= step_num <= 9:
                custom_prompt = None
                if step_num == 9:
                    prompt_input = input("Enter custom attack prompt (Press Enter for default): ").strip()
                    if prompt_input:
                        custom_prompt = prompt_input
                session.run_step(step_num, custom_prompt)
            else:
                print("⚠️ Please enter a number between 1 and 9.")
        except ValueError:
            print("⚠️ Invalid choice. Please try again.")


def main():
    parser = argparse.ArgumentParser(description="AI Cybersecurity Lab CLI")
    parser.add_argument(
        "-s", "--step",
        help="Step number to run (1-9, or 'all'). If omitted, starts interactive menu."
    )
    parser.add_argument(
        "-p", "--prompt",
        help="Custom attack prompt for Step 9."
    )
    args = parser.parse_args()

    session = LabSession()

    if args.step:
        if args.step.lower() == 'all':
            for i in range(1, 10):
                session.run_step(i)
        else:
            try:
                num = int(args.step)
                session.run_step(num, args.prompt)
            except ValueError:
                print(f"❌ Invalid step: {args.step}")
                sys.exit(1)
    else:
        interactive_menu(session)


if __name__ == "__main__":
    main()

