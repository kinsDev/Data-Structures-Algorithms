# Methods cannot be explicitly overloaded in Python but can be implicitly overloaded
# It is a good practice to overload methods in Python to be able to save computer memory

class Employee:
    # defining the properties and assigning them to none
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department
    
    # Method overloading
    def demo(self, a, b, c, d=5, e=None):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)
    
    def tax(self, title=None):
        return (self.salary * 0.2)
    
    def salaryPerDay(self):
        return (self.salary / 30)

# After defining the properties of objects in a class in the initialization
# we create an object to that class

Steve = Employee()

# Printing properties of Steve
print("Demo 1")
Steve.demo(1, 2, 3)
print("\n")

print("Demo 2")
Steve.demo(1, 2, 3, 4)
print("\n")

print("Demo 3")
Steve.demo(1, 2, 3, 4, 5)
print("\n")

print("Demo 4")
Steve.demo("Kinsley", "K", "G", "texty", "Machine Learning Engineer")
print("\n")

#print("Demo 5")
# Steve.demo("Dooly", 7) # We will have this error here: missing 1 required positional argument: 'c'
#print("\n")

# We will have this error below here: takes from 4 to 6 positional arguments but 7 were given
#print("Demo 6")
#Steve.demo("Kinsley", "K", "G", "texty", "Machine Learning Engineer", "can")

# If we redefine a method several times, and give it different arguments,
# Python uses the latest method definition for its implementation