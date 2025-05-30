def say_hello():
    name = "Adele"
    print(f"{name} hello from the other side")

say_hello()


def say_hi(name):
    print(f"Say hi to {name}")

say_hi("sophie")

def greet(name="friend"):
    """Greets a person with a default fallback."""
    print(f"Hello, {name}!")

greet("Liam")
greet()  # Uses default

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

result = add(5, 7)
print(f"Sum is {result}")

def list_fruits(fruits):
    """Prints each fruit from a list."""
    for fruit in fruits:
        print(f"🍓 {fruit}")

list_fruits(["Apple", "Banana", "Cherry"])

def check_temperature(temp):
    """Checks the temperature and prints advice."""
    if temp < 0:
        print("It's freezing! ❄️")
    elif temp < 20:
        print("A bit chilly. 🧥")
    else:
        print("Nice weather! ☀️")

check_temperature(15)

def divide(a, b):
    """Safely divides two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

print(divide(10, 2))
print(divide(5, 0))

def describe_person(name, age):
    """Returns a dictionary describing a person."""
    return {
        "name": name,
        "age": age,
        "status": "adult" if age >= 18 else "minor"
    }

person = describe_person("Emma", 22)
print(person)


