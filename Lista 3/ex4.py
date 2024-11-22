class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
    
    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Ano: {self.ano}")


carro1 = Carro("Toyota", 2020)


carro1.exibir_informacoes()
