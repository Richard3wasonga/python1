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

sum_total = 0
num = 1
while num <= 5:
    sum_total += num
    num += 1
print(f"Sum of 1 to 5: {sum_total}")

print("-" * 30)

value = random.randint(1, 20)
attempt = 0
guess = -1
while guess != value:
    guess = int(input("Guess the number (1-20): "))
    attempt += 1
print(f"Correct in {attempt} tries.")

print("-" * 30)

data = [10, 20, 30, 40]
i = 0
while i < len(data):
    print(f"Item {i}: {data[i]}")
    i += 1

print("-" * 30)

n = 5
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print(f"Factorial: {factorial}")

print("-" * 30)

temp = random.randint(25, 45)
while temp < 40:
    print(f"Temp: {temp}°C — Cooling down...")
    temp += 1
print(f"Reached {temp}°C — Alert triggered!")

print("-" * 30)

k = 10
while k > 0:
    print(f"Countdown: {k}")
    k -= 1

print("-" * 30)

letters = "abcdef"
pos = 0
while pos < len(letters):
    print(letters[pos].upper())
    pos += 1

print("-" * 30)

even = 0
while even <= 10:
    print(f"Even: {even}")
    even += 2

print("-" * 30)

tries = 0
max_tries = 5
answer = ""
while answer != "yes" and tries < max_tries:
    answer = input("Do you agree? (yes/no): ")
    tries += 1

print("-" * 30)
