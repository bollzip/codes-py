class Quadrado:
    def __init__(self, lado):
        
        self.lado = lado

    def calcular_area(self):
       
        return self.lado ** 2

    def calcular_perimetro(self):
     
        return 4 * self.lado


quadrado1 = Quadrado(5)
print(f"A área do quadrado é: {quadrado1.calcular_area()} unidades quadradas.")
print(f"O perímetro do quadrado é: {quadrado1.calcular_perimetro()} unidades.")
