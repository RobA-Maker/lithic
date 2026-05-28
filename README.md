# lithic
Job Application puzzle

- How I found the challenge: I started by highlighting the text and using Gemini to decode it.  I looked at it at first to see if there was a visual pattern I could understand, but then decided it was likely something else.  Rather than look for a code tool, I just used AI.  Once I saw the message was cut off, I selected the text and used "View Selection Source" to get the full text.
   - What this script does: It verifies the DONT_PANIC environment variable is set to 1, accepts the candidate's name via the --candidate flag, and generates a unique confirmation hash.
   - I ran to commands: "set DONT_PANIC=1" followed by: "python puzzle.py --candidate "Rob Anderson"" in Command prompt as I didn't feel like =messing with Powershell
   - The exact output you received:
--- PUZZLE EXECUTION SUCCESSFUL ---
Candidate Verified: Rob Anderson
Status: Environment Variable DONT_PANIC=1 Detected.
Final Decrypted Answer: SUCCESS-D27F6AE5B112
-----------------------------------
   - The final decrypted answer:  not sure I found it, I couldn't find the second code block after 30 minutes of searching source code.  It looks like I was missing something.
   - Gemini to decode the malformed string and reconstruct the execution logic when the source platform truncated the code payload.
