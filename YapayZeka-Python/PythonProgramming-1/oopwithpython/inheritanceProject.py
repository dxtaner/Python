class Website:
    "parent"

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def login_info(self):
        print(self.name + " " + self.surname)


class Website1(Website):
    "child"

    def __init__(self, name, surname, ids):
        super().__init__(name, surname)
        self.ids = ids

    def login(self):
        print(self.name + " " + self.surname + " "+self.ids)


class Website2(Website):
    def __init__(self, name, surname, email):
        super().__init__(name, surname)
        self.email = email

    def login(self):
        print(self.name + " " + self.surname + " "+self.email)


# Creating instances
p1 = Website("John", "Doe")
p2 = Website1("Alice", "Smith", "123")
p3 = Website2("Bob", "Johnson", "bob@example.com")

# Accessing attributes and methods
print("Website:")
print("Name:", p1.name)
print("Surname:", p1.surname)
p1.login_info()
print("\nWebsite1:")
print("Name:", p2.name)
print("Surname:", p2.surname)
print("IDs:", p2.ids)
p2.login()
print("\nWebsite2:")
print("Name:", p3.name)
print("Surname:", p3.surname)
print("Email:", p3.email)
p3.login()
