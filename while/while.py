import time

# 1. Loop that doubles a number until it reaches or exceeds 1000
value = 1
while value < 1000:
    print(f"Value is {value}")
    value *= 2

print("-" * 30)

# 2. Loop that simulates a password check
correct_password = "openai"
attempt = ""
while attempt != correct_password:
    attempt = input("Enter the password: ")
    if attempt != correct_password:
        print("Incorrect password. Try again.")
print("Access granted!")

print("-" * 30)

# 3. Countdown timer with pause (simulated delay)
seconds = 3
while seconds > 0:
    print(f"{seconds}...")
    time.sleep(1)
    seconds -= 1
print("Time's up!")

print("-" * 30)

# 4. Loop that sums user-entered numbers until they type "done"
sum_total = 0
user_input = ""
while user_input != "done":
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input.isdigit():
        sum_total += int(user_input)
print(f"Total sum: {sum_total}")

print("-" * 30)

# 5. Loop that prints a pattern
rows = 1
while rows <= 5:
    print("*" * rows)
    rows += 1

print("-" * 30)

# 6. Loop that finds the first multiple of 7 greater than 50
num = 51
while num % 7 != 0:
    num += 1
print(f"The first multiple of 7 greater than 50 is {num}")

print("-" * 30)

# 7. Loop that keeps asking for a number between 1 and 10
number = 0
while number < 1 or number > 10:
    number = int(input("Enter a number between 1 and 10: "))
print(f"You entered {number}, which is valid!")

print("-" * 30)

# 8. Loop that simulates a loading bar
progress = 0
while progress <= 100:
    print(f"Loading... {progress}%")
    time.sleep(0.2)
    progress += 20
print("Loading complete!")

print("-" * 30)

# 9. Loop that reverses a string
text = "hello"
reversed_text = ""
index = len(text) - 1
while index >= 0:
    reversed_text += text[index]
    index -= 1
print(f"Reversed string: {reversed_text}")

print("-" * 30)

# 10. Loop that checks for prime number
n = int(input("Enter a number to check if it's prime: "))
i = 2
is_prime = True
while i <= n // 2:
    if n % i == 0:
        is_prime = False
        break
    i += 1
if n > 1 and is_prime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
