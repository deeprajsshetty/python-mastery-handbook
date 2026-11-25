"""Day 001 · Example 03 — input() and len().

Run interactively:   python examples/03_input_basics.py
Run with piped input (how tests do it):
    printf 'Ada\n' | python examples/03_input_basics.py
"""

# 🟢 input() pauses, shows the prompt, and returns what the user typed
name = input("What is your name?\n> ")
print("Hello " + name + "!")

# 🟡 Clean it up and use an f-string
clean_name = name.strip().title()
print(f"Nice to meet you, {clean_name}.")

# 🟢 len() counts characters
print(f"Your name has {len(clean_name)} characters.")

# 🟡 Code runs inside-out: input() runs first, then len(), then print()
# print(len(input("Type anything: ")))

# 🔴 input() ALWAYS returns str — even for digits
print(f"type of your answer: {type(name).__name__}")
