# More numeric conditions
if abs(num1 - num2) < 100:
    print("The absolute difference between num1 and num2 is less than 100")

if num1 // num2 > 1:
    print(f"{num1} divided by {num2} (integer division) is greater than 1")

if num2 != 0 and num1 % num2 == 0:
    print(f"{num1} is divisible by {num2}")

if (num1 + num2) % 5 == 0:
    print("The sum of the two numbers is divisible by 5")

# More string conditions
if " " in sentence:
    print("The sentence contains spaces")

if sentence.count("e") > 2:
    print("The letter 'e' appears more than twice")

if sentence.find("random") != -1:
    print("The word 'random' was found using find()")

if sentence[0].isupper():
    print("The sentence starts with a capital letter")

# Checking character types
if any(char.isdigit() for char in sentence):
    print("The sentence contains at least one digit")

if any(char.isupper() for char in sentence):
    print("The sentence contains at least one uppercase letter")

# Boolean combinations
if "random" in sentence or "spontaneous" in sentence:
    print("The sentence contains either 'random' or 'spontaneous'")

if not "monumental" in sentence:
    print("The word 'monumental' is not in the sentence")

# Using in-line if (ternary)
print("num1 is positive" if num1 > 0 else "num1 is not positive")

# Length-based conditions
word_count = len(sentence.split())
if word_count > 5:
    print(f"The sentence has more than 5 words ({word_count} words)")

# Nested numeric condition
if num1 > 100:
    if num1 % 10 == 0:
        print(f"{num1} is a multiple of 10 and greater than 100")

# Case-sensitive check
if "This" in sentence:
    print("The word 'This' (capital T) is in the sentence")

# List membership check
keywords = ["random", "sentence", "example"]
for word in keywords:
    if word in sentence:
        print(f"The word '{word}' is found in the sentence")
