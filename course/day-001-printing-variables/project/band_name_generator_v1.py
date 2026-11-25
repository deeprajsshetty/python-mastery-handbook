"""🎸 Band Name Generator — v1 (🟢 Basic)

Concepts: print(), input(), variables, string concatenation, \n.

Run: python project/band_name_generator_v1.py
"""

# 1. Greet the user
print("Welcome to the Band Name Generator!")

# 2. Ask two questions and store each answer in a well-named variable
city = input("Which city did you grow up in?\n")
pet_name = input("What's your pet's name?\n")

# 3. Combine the answers — remember + does NOT add spaces for us
print("Your band name could be " + city + " " + pet_name)
