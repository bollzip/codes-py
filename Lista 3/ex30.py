class Carro:
    def __init__(self, marca, combustivel_maximo):
        
        self.marca = marca
        self.combustivel_maximo = combustivel_maximo 
        self.combustivel_atual = 0  

    def abastecer(self, quantidade):
        
        if quantidade <= 0:
            print("Quantidade de combustível inválida. O valor deve ser maior que zero.")
        elif self.combustivel_atual + quantidade > self.combustivel_maximo:
            print(f"Não é possível abastecer {quantidade}. O tanque só pode comportar até {self.combustivel_maximo - self.combustivel_atual}.")
            self.combustivel_atual = self.combustivel_maximo
        else:
            self.combustivel_atual += quantidade
            print(f"Abastecido {quantidade} litros. Combustível atual: {self.combustivel_atual} litros.")

    def verificar_combustivel(self):
       
        print(f"O nível de combustível do {self.marca} é {self.combustivel_atual} litros.")


carro = Carro(marca="Fusca", combustivel_maximo=50)


carro.abastecer(20)
carro.abastecer(40)  
carro.abastecer(-5)  


carro.verificar_combustivel()
