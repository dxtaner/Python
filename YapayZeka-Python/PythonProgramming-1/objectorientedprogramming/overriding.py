# Base class
class Animal:
    def speak(self):
        return "Animal speaks"

# Derived class (inheritance)


class Dog(Animal):
    def speak(self):
        return "Dog barks"

# Derived class (inheritance)


class Cat(Animal):
    def speak(self):
        return "Cat meows"


# Creating instances of derived classes
dog = Dog()
cat = Cat()

# Calling the speak method of each instance
print(dog.speak())  # Output: Dog barks
print(cat.speak())  # Output: Cat meows
