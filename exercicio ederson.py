class Bola:
    def __init__(self, cor, circunferencia, material):
        
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, nova_cor):
        
        self.cor = nova_cor
        print(f"A cor da bola foi alterada para {self.cor}")

    def mostra_cor(self):
       
        print(f"A cor da bola é {self.cor}")


bola1 = Bola(cor="vermelha", circunferencia=30, material="borracha")


bola1.mostra_cor()


bola1.troca_cor("azul")


bola1.mostra_cor()
