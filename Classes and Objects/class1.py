# Creating classes

class Car:
    amount_cars = 0

    # __init__ is the constructor
    # self is a mandatory parameter
    def __init__(self, manufacturer, model, hp):
        self.manufacturer = manufacturer
        self.model = model
        self.hp = hp
        Car.amount_cars += 1

    def print_info(self):
        print(f"Manufacturer: {self.manufacturer}| Model: {self.model}| HP: {self.hp}")

    def print_car_amount(self):
        print(f"Amount: {Car.amount_cars}")

    # def__del__(self):
    #     print("Object gets deleted!")
    #     Car.amount_cars -= 1


myCar1 = Car("Tesla", "Model X", 525)
myCar2 = Car("BMW", "X3", 200)
myCar3 = Car("VW", "Golf", 100)
myCar4 = Car("Porsche", "911", 520)

# Hidden Atributes


class MyClass:

    def __init__(self):
        self.__hidden = "Hello"
        print(self.__hidden)  # Works


# Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_older(self, years):
        self.age += years


# The Programmer class inherits the and functions of Person class

class Programmer(Person):
    def __init__(self, name, age, language):
        super(Programmer, self).__init__(name, age)
        self.language = language

    def print_language(self):
        print(f"Favorite Programming Language: {self.language}")


p1 = Programmer("Mike", 30, "Python")
p1.print_language()


# Operator Overloading

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"X: {self.x} |Y: {self.y}"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


v1 = Vector(3, 5)
v2 = Vector(6, 2)
v3 = v1 + v2

print(v1)
print(v2)
print(v3)
