# Variables
x = 5
y = "Hello, Python!"

# Data Types
a = 10            # Integer
b = 3.14          # Float
c = "Python"      # String
d = True          # Boolean

# Arithmetic Operations
sum_result = 10 + 5
difference = 10 - 5
product = 10 * 5
quotient = 10 / 5
remainder = 10 % 3

# String Operations
greeting = "Hello, " + "World!"
repeated = "Python" * 3

# Comparison Operators
is_equal = (x == 5)
greater_than = (x > 2)


# if-else statement
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# for loop
for i in range(5):
    print(i)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1


# Function definition
def greet(name):
    return "Hello, " + name + "!"


# Function call
result = greet("Taner")
print(result)

# Lists
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "orange", "banana"]

# Accessing elements
first_number = numbers[0]
second_fruit = fruits[1]

# Dictionaries
person = {"name": "John", "age": 30, "city": "New York"}

# Accessing values
person_name = person["name"]

# Input
user_input = input("Enter your name: ")
print("Hello, " + user_input + "!")
