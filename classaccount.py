class Account:
    def __init__(self,number:int,holder:str,balance:float):
        self.number=number 
        self.holder=holder
        self.balance=balance
    def withdraw(self,amount: float):
        if self.balance>amount:
            self.balance=self.balance-amount
            return self.balance
        else:
            print("can't withdraw more than you have")
    def deposit(self,amount:float):
        self.balance=self.balance+amount
        return self.balance