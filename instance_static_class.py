class Employee:

    company = "HP"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Instance method (default)
    def print_info(self):
        info = f"The name is {self.name} and salary is {self.salary}"
        print(info)

## Static method -> we dont want to pass self as argument as it doesnt need instance of the class.
    @staticmethod
    def sum(a,b):
        return a+b
    
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company


e1 = Employee("sachin", 3434)
e1.print_info()
print(Employee.company)
e1.change_company("Acer")
e1.print_company()

print(e1.sum(2,3))