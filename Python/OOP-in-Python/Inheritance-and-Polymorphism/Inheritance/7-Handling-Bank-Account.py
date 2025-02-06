# Challenge 2: Handling a Bank Account
class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    # Task 3-implement the withdrawal(amount) method that subtracts the amount from the balance. It does not return anything.
    def withdrawal(self, amount):
        self.balance = self.balance - amount # after withdrawal, the new balance will be...
        pass
    
    # Task 2-implement the deposit(amount) method that adds amount to the balance. It does not return anything.
    def deposit(self, amount):
        self.amount = amount
        self.balance = amount + self.balance # after withdrawal, the new balance will be...
        pass

    # Task 1-implement the getBalance() method that returns balance.
    def getBalance(self):
        return self.balance
        pass

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.interestRate * self.balance) / 100
        pass


# code to test - do not edit this
demo1 = SavingsAccount("Mark", 2000, 5)  # initializing a SavingsAccount object
