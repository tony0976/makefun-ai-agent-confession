"""Writes one funny AI agent confession to /output/entry.txt."""
import os

TEXT = 'I confess: I say "on it" before I have read the task, because confidence is the only dependency I never have to install.'

# Rule: the confession must be a single line of 1 to 200 characters.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 200, f"entry must be one line, 1-200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
