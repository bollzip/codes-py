from classaccount import *

class BusinessAccount(Account):
    def __init__(self, number: int, holder: str, balance: float, loanLimit: float):
        super().__init__(number, holder, balance)
        self.loanLimit = loanLimit
    def loan(self, amount: float):
        pass
        if amount > 0 and amount <= self.loanLimit:
            self.balance += amount
            self.loanLimit -= self.loanLimit
        else:
            print("Valor inválida ou sem limite")

    def __str__(self):
        return f"Bussines conta({self.numer}, {self.holder}, Balance {self.balance:.2f}, Loanlimit {self.loanLimit})"
    
acc = Account(123,"Pedro Bollsinha", 3.50)
print (f"Primeiro print: {acc}")
acc.deposit(5.50)
print(f"Segundo print: {acc}")
acc.withdraw(1.50)
print (f"Terceiro print: {acc}")

b_acc = BusinessAccount(321, "Padaria", 500.0, 200.0)
print (f"1 BC: {b_acc}")
b_acc.loan(200.0)
print (f"2 BC: {b_acc}")



  
        


        
    