# The double underscore in the initializer is used to show python interpreter that this is a special method
# The initializer (__init__) is followed by a keyword (self) which is a way to refer to the object being initialized
# The initializer method does not have a '''return type'''

class Employee:
    # defining the properties and assisgning them none
    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department

# After that we create an object of the Employee class and assign it with values
Kinsley = Employee(388700, 4000, "AI & Data")

# printing properties of Kinsley
print("ID:", Kinsley.ID)
print("Salary:", Kinsley.salary)
print("Department:", Kinsley.department)