"""Solution 03 — Fix the bugs.

Bug                                     → Error             → Fix
1  mismatched quotes  " ... '           → SyntaxError       → use the same quote on both ends
2  leading spaces                       → IndentationError  → start at column 0
3  Print with capital P                 → NameError         → Python is case-sensitive: print
4  missing opening quote before `your`  → SyntaxError       → "Line numbers are " + "your map"
5  extra closing bracket                → SyntaxError       → remove one )
"""

print("Debugging is a superpower")
print("Errors tell you WHERE and WHAT")
print("Read the last line first")
print("Line numbers are " + "your map")
print("Fix one bug at a time")
