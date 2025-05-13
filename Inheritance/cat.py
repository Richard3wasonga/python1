class Cat:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Meow!")

Bubbles = Cat("Bubbles")
Bubbles.speak()
print(Bubbles.name)