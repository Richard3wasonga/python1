import time

print("-" * 30)


num = None
while num is None or num % 2 != 0:
    num = int(input("Enter an even number: "))
print(f"Thanks! {num} is even.")

print("-" * 30)


countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1
    time.sleep(1)
print("Blast off!")

print("-" * 30)


total = 0
num = None
while num != 0:
    num = int(input("Enter a number to add (0 to stop): "))
    total += num
print(f"Total sum: {total}")

print("-" * 30)


progress = 0
while progress <= 100:
    print(f"Progress: {progress}%")
    time.sleep(0.2)
    progress += 10
print("Task complete.")

print("-" * 30)


word = input("Enter a word to check if it's a palindrome: ").lower()
reversed_word = ""
index = len(word) - 1
while index >= 0:
    reversed_word += word[index]
    index -= 1
if word == reversed_word:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")

print("-" * 30)


number = 0
while number <= 100:
    number = int(input("Enter a number greater than 100: "))
print(f"Great! {number} is greater than 100.")

print("-" * 30)


rows = 1
while rows <= 5:
    print("*" * rows)
    rows += 1

print("-" * 30)


answer = ""
while answer.lower() != "silence":
    answer = input("What is so fragile that saying its name breaks it? ")
print("Correct! The answer is silence.")

print("-" * 30)


name = ""
names = []
while name.lower() != "done":
    name = input("Enter a name (or 'done' to finish): ")
    if name.lower() != "done":
        names.append(name)
print("Names collected:", names)

print("-" * 30)


num = 1
while num <= 15:
    if num % 2 != 0:
        print(f"Odd number: {num}")
    num += 1

print("-" * 30)


password = ""
while password != "python123":
    password = input("Enter the password: ")
print("Access granted.")

print("-" * 30)


value = 2
while value <= 1000:
    print(f"Current value: {value}")
    value *= 2

print("-" * 30)


import random
roll = 0
while roll != 6:
    roll = random.randint(1, 6)
    print(f"Rolled: {roll}")
print("You rolled a 6!")

print("-" * 30)


fruits = ["apple", "banana", "cherry", "date"]
while fruits:
    print(f"Removing: {fruits.pop(0)}")

print("-" * 30)


a, b = 0, 1
while a < 100:
    print(a)
    a, b = b, a + b

print("-" * 30)
