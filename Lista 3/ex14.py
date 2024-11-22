class Eletrodomestico:
    def __init__(self, nome, potencia):
        
        self.nome = nome
        self.potencia = potencia

    def ligar(self):
        
        print(f"{self.nome} foi ligado! Potência: {self.potencia} watts.")


eletrodomestico1 = Eletrodomestico("Geladeira", 150)
eletrodomestico1.ligar()  
