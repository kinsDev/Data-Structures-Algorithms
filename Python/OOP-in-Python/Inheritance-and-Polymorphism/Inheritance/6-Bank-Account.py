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

obj1 = Account("Mark", 5000)
obj1 = SavingsAccount("Mark", 5000, 5)