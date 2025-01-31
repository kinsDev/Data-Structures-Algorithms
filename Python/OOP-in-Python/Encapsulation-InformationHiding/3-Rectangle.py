# Implementing Rectangle Class Using Encapsulation
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    
    def area(self):
        Area = self.__length * self.__width
        return Area
    
    def perimeter(self):
        Perimeter = 2 * (self.__length + self.__width)
        return Perimeter

obj = Rectangle(4, 5)
print(obj.area())
print(obj.perimeter())