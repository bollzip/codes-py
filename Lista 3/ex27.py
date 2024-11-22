class Animal:
    def __init__(self, nome, tipo):
        
        self.nome = nome
        self.tipo = tipo

    def mover(self):
        
        if self.tipo == "peixe":
            print(f"O {self.nome} nada.")
        elif self.tipo == "pássaro":
            print(f"O {self.nome} voa.")
        elif self.tipo == "cachorro":
            print(f"O {self.nome} corre.")
        else:
            print(f"O {self.nome} se move de uma maneira desconhecida.")


peixe = Animal(nome="Peixe dourado", tipo="peixe")
passaro = Animal(nome="Papagaio", tipo="pássaro")
cachorro = Animal(nome="Rex", tipo="cachorro")
outro_animal = Animal(nome="Cavalo-marinho", tipo="desconhecido")


peixe.mover()  
passaro.mover()  
cachorro.mover() 
outro_animal.mover()  
