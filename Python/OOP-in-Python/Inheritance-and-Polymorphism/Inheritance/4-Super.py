# Now let's use Super to refer to the Parent class

# Without Super
class Vehicle:
    # initializer
    def __init__(self, make, color, model):
        # public attributes
        self.make = make
        self.color = color
        self.model = model

    # methods
    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)

# child class
class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        Vehicle.__init__(self, make, color, model)
        self.doors = doors
    
    def printCarDetails(self):
        self.printDetails()
        print("Doors:", self.doors)

obj1 = Car("Suzuki", "Grey", "2024", 4)
obj1.printCarDetails()


# With Super - we will only be interchanging one line of code
class Vehicle:
    # initializer
    def __init__(self, make, color, model):
        # public attributes
        self.make = make
        self.color = color
        self.model = model

    # methods
    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)

# child class


class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        super().__init__(make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Doors:", self.doors)


obj1 = Car("Suzuki", "Grey", "2024", 4)
obj1.printCarDetails()

obj2 = Vehicle("Mercedes", "Red", "2024")
obj2.printDetails()