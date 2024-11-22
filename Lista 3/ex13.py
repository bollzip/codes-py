class Veiculo:
    def __init__(self, modelo, velocidade=0):

        self.modelo = modelo
        self.velocidade = velocidade

    def aumentar_velocidade(self, incremento):
       
        self.velocidade += incremento
        print(f"A velocidade do {self.modelo} aumentou para {self.velocidade} km/h.")


veiculo1 = Veiculo("Fusca", 30)
veiculo1.aumentar_velocidade(20)  
