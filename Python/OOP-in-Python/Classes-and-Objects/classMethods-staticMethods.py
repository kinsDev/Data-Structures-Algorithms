# CLASS METHODS

# Class methods use decorator @classmethod, and instead of self we use cls to refer to the class
# Class methods are accessed using the class name and can be accessed without creating a class object.

class Player:
    # class variable
    teamName = "Liverpool"

    def __init__(self, name):
        self.name = name
    
    # instead of creating class object we just use the class method decorator
    @classmethod
    def getTeamName(cls):
        return cls.teamName

print(Player.getTeamName())
print("\n")


# STATIC METHODS

# Static methods are methods that are usually limited to class only and not their objects. 
# They have no direct relation to class variables or instance variables.
# Static methods can be accessed using the class name or object name
# We use decorator @staticMethod and we don't self or cls

class Player:
    teamName = "Liverpool" # creating the class variable

    def __init__(self, name):
        self.name = name   # creating the instance variable
    
    @staticmethod
    def demo():
        print("I am a static method")

p1 = Player("lol")
p1.demo()
Player.demo()
print(Player.teamName)