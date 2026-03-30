# Class
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + " is barking")

dog1 = Dog("Tommy")
dog1.bark()

# Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    pass

c = Cat()
c.speak()