class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Generic animal sound:")

class Dog(Animal):
    def speak(self):
        print("Woof!!")

class Cat(Animal):
    def speak(self):
        print("Meow!!!")

my_dog = Dog("Bruno")
my_cat = Cat("Fluppy")


print(my_dog.name)
my_dog.speak()
print(my_cat.name)
my_cat.speak()

