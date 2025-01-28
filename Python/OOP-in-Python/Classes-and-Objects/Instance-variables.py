# Properties can be defined in two parts: 
# 1. Class variables & Instance variables

# Class variables share properties for all objects in a class while instance variables have unique properties for objects in a class

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
