# Challenge 1: Override a Method Using the Super Function

class XShape(Shape):
    # initializer
    def __init__(self, name):
        self.xsname = name

    def getName(self):  # overriden method
        return (self.super() + ", " + self.xsname)
