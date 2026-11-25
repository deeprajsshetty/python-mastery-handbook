"""Solution 04 — Name stats."""

name = input("What is your name?\n").strip().title()   # methods can be chained left→right
print(f"Hello, {name}!")
print(f"Your name has {len(name)} characters.")
