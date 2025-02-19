# challenge 1
class Music:  # defining the parent class
    total_songs = 100


class Rock(Music):  # defining the child class
    total_songs = 30

    def display(self):
        print(self.total_songs)

        print(super().total_songs)


genre = Rock()
genre.display()



# challenge 2
# class
# object
# calling the objects
class Vehicle:
    def displayType(self):
        print("This is a vehicle")


class Car(Vehicle):
    def displayType(self):
        print("This is a car")


class Bus(Vehicle):
    def displayType(self):
        print("This is a bus")


c = Car()
b = Bus() # object in the bus class
v = Vehicle()

c.displayType()
b.displayType()
v.displayType()



# challenge 3
class A:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, num):
        return A((self.x + num.x) * 2)

    def __sub__(self, num):
        return A((self.x - num.x) * 2)


obj1 = A(3)
obj2 = A(5)

obj3 = obj1 + obj2
obj4 = obj1 - obj2

print("obj3.x = ", obj3.x)
print("obj3.y = :", obj3.y)
print("obj4.x = :", obj4.x)
print("obj4.y = ", obj4.y)




# challenge 4
class Vehicle:
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)


obj = Car('Tesla')



# challenge 5
class Ingredient:
    def __init__(self, name=''):
        self.name = name

    def printDetails(self):
        print(self.name)


class Pizza:
    def __init__(self, cheese, tomato, topping, dough):
        self.cheese = Ingredient(cheese)
        self.tomato = Ingredient(tomato)
        self.topping = Ingredient(topping)
        self.dough = Ingredient(dough)

    def printIngredients(self):
        self.cheese.printDetails()
        self.tomato.printDetails()
        self.topping.printDetails()
        self.dough.printDetails()


# Creating a Pizza object with specific ingredients
pepperoni_pizza = Pizza('cheese', 'tomato', 'pepperoni', 'dough')
pepperoni_pizza.printIngredients()



# challenge 6
from abc import ABC, abstractmethod
class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length


# Creating an instance of Square
square = Square(5)





`# challenge 7:
# Override the print_continent method for the derived classes
#This coding challenge will test your concepts on inheritance and polymorphism. You are asked to create a class Country that will contain a name attribute.
#You will be provided with base classes that inherit from the Country class . You will need to add a method to the derived classes called print_continent that will state which continent that country belongs to.
#For example, given an object of the class India:
#obj = India()
#The print_continent method should give the following output:
#Asia
#Similarly, given an object of the France class:
#obj = France()
#The print_continent method should give the following output:
#Europe
class Country:
    def __init__(self, name):
        self.name = name

    def print_continent(self):
        print('This method should behave differently for each derived class')


class India(Country):
    def __init__(self):
        super().__init__("India")  # Hardcode the name as "India"

    def print_continent(self):
        print("Asia")


class France(Country):
    def __init__(self):
        super().__init__("France")  # Hardcode the name as "France"

    def print_continent(self):
        print("Europe")


class Nigeria(Country):
    def __init__(self):
        super().__init__("Nigeria")  # Hardcode the name as "Nigeria"

    def print_continent(self):
        print("Africa")


# Testing the classes
obj1 = India()  # No argument needed
obj1.print_continent()  # Output: Asia

obj2 = France()  # No argument needed
obj2.print_continent()  # Output: Europe

obj3 = Nigeria()  # No argument needed
obj3.print_continent()  # Output: Africa




# challenge 8
#Composition
#For this coding challenge, you are asked to create an Employee and a Salary class . The Employee class will have the following attributes:
#name
#salary

#The Salary class will have the following attributes:
#base_salary
#bonus

#For this use case, the Employee class object will compose a Salary class object as well.
#Note: Some helper methods have already been added to the classes, which you can use for your solution.
#You will need to create the following methods for each class:
# my initial implementation
class Salary:
    def __init__(self, base_salary=0, bonus=0):
        self.base_salary = base_salary
        self.bonus = bonus
    
    def get_bonus(self):
        return self.bonus
    
    def set_bonus(self, b):
        self.bonus = b

    def get_base_pay(self):
        return self.base_salary
    
    def set_base_pay(self, sb):
        self.base_salary = sb


class Employee:
    def __init__(self, name='', salary=0):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def set_name(self, n):
        self.name = n

    def get_salary(self):
        return self.salary

    def set_salary(self, s):
        self.salary = s
