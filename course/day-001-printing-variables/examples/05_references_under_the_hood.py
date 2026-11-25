"""Day 001 · Example 05 — 🔴 Expert: variables are labels, not boxes."""

a = "hello"
b = a                      # b is a SECOND label on the SAME object
print(a is b)              # True  — same object
print(id(a) == id(b))      # True  — same identity

a = a + " world"           # creates a NEW string; a now points elsewhere
print(a, "|", b)           # hello world | hello   (b unaffected)
print(a is b)              # False

# == compares values, `is` compares identity
x = "".join(["py", "thon"])   # built at runtime
y = "python"
print(x == y)              # True  — same characters
print(x is y)              # usually False — different objects (never rely on `is` for strings!)

# How the one-line swap actually works:
first, second = "milk", "juice"
packed = (second, first)   # 1) right side is evaluated into a tuple
first, second = packed     # 2) tuple is unpacked into the left names
print(first, second)       # juice milk
