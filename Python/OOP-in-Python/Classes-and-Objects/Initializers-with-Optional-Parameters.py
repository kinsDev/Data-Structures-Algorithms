# The default initializer has all properties as optional.
# We will practice that by creating a class Employee with two objects in it
# One object without the initializer parameters, and one with the initializer parameters

class Employee:
    def __init__(self, ID = None, salary = 0, department = None, title = None):
        self.ID = ID
        self.salary = salary
        self.department = department
        self.title = title

# Create two objects for the employee class
# 
# Object with default parameters 
Kaimenyi = Employee()

# Object with initialized parameters
Kinsley = Employee(388700, 4000, "AI & Data", "Machine Learning Engineer")

# print the objects with their attributes or properties
print("Kaimenyi's ID:", Kaimenyi.ID)
print("Kaimenyi's salary:", Kaimenyi.salary)
print("Kaimenyi's department:", Kaimenyi.department)
print("Kaimenyi's title:", Kaimenyi.title)
print("\n")
print("Kinsley's ID:", Kinsley.ID)
print("Kinsley's salary:", Kinsley.salary)
print("Kinsley's department:", Kinsley.department)
print("Kinsley's title:", Kinsley.title)
