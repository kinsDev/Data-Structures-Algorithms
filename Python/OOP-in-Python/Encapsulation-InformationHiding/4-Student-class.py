# Implementing the Complete Student Class

class Student:
    def __init__(self, name, rollNumber):
        self.__name = name
        self.__rollNumber = rollNumber
    
    def setName(self, newSetName):
        self.__name = newSetName

    def getName(self):
        return self.__name
    
    def setRollNumber(self, newRollNumber):
        self.__rollNumber = newRollNumber

    def getRollNumber(self):
        return self.__rollNumber

obj1 = Student("Kinsley", 1073)
print(obj1.getName())
obj1.setName("Kaimenyi")
print(obj1.getName())
print(obj1.getRollNumber())
obj1.setRollNumber(1503)
print(obj1.getRollNumber())


# Lets solve this question without using the init method
# We have initialized the two properties name & rollNumber on the two set methods
# That eliminated the need to use the initializers
class Student:
    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name
    
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber
    
    def getRollNumber(self):
        return self.__rollNumber
    