class Employee:

    raise_rate = 1.8
    counter = 0

    def __init__(self, first_name, last_name, salary):  # constructor
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + last_name + "@yandex.com"

        Employee.counter += 1

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def apply_raise(self):
        self.salary += self.salary * self.raise_rate


# Employee example
employee1 = Employee("samir", "peep", 100)
print("Initial salary: ", employee1.salary)
employee1.apply_raise()
print("New salary: ", employee1.salary)

employee2 = Employee("peep", "giz", 200)
employee3 = Employee("guler", "arda", 600)
employee4 = Employee("koc", "griog", 500)

# Example using a list
employee_list = [employee1, employee2, employee3, employee4]

max_salary = -1
max_salary_index = -1
for emp in employee_list:
    if emp.salary > max_salary:
        max_salary = emp.salary
        max_salary_index = emp

print("Maximum salary: ", max_salary)
print("Employee with maximum salary: ", max_salary_index.get_full_name())
