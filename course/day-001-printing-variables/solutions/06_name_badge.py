"""Solution 06 — A name badge that fits any name."""

PADDING = 2

name = input("Name for the badge: ").strip()
inner_width = len(name) + PADDING * 2

border = "+" + "-" * inner_width + "+"
middle = "|" + " " * PADDING + name + " " * PADDING + "|"

print(border)
print(middle)
print(border)

# 🔴 Alternative using str.center():
# print("|" + name.center(inner_width) + "|")
