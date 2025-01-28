# Properties can be defined in two parts: 
# 1. Class variables & Instance variables

# Class variables share properties for all objects in a class while instance variables have unique properties for objects in a class

# First example, just commented out
class Player:
    # Class variable
   teamName = "Liverpool"
   
   # Instance variable
   def __init__(self, playerName):
        self.playerName = playerName

p1 = Player("Kinsley")
p2 = Player("Kaimenyi")

print("Player Name", p1.playerName)
print("Player 1 team name", p1.teamName)
print("\n")
print("Player Name", p2.playerName)
print("Player 2 team name", p2.teamName)



# Second example
class Player:
    # class variable
    TeamName = "Liverpool"

    # Instance variable
    def __init__(self, playerName, previousTeam):
        self.playerName = playerName
        self.previousTeam = previousTeam

player1 = Player("Lionel Messi", "FC Barcelona")
player2 = Player("Christiano Ronaldo", "Real Madrid")

print(f"Player Name: {player1.playerName}, Current Team is: {Player.TeamName}, Previous Team is: {player1.previousTeam}")
print(f"Player Name: {player2.playerName}, Current Team is: {Player.TeamName}, Previous Team is: {player2.previousTeam}")

print("\n")

# Third and Final exaple. This will be on people owning cars "Yes as a collective"
# And what cars to be specific since they will own unique cars from one another

class Car:
    # Class variables
    ownCars = "Yes"

    # Instance variables
    def __init__(self, carOwnerName, typeOfCar):
        self.carOwnerName = carOwnerName
        self.typeOfCar = typeOfCar

Owner1 = Car("Kinsley Kaimenyi", "Mercedes")
Owner2 = Car("Loved Ones", "Bugahtti")

print(f"Is it: {Car.ownCars}? The first car owner's name is: {Owner1.carOwnerName}, and he owns this car: {Owner1.typeOfCar}")
print(f"Is it: {Car.ownCars}? The second car owner will go to a collective of my: {Owner2.carOwnerName}, and they own a: {Owner2.typeOfCar}")


# Using Class Variables Smartly
# Class variables are useful when implementing properties that should be common and accessible to all class objects
class Player:
    # class variable
    teamName = "Liverpool"
    teamMembers = []

    # instance variable
    def __init__(self, name):
        self.name = name
        self.formerTeams = []
        self.teamMembers.append(self.name)

p1 = Player("Kinsley")
p2 = Player("Kaimenyi")

print("Name:", p1.name)
print("Team Members:")
print(p1.teamMembers)
print("")
print("Name:", p2.name)
print("Team Members:")
print(p2.teamMembers)