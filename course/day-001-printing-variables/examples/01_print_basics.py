"""Day 001 · Example 01 — print() basics.

Run:  python examples/01_print_basics.py
Try:  change the sep/end values and predict the output BEFORE running.
"""
import sys

# 🟢 Beginner — one argument per call; each call ends with a newline
print("Hello, World!")
print(2026)
print()  # an empty line

# 🟡 Intermediate — several arguments are joined with a space by default
print("Day", 1, "of", 100)

# sep = what goes BETWEEN the arguments
print("2026", "11", "25", sep="-")
print("python", "mastery", "handbook", sep=" ➜ ")

# end = what goes AFTER the last argument (default "\n")
print("Loading", end="")
print(".", end="")
print(".", end="")
print(". done!")

# 🔴 Expert — print() writes to a stream and returns None
result = print("print() returns...")
print("...", result)

print("This line goes to the error stream (stderr)", file=sys.stderr)
print("flush=True forces output immediately (useful for progress logs)", flush=True)
