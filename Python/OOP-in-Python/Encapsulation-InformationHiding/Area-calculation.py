# Calculate area of a circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def print_area(self):
        pi = 3.14
        area = pi * (self.radius ** 2)
        print(round(area, 2))  # print the area rounded to 2 decimal places

obj = Circle(5)
obj.print_area()
