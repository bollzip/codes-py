class ContaBancaria:
    def __init__(self, numero, titular, saldo=0):
        
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def deposito(self, valor):
      
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor} realizado na conta {self.numero}.")
        else:
            print("Valor de depósito inválido.")

    def saque(self, valor):
  
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor} realizado da conta {self.numero}.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def obter_saldo(self):
        
        return self.saldo


class Banco:
    def __init__(self):
       
        self.contas = []

    def adicionar_conta(self, conta):
       
        self.contas.append(conta)

    def listar_saldos(self):
      
        if not self.contas:
            print("Não há contas no banco.")
        else:
            print("Saldos das contas:")
            for conta in self.contas:
                print(f"Conta {conta.numero} - Titular: {conta.titular} - Saldo: {conta.obter_saldo():.2f}")



conta1 = ContaBancaria(numero=101, titular="João Silva", saldo=1500.00)
conta2 = ContaBancaria(numero=102, titular="Maria Oliveira", saldo=3200.50)
conta3 = ContaBancaria(numero=103, titular="Carlos Souza", saldo=980.75)


banco = Banco()


banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)
banco.adicionar_conta(conta3)


banco.listar_saldos()
