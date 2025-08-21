class Person:
    mobile = 8888895927         # Class attribute.

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        
    def print_info(self):
        print("Name = ", self.name ,", age = ", self.age, "and email = ", self.email)
    
    def get_email(self):
        return self.email


p = Person("Sachin",34,"sdmangrule.gmail.com")
p.print_info()
print(Person.mobile)

print(p.get_email())

# object introspection

print(dir(p))