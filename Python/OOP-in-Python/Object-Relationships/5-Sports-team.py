# Challenge 2: Implementing a Sports Team!

# In this exercise, you have to perform aggregation between 3 classes.

# You have to implement 3 classes, School, Team, and Player, 
# such that an instance of a School should contain instances of Team objects. 
# Similarly, a Team object can contain instances of Player class.

class Player:
    def __init__(self, ID, name, teamName):
        self.ID = ID
        self.name = name
        self.teamName = teamName

class Team:
    def __init__(self, name):
        self.name = name
        self.players = [] # initialize an empty list of players

    def addPlayer(self, player): # this method will accept a player object and add it to the players list
        if isinstance(player, Player): # Ensure the argument is a player instance
            self.players.append(player)
        else:
            print("Error: only Player objects can be added")

    def getNumberOfPlayers(self): # this method will return the total numer of players currently in the team
        return len(self.players)

class School:
    def __init__(self, name):
        self.name = name
        self.teams = []
    
    def addTeam(self, team):
        if isinstance(team, Team): # to ensure that the argument is a Team instance
            self.teams.append(team)
        else:
            print("Error: Only Team objects can be added")
    
    def getTotalPlayersInSchool(self):
        # I need to iterate through all teams in self.teams and sum up their player counts.
        total_players = sum(team.getNumberOfPlayers() for team in self.teams)
        return total_players