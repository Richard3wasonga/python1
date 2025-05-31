num = 10

while num <20:
    print(num)
    num += 1

countdown = 5

while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1

print("🚀 Liftoff!")

user_input = ""

while user_input.lower() != "exit":
    user_input = input("Type something (or 'exit' to quit): ")
    print(f"You typed: {user_input}")


total = 0
number = 1

while total < 50:
    total += number
    print(f"Added {number}, total is now {total}")
    number += 1


x = 0

while True:
    print(f"x is {x}")
    x += 1
    if x == 5:
        print("Breaking out of the loop.")
        break

n = 0

while n < 10:
    n += 1
    if n % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {n}")

