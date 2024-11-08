'''Challenge: 
Design a Python class for a Bank Account.
The constructor should take parameters for the account holder's name and initial balance.
Implement private attributes for these parameters.
Create methods to deposit and withdraw money from the account, as well as to display the account's balance.

Instantiate more than one object from the class, and show suitable testing.  '''

class BankAccount:
    #private name and balance
    __name = ""
    __balance = 0
    #constructor method
    def __init__(self, theName, theBalance):
        self.__name = theName
        self.__balance = theBalance
    #method to deposit money
    def deposit(self, amount):
        self.__balance = self.__balance + amount
    #method to withdraw money
    def withdraw(self, amount):
        self.__balance = self.balance - amount
    #method to display the account
    def display(self):
        print(self.__name+", £"+str(self.__balance))

#instantiate a bank account
husaam = BankAccount("Husaam",1000000000000000)
eesa = BankAccount("Eesa",-30)

husaam.display()