class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura

# Instanciando um objeto da classe Retangulo
retangulo1 = Retangulo(5, 3)

# Calculando e imprimindo a área
area = retangulo1.calcular_area()
print(f"A área do retângulo é: {area}")
