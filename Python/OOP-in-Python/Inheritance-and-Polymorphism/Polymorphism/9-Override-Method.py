# Challenge 1: Override a Method Using the Super Function

class Shape: # parent class
    sname = "Shape"

    def getName(self):
        return self.sname
    
class XShape(Shape): # child class
    # initializer
    def __init__(self, name):
        self.xsname = name

    def getName(self):  # overriden method
        return (super().getName() + ", " + self.xsname)

circle = XShape("Circle")
print(circle.getName())