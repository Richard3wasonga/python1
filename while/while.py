# Loop that doubles a number until it reaches or exceeds 1000
value = 1
while value < 1000:
    print(f"Value is {value}")
    value *= 2

# Loop that simulates a password check
correct_password = "openai"
attempt = ""
while attempt != correct_password:
    attempt = input("Enter the password: ")
    if attempt != correct_password:
        print("Incorrect password. Try again.")
print("Access granted!")

# Countdown timer with pause (simulated delay)
import time
seconds = 3
while seconds > 0:
    print(f"{seconds}...")
    time.sleep(1)
    seconds -= 1
print("Time's up!")

# Loop that sums user-entered numbers until they type "done"
sum_total = 0
user_input = ""
while user_input != "done":
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input.isdigit():
        sum_total += int(user_input)
print(f"Total sum: {sum_total}")

# Loop that prints a pattern
rows = 1
while rows <= 5:
    print("*" * rows)
    rows += 1
