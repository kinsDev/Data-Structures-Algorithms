class Parent:
    def prn(self):
        print("Parent")

class Child(Parent):
    def __init__(self):
        self.a = Parent() 
        # inside a Child object, there's an attribute that holds a separate Parent object
        # overridden prn() method
    def prn(self):
        print("Child") # the Child class has it's own prn() method that overrides the prn() method from the Parent class

temp = Child() # this creates an instance of the Child Class
temp.a.prn() # __init__ method of Child is called. self.a = Parent() creates a new Parent object, and assigns it to temp.a
# So we are basically accessing prn() of Parent
# Here, temp.a refers to the Parent object that was created inside the Child's __init__ method.
# Since a is an instance of Parent, calling temp.a.prn() invokes the prn() method of the Parent class .





# Another example, but slightly different
class Parent:
    def prn(self):
        print("Parent")


class Child(Parent):
    def __init__(self):
        self.a = Parent()

    def prn(self):
        print("Child")


temp = Child()
temp.prn()
