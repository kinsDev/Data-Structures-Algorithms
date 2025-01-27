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
print("ID:", Kaimenyi.ID)
print("salary:", Kaimenyi.salary)
print("department:", Kaimenyi.department)
print("title:", Kaimenyi.title)
print("\n")
print("ID:", Kinsley.ID)
print("salary:", Kinsley.salary)
print("department:", Kinsley.department)
print("title:", Kinsley.title)