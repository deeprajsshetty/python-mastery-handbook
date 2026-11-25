"""Day 001 · Example 04 — variables, reassignment and swapping."""

# 🟢 Create and reassign
player = "Ada"
print(player)
player = "Grace"
print(player)

# 🟢 Swap with a temporary variable (works in every language)
glass1 = "milk"
glass2 = "juice"
temp = glass1
glass1 = glass2
glass2 = temp
print(f"glass1={glass1}, glass2={glass2}")

# 🟡 Pythonic swap — tuple packing/unpacking
glass1, glass2 = glass2, glass1
print(f"glass1={glass1}, glass2={glass2}")

# 🟡 Rotate THREE values in one line
a, b, c = "🍎", "🍌", "🍒"
a, b, c = b, c, a
print(a, b, c)                 # 🍌 🍒 🍎

# 🟡 Multiple & chained assignment
x, y, z = 1, 2, 3
total = count = 0
print(x, y, z, total, count)

# 🟡 Dynamic typing — the NAME has no type; the VALUE does
value = "ten"
print(type(value).__name__)    # str
value = 10
print(type(value).__name__)    # int

# 🔴 Type hints document intent (not enforced at runtime)
city: str = "Mumbai"
print(city)
