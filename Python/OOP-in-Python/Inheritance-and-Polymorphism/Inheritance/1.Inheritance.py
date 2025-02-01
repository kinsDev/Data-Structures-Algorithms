# Inheritance provides a way to create a new class from an existing class. 
# The new class is a specialized version of the existing class such that it 
# inherits all the non-private fields (variables) and methods of the existing class. 
# The existing class is used as a starting point or as a base to create the new class.


# In inheritance, in order to create a new class based on an existing class, 
# we use the following terminology:
# Parent Class(Super Class or Base Class): This class allows the reuse of its public properties in another class .
# Child Class(Sub Class or Derived Class): This class inherits or extends the superclass.

class ParentClass:
    # attributes of the parent class

class ChildClass(ParentClass):
    # public attributes of the ParentClass
    # attributes of the ChildClass