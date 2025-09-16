class Employee:

    company = "HP"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e = Employee("Sachin", 343434)

print(e.name, e.salary)