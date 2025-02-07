# Method overriding
# Method overriding is the process of redefining a parent class’s method in a subclass.
# In other words, if a subclass provides a specific implementation of a method 
# that had already been defined in one of its parent classes, it is known as method overriding.


# In method overriding:

# The method in the parent class is called the overridden method.
# The methods in the child classes are called the overriding methods.

class Shape: # Parent Class
    def __init__(self): # initializing sides of all shapes to 0
        self.sides = 0
    
    def getArea():
        pass

class Rectangle(Shape): # Child Class
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        self.sides = 4
    
    # method to calculate area
    def getArea(self):
        return self.width * self.height

class Circle(Shape): # Another child class
    def __init__(self, radius = 0):
        self.radius = radius
    
    # method to get area
    def getArea(self):
        return self.radius * self.radius * 3.14

shapes = [Rectangle(6, 10), Circle(7)]
print("Area of Rectangle", str(shapes[0].getArea())) # converted it to string
print("Area of Circle", shapes[1].getArea()) # didn't convert to string

# In the above example: Both Rectangle Class and Circle class overide the getArea() method 
# from the Shape class, which is the parent class
