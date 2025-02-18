# Challenge 1: Implement a Banking Account
class Account: # parent class
    # Instance variables
    def __init__(self, title = None, balance = 0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account): # child class
    # instance variables
    def __init__(self, title = None, balance = 0, interestRate = 0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    # created a method to print this details
    def PrintDetails(self):
        print("Account", self.balance)
        print("Savings Account Interest", self.interestRate)

obj1 = Account("Mark", 5000)
obj2 = SavingsAccount("Mark", 5000, 5)
obj2.PrintDetails()
