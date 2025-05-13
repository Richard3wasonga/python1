class Pet:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("Pet is speaking")

class Dog(Pet):
    def speak(self):
        super().speak()
        print("Woof!")

dog1 = Dog("Major")
dog1.speak()

class Cat(Pet):
    pass

