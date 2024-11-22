class Funcionario:
    def __init__(self, nome, salario):
       
        self.nome = nome
        self.salario = salario

    def calcular_aumento(self, percentual):
       
        aumento = self.salario * (percentual / 100)
        self.salario += aumento
        print(f"O salário de {self.nome} foi aumentado para {self.salario:.2f} após um aumento de {percentual}%.")


funcionario1 = Funcionario(nome="Carlos Souza", salario=3000.00)


funcionario1.calcular_aumento(10)


print(f"Novo salário de {funcionario1.nome}: {funcionario1.salario:.2f}")
