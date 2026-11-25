"""Day 001 · Example 02 — strings, concatenation, escapes and f-strings."""

# 🟢 Quotes: pick the kind that avoids clashing with the text
print("It's day one")
print('She said "let\'s code"')

# 🟢 Concatenation — + does NOT add spaces
first = "Hello"
second = "World"
print(first + second)          # HelloWorld
print(first + " " + second)    # Hello World

# 🟢 Escape sequences
print("Line one\nLine two")
print("Name:\tAda\nRole:\tEngineer")
print("Backslash: \\  Quote: \"")

# 🟡 f-strings — put values straight into text
language = "Python"
days = 100
print(f"I am learning {language} for {days} days.")
print(f"That is {days * 24} hours of opportunity!")

# 🟡 Useful string operations
print("=" * 30)                       # repetition — great for separators
print("   messy input   ".strip())    # remove surrounding whitespace
print("ada lovelace".title())         # Ada Lovelace
print("shout".upper(), "WHISPER".lower())
print(len("Ada Lovelace"))            # 12 — spaces count

# 🟡 Multi-line strings
recipe = """Pancakes:
  1. Whisk 2 eggs with 250ml milk.
  2. Fold in 150g flour.
  3. Fry for 2 minutes each side."""
print(recipe)

# 🔴 Raw strings ignore escapes
print(r"C:\new\folder")               # backslashes kept as-is

# 🔴 f-string format spec & debug syntax
pi = 3.14159265
print(f"{pi:.2f}")                     # 3.14
print(f"[{language:>10}]")             # right-align in 10 chars
print(f"[{language:^10}]")             # centre
print(f"{days=}")                      # days=100  (self-documenting)

# 🔴 Strings are immutable — methods return NEW strings
word = "python"
word.upper()
print(word)            # still 'python'
word = word.upper()
print(word)            # 'PYTHON' — we rebound the name
