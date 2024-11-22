class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
    
    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Ano: {self.ano}")

# Instanciando um objeto da classe Carro
carro1 = Carro("Toyota", 2020)

# Exibindo as informações do carro
carro1.exibir_informacoes()
