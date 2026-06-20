class Account:

    def __init__(self, name, acno, balance):
        self.name = name
        self.acno = acno
        self.balance = balance

    # Method to display the account details
    def display_account_info(self):
        print("Name:", self.name)
        print("Account Number:", self.acno)
        print("Balance:", self.balance)

    # -------------------------------------

    # Method to deposit money into the account
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited: Rs.", amount)
        print("Available Balance: Rs.", self.balance)

    # -------------------------------------

    # Method to withdraw money from the account
    def withdraw(self, account):
        if (self.balance - amount)
          self.balance+=amount
        print("Amount deposited: Rs.",amount)
        print("Available Balance: Rs.",self.balance)
    #---------------------------------------------------
    #Method to withdraw money from the account
    def withdraw(self,amount):
        if (self.balance- amount) < 1000:
            print("Insufficient Balance!")
        else:
            self.balance-=amount
            print("Amount withdrawn: Rs.",amount)
            print("Available Balance: Rs.",self.balance)
    #---------------------------------------------------
    #method to display available balance
    def display_balance(self):
        print("Available Balance: Rs.",self.balance)
#-------------------------------------------------------------------------------