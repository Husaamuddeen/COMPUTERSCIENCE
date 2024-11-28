'''Challenge: 
Create a Python class for a Bank. Implement a constructor that initializes an empty list to store bank accounts.
Create methods to add a new account to the bank, find an account by account number,
deposit money into an account, withdraw money from an account, and display all accounts' information.
Instantiate more than one object from the class, and show suitable testing.  '''

class Bank:
    __bankName = ""
    __accounts = []
    def __init__(self, newBankName):
        self.__bankName = newBankName
        self.__accounts = []

    def addAccount(self, newAccount):
        self.__accounts.append(newAccount)

    def findAccount(self, idSearch):
        for i in range len(self.__accounts)
            if idSearch == self.__accounts[i].getID():
                self.__accounts[i].displayInfo()

class BankAccount:
    __name = ""
    __id = 0
    __balance = 0
    def __init__(self, newName, newID, newBalance):
        self.__name = newName
        self.__id = newID
        self.__balance = newBalance
    
    def deposit(self, amount):
        self.__balance = self.__balance + amount
    
    def withdraw(self, amount):
        self.__balance = self.__balance - amount

    def displayInfo(self):
        print("name: "+self.__name)
        print("id: "+str(self.__id))
        print("balance: "+str(self.__balance))
    
    def getID(self):
        return self.__id
    
HusaamsBank = Bank("Husaam's Bank")
