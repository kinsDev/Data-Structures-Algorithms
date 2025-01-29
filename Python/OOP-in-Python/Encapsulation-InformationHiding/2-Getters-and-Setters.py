# Getters and Setters as we said in the previous file in Encapsulation
# Are methods used to be able to get details of binded data(capsules - private classes that are encapsulated)

# A getter method allows reading of a property's value - getPropertyName()
# A setter method allows manipulating the content of a property's value - setPropertyName(value)

# Let's get and set methods for the __username in our User class
class User:
    def __init__(self, username = None): # defining initializer
        self.__username = username

    def setUsername(self, x):
        self.__username = x
    
    def getUsername(self):
        return(self.__username)

Obj = User("Kinsley")
print("Before setting:", Obj.getUsername())

Obj.setUsername("Kaimenyi")
print("After setting:", Obj.getUsername())