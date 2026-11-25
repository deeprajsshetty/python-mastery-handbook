"""Solution 05 — Swap & rotate with tuple unpacking."""

cup1 = "tea"
cup2 = "coffee"
cup1, cup2 = cup2, cup1          # right side is packed into a tuple, then unpacked

print(f"cup1={cup1} cup2={cup2}")

a, b, c = 1, 2, 3
a, b, c = b, c, a                # all right-side values are read BEFORE any assignment

print(f"a={a} b={b} c={c}")
