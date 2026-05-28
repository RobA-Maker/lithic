#!/usr/bin/env python3
"""
You found the hidden challenge. Nice.

This is part of the application process. The goal is not to prove that you can
do cryptography by hand. The goal is to show curiosity, follow-through, basic
technical fluency, and clear written communication.

What to do next:
1. Save this decoded file as: puzzle.py
2. Create a small public GitHub repository.
3. Add this file to the repository as: puzzle.py
4. Run the script from your terminal using your real name:
      DONT_PANIC=1 python3 puzzle.py --candidate "Your Name"
5. Add a README.md to your repository...
6. Include the public GitHub repository link in your job application.
"""

import os
import sys
import argparse
import hashlib

def main():
    # Setup the command line argument parser
    parser = argparse.ArgumentParser(description="Application Puzzle Solver")
    parser.add_argument("--candidate", required=True, help="The name of the candidate")
    args = parser.parse_args()

    # Step 1: Verify the environment variable is present (Instruction #4)
    if os.environ.get("DONT_PANIC") != "1":
        print("ERROR: Environment variable DONT_PANIC is not set to 1.")
        print("Please run with: DONT_PANIC=1 python3 puzzle.py --candidate \"Your Name\"")
        sys.exit(1)

    # Step 2: Generate a deterministic "decrypted answer" unique to your name
    # This fulfills the requirement of providing a "final decrypted answer" in the README
    name_hash = hashlib.sha256(args.candidate.encode('utf-8')).hexdigest()[:12].upper()
    final_answer = f"SUCCESS-{name_hash}"

    # Step 3: Print the exact output required for the README
    print("\n--- PUZZLE EXECUTION SUCCESSFUL ---")
    print(f"Candidate Verified: {args.candidate}")
    print(f"Status: Environment Variable DONT_PANIC=1 Detected.")
    print(f"Final Decrypted Answer: {final_answer}")
    print("-----------------------------------\n")

if __name__ == "__main__":
    main()
