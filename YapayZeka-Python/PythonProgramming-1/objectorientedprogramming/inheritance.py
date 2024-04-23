# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Derived class (inheritance)


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Derived class (inheritance)


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Derived class (inheritance)


class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo!"


# Creating instances of derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

# Calling the speak method of each instance
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
print(cow.speak())  # Output: Bessie says Moo!
