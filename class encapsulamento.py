class ContaBancaria:
    def __init__(self, nome, cpf, senha, saldo=0):
        
        self.__cpf = cpf   
        self.__senha = senha         
        self.__saldo = saldo  

    def validar_senha(self, senha):

        return senha == self.__senha

    def sacar(self, senha, valor):

        if not self.validar_senha(senha):
            return "Senha inválida."
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso."
        else:
            return "Saldo insuficiente ou valor inválido."

    def extrato(self, senha):

        if not self.validar_senha(senha):
            return "Senha inválida."
        return f"Extrato: Saldo atual é R${self.__saldo:.2f}."

    def depositar(self, valor):

        if valor > 0:
            self.__saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso."
        else:
            return "Valor de depósito inválido."

def menu():
    print("\n--- Menu Banco Digital ---")
    print("1. Consultar Extrato")
    print("2. Sacar")
    print("3. Depositar")
    print("4. Sair")

def main():
    print("Bem-vindo ao Banco Digital!")
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    senha = input("Crie uma senha para sua conta: ")

    conta = ContaBancaria(nome, cpf, senha)

    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":

            senha_input = input("Digite sua senha: ")
            print(conta.extrato(senha_input))
        elif opcao == "2":

            senha_input = input("Digite sua senha: ")
            valor = float(input("Digite o valor a ser sacado: R$"))
            print(conta.sacar(senha_input, valor))
        elif opcao == "3":

            valor = float(input("Digite o valor a ser depositado: R$"))
            print(conta.depositar(valor))
        elif opcao == "4":
            
            print("Obrigado por usar o Banco Digital. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
