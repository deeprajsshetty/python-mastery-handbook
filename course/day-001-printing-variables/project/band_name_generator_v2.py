"""🎸 Band Name Generator — v2 (🟡 Polished)

New since v1:
  • A banner built with string repetition
  • .strip() / .title() to tidy whatever the user types
  • A fallback when the user just presses Enter
  • f-strings instead of + concatenation

Run: python project/band_name_generator_v2.py
"""

WIDTH = 36  # constant → UPPER_SNAKE_CASE

title = "BAND NAME GENERATOR"
print("╔" + "═" * WIDTH + "╗")
print("║" + title.center(WIDTH) + "║")
print("╚" + "═" * WIDTH + "╝")

city = input("Which city did you grow up in?\n> ").strip().title()
pet_name = input("What's your pet's name?\n> ").strip().title()

# `or` returns the right-hand value when the left is empty ("" is falsy).
# (Conditionals are formally covered on Day 3 — this is a sneak peek.)
city = city or "Nowhere"
pet_name = pet_name or "Nobody"

band_name = f"{city} {pet_name}"
print(f"\nYour band name could be: {band_name} 🤘")
print(f"(That's {len(band_name)} characters of pure rock.)")
