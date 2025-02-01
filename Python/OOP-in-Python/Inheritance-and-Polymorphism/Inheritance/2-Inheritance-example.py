class Vehicle: # parent class
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model
    
    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)

class Car(Vehicle): # child class
    def __init__(self, make, color, model, doors):
        # First we call the constructor from the parent class
        Vehicle.__init__(self, make, color, model)
        self.doors = doors
    
    def printCarDetails(self):
        # we call the method from the parent constructor class
        self.printDetails()
        print("Doors:", self.doors)

obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printCarDetails()