# Cars and Engines Challenge 1

# In this exercise, you have to perform a composition between a sedan car class and its engine.

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def printDetails(self):
        print("Model of Car:", self.model)
        print("Color of Car:", self.color)

class SedanEngine:
    def start(self):
        print("Car has started.")

    def stop(self):
        print("Car has stopped.")

class Sedan(Car):
    def __init__(self, model, color):
        super().__init__(model, color)
        self.engine = SedanEngine()
    
    def setStart(self):
        self.engine.start()
    
    def setStop(self):
        self.engine.stop()


car1 = Sedan("Toyota", "Grey")
car1.setStart()
car1.printDetails()
car1.setStop()