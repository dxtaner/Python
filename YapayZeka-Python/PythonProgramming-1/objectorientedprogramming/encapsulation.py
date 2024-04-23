class Car:
    def __init__(self, make, model, year):
        self.__make = make   # Private attribute
        self.__model = model  # Private attribute
        self.__year = year   # Private attribute
        self.__odometer_reading = 0  # Private attribute

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_odometer_reading(self):
        return self.__odometer_reading

    def set_odometer_reading(self, mileage):
        if mileage >= self.__odometer_reading:
            self.__odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.__odometer_reading += miles
        else:
            print("You can't decrement odometer!")


# Creating an instance of Car
my_car = Car("Toyota", "Corolla", 2020)

# Accessing private attributes indirectly via getter methods
print("Make:", my_car.get_make())
print("Model:", my_car.get_model())
print("Year:", my_car.get_year())

# Trying to access private attribute directly
# This will cause an error
# print("Make:", my_car.__make)

# Modifying private attribute indirectly via setter methods
my_car.set_make("Honda")
my_car.set_model("Civic")
my_car.set_year(2022)

# Accessing modified private attributes indirectly
print("Make:", my_car.get_make())
print("Model:", my_car.get_model())
print("Year:", my_car.get_year())

# Using methods to interact with private attribute
my_car.set_odometer_reading(1000)
print("Odometer Reading:", my_car.get_odometer_reading())

# Incrementing odometer reading
my_car.increment_odometer(500)
print("Odometer Reading After Increment:", my_car.get_odometer_reading())

# Trying to roll back odometer
my_car.set_odometer_reading(800)
print("Odometer Reading After Rollback Attempt:", my_car.get_odometer_reading())
