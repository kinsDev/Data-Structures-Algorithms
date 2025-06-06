# Assigning values in the main code
class Employee:
    # Properties of that class and assigned with None
    # If we don't initialize the properties in the Employee Class, the code will not run
    # Classes contain properties or attributes that are identical for all objects in the same class
    # Methods are used to obtain properties of a class and are used to perform an action on an object
    # of a class. 
    ID = None
    salary = None
    department = None

# Create an object for the Employee class
Kinsley = Employee()

# Assign values to properties of Kinsley - an object of the Employee class
Kinsley.ID = 388700
Kinsley.salary = 3500
Kinsley.department = "AI & Data"

print("Kinsley's ID is", Kinsley.ID)
print("Kinsley's salary is", Kinsley.salary)
print("Kinsley's department is", Kinsley.department)
print("\n")

# Assigning values when defining the class 
class Employees:
    # I am defining properties of a class and assigning values to them
    id = 3789
    salarys = 2500
    departments = "Human Resource"

# I will then create an object with an employee class
# This object could be a person. So we can different people or objects in the same class and they will share the same properties
# in this case id, salary, and departments
Steve = Employees()

# lets print the properties of Steve - an object of an Employees class
# To access the properties of an object in a class, the dot notation in used e.g Employee.ID
print("Steve's ID No. is", Steve.id)
print("Steve's salary is", Steve.salarys)
print("Steve's department is", Steve.departments)
print("\n")

# Now let's create properties outside a Class
# In the already existing ID, salary, department properties on the Employee class, we will add the title property

class Stuff:
    # properties of a stuff member
    ID = None
    salary = None
    department = None

# create an object for that class
Kaimenyi = Stuff()

# Assign values to the properties of Kaimenyi - an object of the Stuff class
Kaimenyi.ID = 388700
Kaimenyi.salary = 4000
Kaimenyi.department = "Technical"
# Adding another property that wasn't a part of the initial class properties
Kaimenyi.title = "Machine Learning Engineer"

# printing properties of Kaimenyi
print("ID:", Kaimenyi.ID)
print("salary:", Kaimenyi.salary)
print("department:", Kaimenyi.department)
print("title:", Kaimenyi.title)