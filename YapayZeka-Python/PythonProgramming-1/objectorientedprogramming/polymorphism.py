class Animal:
    def speak(self):
        pass

# Derived class (inheritance)


class Dog(Animal):
    def speak(self):
        return "Dog barks"

# Derived class (inheritance)


class Cat(Animal):
    def speak(self):
        return "Cat meows"

# Derived class (inheritance)


class Cow(Animal):
    def speak(self):
        return "Cow moos"

# Function demonstrating polymorphism


def make_sound(animal):
    return animal.speak()


# Creating instances of derived classes
dog = Dog()
cat = Cat()
cow = Cow()

# Calling the make_sound function with different instances
print(make_sound(dog))  # Output: Dog barks
print(make_sound(cat))  # Output: Cat meows
print(make_sound(cow))  # Output: Cow moos
