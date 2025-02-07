# Abstract Base Classes

# Abstract base classes define a set of methods and properties that a class must implement in order to be considered a duck-type instance of that class.

from abc import ABC, abstractmethod
class Shape(ABC):  # Shape is a child class of Abstract Base Classes(ABC)
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)

square = Square(4) # object of square was instantiated

# When we define the methods, area and perimeter, in the child class Square, 
# an object of Shape cannot be instantiated, but an object of Square can be.
# We allow the user to have a free hand over the definition of the methods while also making sure that the methods are defined.
# Methods with @abstractmethod decorators must be defined in the child class.
