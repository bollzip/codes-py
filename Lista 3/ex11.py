class ContaBancaria:
    def __init__(self, saldo_inicial=0):
       
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Deposito de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}")
        else:
            print("Valor de depósito inválido. O valor deve ser maior que 0.")
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}")
        elif valor > self.saldo:
            print("Saldo insuficiente para o saque.")
        else:
            print("Valor de saque inválido. O valor deve ser maior que 0.")


conta = ContaBancaria(1000)  


conta.depositar(500)  


conta.sacar(200)  


conta.sacar(2000)  
