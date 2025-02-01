# The Super Function

# The use of super() comes into play when we implement inheritance. 
# It is used in a child class to refer to the parent class without explicitly naming it. 
# It makes the code more manageable, and there is no need to know the name of the parent class to 
# access its attributes.


# Use cases of the super() function

# 1. Accessing parent class properties
class Vehicle:
    fuelCap = 90

class Car(Vehicle):
    fuelCap = 50

    def display(self):
        # Accessing fuelCap from the Vehicle class using Super()
        print("Fuel Cap from the Vehicle class:", super().fuelCap)

        # Accessing the fuelCap from the Car class using self
        print("Fuel cap from the Car Class:", self.fuelCap)

obj = Car() # creating a car object
obj.display() # calling the car class display() method



# 2. Calling the parent class methods
class Vehicle: # defining the parent class
    def display(self): # defining display method in the parent class
        print("I am from the Vehicle class")

class Car(Vehicle): # defining the child class
    def display(self):
        super().display()
        print("I am from the Car class")

obj1 = Car()  # creating a car object
obj1.display()  # calling the Car class method display()



# 3. Using with initializers
# - Another essential use of the function super() is to call the initializer 
# - of the parent class from inside the initializer of the child class.
class  ParentClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class ChildClass(ParentClass):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c


obj = ChildClass(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)
