print("-" * 30)

# 11. Loop that simulates a simple menu system
choice = ""
while choice != "4":
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Do Nothing")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye!")
    elif choice == "3":
        print("Okay...")
print("Exiting menu.")

print("-" * 30)

# 12. Loop that tracks temperature drop below freezing
temperature = 10
while temperature > 0:
    print(f"Current temperature: {temperature}°C")
    temperature -= 2
print("It's freezing!")

print("-" * 30)

# 13. Loop that finds the first perfect square greater than 30
num = 31
while True:
    if (num ** 0.5).is_integer():
        print(f"First perfect square greater than 30 is {num}")
        break
    num += 1

print("-" * 30)

# 14. Loop that builds a simple password hint
password = "openai"
hint = ""
i = 0
while i < len(password):
    hint += password[i] + "*"
    i += 1
print(f"Password hint: {hint}")

print("-" * 30)

# 15. Loop that calculates factorial of a number
n = int(input("Enter a number to find its factorial: "))
result = 1
counter = 1
while counter <= n:
    result *= counter
    counter += 1
print(f"Factorial of {n} is {result}")
