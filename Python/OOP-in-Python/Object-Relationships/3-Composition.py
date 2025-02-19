# Composition

# Composition is the practice of accessing other class objects in your class. 
# In such a scenario, the class which creates the object of the other class is known as the owner 
# and is responsible for the lifetime of that object.

# Composition relationships are Part-of relationships where the part must constitute a segment of the whole object.

# In composition, the lifetime of the owned object depends on the lifetime of the owner.

# Example
# A car is composed of an engine, tires, and doors. 
# In this case, a Car owned these objects, so a Car is an Owner class, and the tires, doors, 
# and engine classes are Owned classes.

class Engine:
    def __init__(self, capacity=0):
        self.capacity = capacity
    
    def printDetails(self):
        print("Engine Details:", self.capacity)

class Tires:
    def __init__(self, tires=0):
        self.tires = tires
    
    def printDetails(self):
        print("Number of Tires:", self.tires)

class Doors:
    def __init__(self, doors):
        self.doors = doors
    
    def printDetails(self):
        print("Number of Doors:", self.doors)


class Car:
    def __init__(self, eng, tr, dr, color):
        self.eobj = Engine(eng)
        self.tobj = Tires(tr)
        self.dobj = Doors(dr)
        self.color = color
    
    def printDetails(self):
        self.eobj.printDetails()
        self.tobj.printDetails()
        self.dobj.printDetails()
        print("Car Color:", self.color)

car = Car(2500, 4, 2, "Red") # creating a car object from the Car class
car.printDetails()

# We have created a Car class which contains the objects of Engine, Tires, and Doors classes. 
# Car class is responsible for their lifetime, i.e., when Car dies, so does tire, engine, and doors too.


class Salary:
    def __init__(self, base_pay=0, bonus=0):
        self._base_pay = base_pay
        self._bonus = bonus

    def get_base_pay(self):
        return self._base_pay

    def set_base_pay(self, base_pay):
        self._base_pay = base_pay

    def get_bonus(self):
        return self._bonus

    def set_bonus(self, bonus):
        self._bonus = bonus


class Employee:
    def __init__(self, name='', base_pay=0, bonus=0):
        self._name = name
        # Create a Salary object internally
        self._salary = Salary(base_pay, bonus)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_salary(self):
        return self._salary.get_base_pay() + self._salary.get_bonus()

    def set_salary(self, base_pay, bonus):
        self._salary.set_base_pay(base_pay)
        self._salary.set_bonus(bonus)


# Testing the classes
e = Employee("John Doe", 50000, 5000)  # Pass base_pay and bonus directly
print(e.get_name())  # Output: John Doe
print(e.get_salary())  # Output: 55000

e.set_name("Jane Smith")
e.set_salary(60000, 7000)

print(e.get_name())  # Output: Jane Smith
print(e.get_salary())  # Output: 67000
