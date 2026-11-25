"""Day 001 · Example 06 — naming rules & conventions."""
import keyword

# ✅ Good names (PEP 8 snake_case, descriptive)
pet_name = "Bruno"
city_of_birth = "Pune"
MAX_NAME_LENGTH = 30        # constant by convention
print(pet_name, city_of_birth, MAX_NAME_LENGTH)

# ❌ These would be SyntaxErrors — uncomment one at a time to see the message
# 1st_name = "Ada"          # cannot start with a digit
# user name = "Ada"         # no spaces
# user-name = "Ada"         # '-' is the minus operator
# class = "Python 101"      # 'class' is a keyword

# Case-sensitive: these are two different variables
Name = "Upper"
name = "lower"
print(Name, name)

# 🔴 All reserved keywords
print(f"{len(keyword.kwlist)} keywords:", ", ".join(keyword.kwlist))

# 🔴 Shadowing a built-in breaks it — don't do this in real code
original_len = len
len = 5                      # 😱 now len("abc") would crash
len = original_len           # restore it
print(len("restored"))
