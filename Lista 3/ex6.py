class Animal:
    def __init__(self, especie, som):
        self.especie = especie
        self.som = som
    
    def emitir_som(self):
        print(f"O {self.especie} faz o som: {self.som}")


animal1 = Animal("Cachorro", "Au Au")

animal1.emitir_som()
