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
