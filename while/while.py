import time

print("-" * 30)

# 16. Loop that keeps asking for a number until an even one is entered
num = None
while num is None or num % 2 != 0:
    num = int(input("Enter an even number: "))
print(f"Thanks! {num} is even.")

print("-" * 30)

# 17. Loop that simulates a countdown timer
countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1
    time.sleep(1)
print("Blast off!")

print("-" * 30)

# 18. Loop that sums user-entered numbers until 0 is entered
total = 0
num = None
while num != 0:
    num = int(input("Enter a number to add (0 to stop): "))
    total += num
print(f"Total sum: {total}")

print("-" * 30)

# 19. Loop that simulates a progress bar
progress = 0
while progress <= 100:
    print(f"Progress: {progress}%")
    time.sleep(0.2)
    progress += 10
print("Task complete.")

print("-" * 30)

# 20. Loop that checks if a word is a palindrome
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

# 21. Loop that keeps asking for a number greater than 100
number = 0
while number <= 100:
    number = int(input("Enter a number greater than 100: "))
print(f"Great! {number} is greater than 100.")

print("-" * 30)

# 22. Loop that builds a triangle of stars
rows = 1
while rows <= 5:
    print("*" * rows)
    rows += 1

print("-" * 30)

# 23. Loop that asks a riddle until the correct answer is given
answer = ""
while answer.lower() != "silence":
    answer = input("What is so fragile that saying its name breaks it? ")
print("Correct! The answer is silence.")

print("-" * 30)

# 24. Loop that collects names until 'done' is typed
name = ""
names = []
while name.lower() != "done":
    name = input("Enter a name (or 'done' to finish): ")
    if name.lower() != "done":
        names.append(name)
print("Names collected:", names)

print("-" * 30)

# 25. Loop that prints only odd numbers up to 15
num = 1
while num <= 15:
    if num % 2 != 0:
        print(f"Odd number: {num}")
    num += 1

print("-" * 30)
