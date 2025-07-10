import time
import random

print("-" * 30)

char = ""
while char != "x":
    char = input("Type 'x' to exit: ")

print("-" * 30)

counter = 10
while counter >= 0:
    print(counter)
    counter -= 1

print("-" * 30)

guess = ""
secret = "python"
while guess != secret:
    guess = input("Guess the secret word: ")
print("You got it!")

print("-" * 30)

x = 1
while x * x < 200:
    print(f"Square: {x * x}")
    x += 1

print("-" * 30)

index = 0
text = "hello world"
while index < len(text):
    print(text[index])
    index += 1

print("-" * 30)

balance = 100
while balance > 0:
    spend = int(input(f"Balance: {balance}. Enter amount to spend: "))
    if spend <= balance:
        balance -= spend
print("No balance left.")

print("-" * 30)

attempts = 3
code = ""
while code != "1234" and attempts > 0:
    code = input("Enter PIN: ")
    attempts -= 1
if code == "1234":
    print("Welcome.")
else:
    print("Locked out.")

print("-" * 30)

level = 1
while level <= 3:
    print(f"Level {level} complete")
    time.sleep(0.5)
    level += 1
print("Game over.")

print("-" * 30)

number = 1
while True:
    if number > 10:
        break
    print(number)
    number += 1

print("-" * 30)

word = input("Enter a word: ")
i = 0
while i < len(word):
    print(f"Letter {i+1}: {word[i]}")
    i += 1

print("-" * 30)
