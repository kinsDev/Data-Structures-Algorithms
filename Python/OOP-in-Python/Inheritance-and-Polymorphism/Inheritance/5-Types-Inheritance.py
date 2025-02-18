# Types of Inheritance

# 1. Single inheritance
# In single inheritance, there is only a single class extending from another class. 
# We can take the example of the Vehicle class as the parent class, and the Car class as the child class. 
# Let’s implement these classes below:

class Vehicle: # parent class
    def setTopSpeed(self, speed):
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)

class Car(Vehicle): # child class
    def openTrunk(self):
        print("Trunk is now open.")

corolla = Car() # creating an object of the car class
corolla.setTopSpeed(220) # Accessing methods from the parent class
corolla.openTrunk # accessing method from its own class




# 2. Multi-level inheritance
# When a class is derived from a class which itself is derived from another class, it is called multilevel inheritance. 
# We can extend the classes to as many levels as we want to

# e.g A Car is a Vehicle
# A Hybrid is a Car

class Vehicle: # parent class
    def setTopSpeed(self, speed):
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)

class Car(Vehicle): # child class
    def openTrunk(self):
        print("Trunk is now open.")

class Hybrid(Car): # child class of a child
    def turnOnHybrid(self):
        print("Hybrid mode is now on.")


priusPrime = Hybrid() # creating an object of the Hybrid class
priusPrime.setTopSpeed(220)  # accessing methods from the parent class
priusPrime.openTrunk()  # accessing method from the parent class
priusPrime.turnOnHybrid()  # accessing method from the child class





# 3. Hierarchical inheritance
# In hierarchical inheritance, more than one class extends, as per the requirement of the design, from the same base class. 
# The common attributes of these child classes are implemented inside the base class.
# e.g A Car is a Vehicle
# A Truck is a Vehicle

class Vehicle: # parent class
    def setTopSpeed(self, speed):  # defining the set
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)

class Car(Vehicle): # child class of the Vehicle Class
    pass

class Truck(Vehicle): # child class of the Vehicle class
    pass

corolla = Car() # creating object of the Car class
corolla.setTopSpeed(250)

volvo = Truck() # creating object of the Truck class
volvo.setTopSpeed(160)






# 4. Multiple inheritance
# When a class is derived from more than one base class, i.e., 
# when a class has more than one immediate parent class, it is called multiple inheritance.
# e.g HybridEngine IS A ElectricEngine.
# HybridEngine IS A CombustionEngine as well.

class CombustionEngine(): # One of the classes
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity

class ElectricEngine(): # The other class
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# child class that has inherited from both CombustionEngine and ElectricEngine classes
class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)

car = HybridEngine()
car.setChargeCapacity("250W")
car.setTankCapacity("60 Litres")
car.printDetails()






# 5. Hybrid Inheritance
# It is a combination of Multiple and Multi-level inheritance
# We are saying this because, a class is derived from more than one immediate Parent Class making it (multi-level)
# And those multiple immediate Parent classes are derived from another Parent class, making it (multiple)
# e.g CombustionEngine is a Engine
# ElectricEngine is a Engine
# HybridEngine is a CombustionEngine and a ElectricEngine

class Engine: # Parent class
    def setPower(self, power):
        self.power = power


class CombustionEngine(Engine):  # Child class inherited from Engine
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine(Engine):  # Child class inherited from Engine
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity


# Child class inherited from CombustionEngine and ElectricEngine
class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Power:", self.power)
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)

car = HybridEngine()
car.setPower("2000 CC")
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()
