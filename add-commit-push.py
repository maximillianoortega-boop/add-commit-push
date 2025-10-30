#!/usr/bin/env python3
"""
add-commit-push.py
Automates the process of running 'git add .', 'git commit -m "msg"', and 'git push'.
Usage:
    python add-commit-push.py [-m "your message"] [-f]
"""

import argparse
import subprocess
import sys

# ====== CONSTANTS ======
ADD_CMD = ["git", "add", "."]
PUSH_CMD = ["git", "push"]
STATUS_CMD = ["git", "status"]

# ====== FUNCTIONS ======
def run_command(command):
    """Prints a command, runs it, skips a line, and prints the result."""
    print(f"\n> {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    print("-" * 40)


def main():
    # ====== ARGUMENT PARSING ======
    parser = argparse.ArgumentParser(description="Automate git add, commit, and push.")
    parser.add_argument("-m", "--message", type=str, default="Auto commit",
                        help="Commit message for git commit.")
    parser.add_argument("-f", "--force", action="store_true",
                        help="Skip confirmation step and force execution.")
    args = parser.parse_args()

    # ====== DISPLAY GIT STATUS ======
    print("git status:")
    subprocess.run(STATUS_CMD)

    # ====== PREPARE COMMANDS ======
    commit_cmd = ["git", "commit", "-m", args.message]
    commands = [ADD_CMD, commit_cmd, PUSH_CMD]

    print("\nCommands to be executed:")
    for cmd in commands:
        print(" ", " ".join(cmd))

    # ====== CONFIRM EXECUTION ======
    if not args.force:
        confirm = input("\nExecute these commands? (y/n): ").strip().lower()
        if confirm != "y":
            print("Aborted.")
            sys.exit(0)

    # ====== EXECUTE COMMANDS ======
    for cmd in commands:
        run_command(cmd)


if __name__ == "__main__":
    main()
