# Public attributes
# Public attributes are those that can be accessed inside the class and outside the class.
class Employee:
    # defining properties of the object on the initializer
    def __init__(self, ID, salary):
        self.ID = ID
        self.salary = salary

    # A public method to display the ID - to shocase that I can access this info
    # from inside and outside the class
    def displayID(self):
        #print("ID from inside class", self.ID)
        return self.ID

# creating object to class Employee
Kinsley = Employee(388700, 5000)

print("ID from inside class", Kinsley.displayID())
print("ID from outside class", Kinsley.ID)
print("Salary", Kinsley.salary)
print("\n")


# Private Attributes
# Private attributes cannot be accessed directly from outside the class but can be accessed from inside the class .
# We can make members private using the double underscore __ prefix
# Implementing Private methods:
class Employee:
    # initializer
    def __init__(self, ID, salary):
        self.ID = ID            # public property
        self.__salary = salary  # private property
    
    # Instance Methods
    def displaySalary(self): # public method
        print("Salary", self.__salary)
        
    def __displayID(self):   # private method
        print("ID", self.ID)

# Object for the class
Kinsley = Employee(388700, 5000)

print("Salary:", Kinsley.displaySalary())
print("ID:", Kinsley.__displayID()) # This will display an error
print("\n")

# We can access a private attribute in the main code by first stating className. 
# Object._ClassName__privateAttribute

class Employee:
    def __init__(self, ID, salary):
        self.ID = ID # Public attribute
        self.__salary = salary # Private attribute
    
    def displaySalary(self):           # public method
        print("Salary", self.__salary)
    
    def __displayID(self):             # privare method
        print("ID", self.ID)

Kinsley = Employee(388700, 7000)
Kinsley.displaySalary()
Kinsley._Employee__displayID()