class Elevador:
    def __init__(self, totalAndares):
        
        self.andarAtual = 0  
        self.totalAndares = totalAndares

    def subir(self, andares):
        
        if self.andarAtual + andares <= self.totalAndares:
            self.andarAtual += andares
            print(f"Elevador subiu para o andar {self.andarAtual}.")
        else:
            print(f"Não é possível subir {andares} andares. O elevador já está no último andar.")

    def descer(self, andares):
        
        if self.andarAtual - andares >= 0:
            self.andarAtual -= andares
            print(f"Elevador desceu para o andar {self.andarAtual}.")
        else:
            print(f"Não é possível descer {andares} andares. O elevador já está no térreo.")


elevador = Elevador(totalAndares=10)  

elevador.subir(3)  
elevador.descer(1)  
elevador.subir(9)  
elevador.descer(5)  
