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
