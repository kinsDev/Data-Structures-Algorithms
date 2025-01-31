class User:
    def __init__(self, username=None, password=None):
        self.__username = username # private attribute
        self.__password = password # private attribute
    
    def login(self, username, password):
        if ((self.__username.lower() == username.lower()) and (self.__password == password)):
            print("Access granted against username", 
                  self.__username.lower(), 
                  "and password", self.__password)
        else:
            print("Invalid credentials Access Denied!")

# We will now create an object for the class
Kinsley = User("Kinsley", "1234@looby")

# With the credentials created for that object, next thing will be to log in
Kinsley.login("Kinsley", "1234@looby") # will grant access because credentials are valid
print("\n")

# The two calls below will lead to an error since the credentials are invalid
Kinsley.login("Kaimenyi", "1234@looby") # compilation error will occur due to this line Kinsley.__username
print("\n")
Kinsley.login("Kinsley", "1234@booly") # compilation error will occure due to this line Kinsley.__password