class Calculadora:
    def somar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b


calculadora = Calculadora()


resultado_soma = calculadora.somar(10, 5)
resultado_subtracao = calculadora.subtrair(10, 5)


print(f"A soma de 10 e 5 é: {resultado_soma}")
print(f"A subtração de 10 e 5 é: {resultado_subtracao}")