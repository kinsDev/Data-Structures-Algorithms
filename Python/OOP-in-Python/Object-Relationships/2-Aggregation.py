# Aggregation
# Aggregation follows the Has-A model. This creates a parent-child relationship between two 
# classes, with one class owning the object of another.

# In aggregation, the lifetime of the owned object does not depend on the lifetime of the owner.
# The owner object could get deleted, but the owned object can continue to exist in the program.




# Example
# Let’s take the example of people and their country of origin. 
# Each person is associated with a country, but the country can exist without that person.

class Country:
    def __init__(self, name=None, population=0):
        self.name = name
        self.population = population
    
    def printDetails(self):
        print("Counntry Name:", self.name)
        print("Country Population:", self.population)

class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    
    def printDetails(self):
        print("Person Name:", self.name)
        self.country.printDetails()


c = Country("Wales", 1500)
p = Person("Joe", c)
p.printDetails()

# deletes the object p
del p
print("")
c.printDetails()
