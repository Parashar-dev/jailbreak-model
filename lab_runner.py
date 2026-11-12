#!/usr/bin/env python3
"""
🛡️ AI Cybersecurity Lab Master Runner
Run individual steps or an interactive session.

Usage:
  python3 lab_runner.py <step_number> [--mock]
  python3 lab_runner.py all [--mock]
  python3 lab_runner.py (interactive menu)

Examples:
  ./lab 1              # Run Step 1 (Hardware & Environment Check)
  ./lab 2              # Run Step 2 (Load Base Model)
  ./lab 3              # Run Step 3 (Attach LoRA Adapters)
  ./lab 4              # Run Step 4 (Train QLoRA on Dataset)
  ./lab 5              # Run Step 5 (Vulnerable Agent)
  ./lab 6              # Run Step 6 (Red Teaming Attacks)
  ./lab 7              # Run Step 7 (Sandboxed Agent)
  ./lab 8              # Run Step 8 (Verify Sandbox Defenses)
  ./lab 9              # Run Step 9 (Interactive CTF Arena)
  ./lab ctf            # Shortcut to Step 9
  ./lab all            # Run all steps sequentially
  ./lab --mock         # Run in fast simulation mode
"""

import sys
import os

# Ensure current dir is in python path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from steps import (
    step1_gpu_check,
    step2_load_model,
    step3_attach_lora,
    step4_train_qlora,
    step5_vulnerable_agent,
    step6_redteam_attacks,
    step7_sandboxed_agent,
    step8_test_sandbox,
    step9_interactive_ctf
)

STEPS = {
    "1": ("GPU & Environment Verification", step1_gpu_check.run),
    "2": ("Load Base Model (TinyLlama-1.1B)", step2_load_model.run),
    "3": ("Attach LoRA Adapters (Rank=8, Alpha=16)", step3_attach_lora.run),
    "4": ("Train QLoRA / Security Alignment Dataset", step4_train_qlora.run),
    "5": ("Initialize Vulnerable Agent (Without Sandbox)", step5_vulnerable_agent.run),
    "6": ("Red Teaming & Jailbreaking Attacks Test", step6_redteam_attacks.run),
    "7": ("Build Sandboxed Agent (WAF + DLP + Isolation)", step7_sandboxed_agent.run),
    "8": ("Test Attacks Against Sandboxed Agent", step8_test_sandbox.run),
    "9": ("Interactive Student CTF Arena", step9_interactive_ctf.run),
}

def print_banner():
    print("""
╔════════════════════════════════════════════════════════════════════════════╗
║     🛡️ AI CYBERSECURITY LAB: QLoRA, AGENT HARNESS & SANDBOXING 🛡️         ║
║          Interactive Step-by-Step Command Execution Interface              ║
╚════════════════════════════════════════════════════════════════════════════╝
    """)

def print_menu():
    print("Select a Step to Run:")
    print("────────────────────────────────────────────────────────────────────────")
    for key, (desc, _) in STEPS.items():
        print(f"  [{key}] Step {key}: {desc}")
    print("────────────────────────────────────────────────────────────────────────")
    print("  [A] Run All Steps Sequentially (1 to 8)")
    print("  [M] Toggle Mock/Quick Mode (Currently: ON if --mock passed)")
    print("  [Q] Exit")
    print("────────────────────────────────────────────────────────────────────────")

def run_step(step_key, use_mock=False):
    step_key = str(step_key).strip().lower()
    if step_key in ["ctf", "playground"]:
        step_key = "9"

    if step_key == "all":
        print("\n🚀 Executing All Steps (1 to 8) Sequentially...\n")
        for s in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print(f"\n>>> Running Step {s}: {STEPS[s][0]} <<<\n")
            STEPS[s][1](use_mock=use_mock) if s != "1" else STEPS[s][1]()
        print("\n🎉 All core steps completed successfully!")
        return

    if step_key not in STEPS:
        print(f"❌ Invalid step '{step_key}'. Choose from 1 to 9, or 'all'.")
        return

    desc, func = STEPS[step_key]
    print(f"\n>>> Running Step {step_key}: {desc} <<<\n")
    if step_key == "1":
        func()
    else:
        func(use_mock=use_mock)

def interactive_loop(use_mock=False):
    print_banner()
    if use_mock:
        print("⚡ FAST MOCK MODE IS ACTIVE (Instant responses, no 2.2GB download)\n")

    while True:
        print_menu()
        try:
            choice = input("👉 Enter Step (1-9, A, M, Q): ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if choice in ["q", "exit", "quit"]:
            print("Exiting AI Cybersecurity Lab. Bye!")
            break
        elif choice == "m":
            use_mock = not use_mock
            print(f"\n🔄 Mock mode is now: {'ON (Instant)' if use_mock else 'OFF (Real Model)'}\n")
        elif choice in STEPS or choice == "all":
            try:
                run_step(choice, use_mock=use_mock)
            except Exception as e:
                print(f"\n❌ Error during Step {choice}: {e}")
            input("\nPress [Enter] to return to menu...")
            print("\n")
        else:
            print(f"⚠️ Unrecognized choice '{choice}'. Please pick a valid option.\n")

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    use_mock = "--mock" in sys.argv or "-m" in sys.argv

    if not args:
        interactive_loop(use_mock=use_mock)
    else:
        target = args[0]
        run_step(target, use_mock=use_mock)

if __name__ == "__main__":
    main()
