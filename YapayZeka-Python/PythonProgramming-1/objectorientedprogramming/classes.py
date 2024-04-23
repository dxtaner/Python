# Variables
integer = 10
string = "icardi" "galatasaray football team"

# Classes
integer1 = 33
string1 = "kerem"


class Employee:
    pass


employee1 = Employee()

# Attributes


class Footballer:
    football_club = "galatasaray"
    age = 30


f1 = Footballer()
print("Footballer Object:", f1)
print("Age:", f1.age)
print("Football Club:", f1.football_club)

f1.football_club = "real madrid"
print("Changed Football Club:", f1.football_club)

# Methods


class Square:
    edge = 5  # meters
    area = 0

    def area1(self):
        self.area = self.edge * self.edge
        print("Area:", self.area)


s1 = Square()
print("Square Object:", s1)
print("Edge Length:", s1.edge)
s1.area1()

s1.edge = 7
s1.area1()

# Methods vs Functions


class Emp:
    age = 25
    salary = 1000  # $

    def age_salary_ratio(self):
        ratio = self.age / self.salary
        print("Method:", ratio)


e1 = Emp()
e1.age_salary_ratio()

# Function


def age_salary_ratio(age, salary):
    ratio = age / salary
    print("Function:", ratio)


age_salary_ratio(30, 3000)

# Function with Return


def find_area(a, b):  # a = pi,  b = r
    area = a * b**2
    return area


pi = 3.14
r = 5

result1 = find_area(pi, r)
print("Area 1:", result1)
result2 = find_area(pi, 10)
print("Area 2:", result2)
print("Sum of Areas:", result1 + result2)

# Initializer or Constructor


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name


a1 = Animal("dog", 2)
a2 = Animal("bird", 4)
a3 = Animal("lion", 6)
