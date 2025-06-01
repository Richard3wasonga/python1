num1,num2 = 200,123

if num1 < num2:
    print(f"sure {num1} is less than {num2}")
elif num1 == num2:
    print(f"sure {num1} is equal to {num2}")
else:
    print(f"{num1} is greater than {num2}")
sentence ='''
This is a random sentence i have just written.
'''

if "have" in sentence:
    print("The word have is in sentence")

if "monumental" in sentence:
    print("The word monumental is not in sentence")

if len(sentence) > 10:
    print("This is a very long sentence")

# Numeric conditions
if num1 % 2 == 0:
    print(f"{num1} is even")

if num2 % 2 != 0:
    print(f"{num2} is odd")

if num1 - num2 > 50:
    print(f"The difference between {num1} and {num2} is greater than 50")

if num1 > 100 and num2 > 100:
    print("Both numbers are greater than 100")

if num1 > 100 or num2 > 100:
    print("At least one number is greater than 100")

# String conditions
if sentence.startswith("This"):
    print("The sentence starts with 'This'")

if sentence.endswith("."):
    print("The sentence ends with a period")

if sentence.islower():
    print("The entire sentence is lowercase")
else:
    print("The sentence has some capital letters")

# Combining conditions
if "random" in sentence and len(sentence) > 30:
    print("The sentence contains 'random' and is fairly long")

# Nested condition
if "sentence" in sentence:
    if "written" in sentence:
        print("The sentence contains both 'sentence' and 'written'")

# Check if a character exists
if '.' in sentence:
    print("The sentence contains a period '.'")
