class Calculadora:
    def __init__(self):
        # Inicializa a lista de histórico de operações
        self.historico = []

    def adicionar(self, a, b):
        # Soma dois números e adiciona a operação ao histórico
        resultado = a + b
        self.historico.append(f"{a} + {b} = {resultado}")
        return resultado

    def subtrair(self, a, b):
       
        resultado = a - b
        self.historico.append(f"{a} - {b} = {resultado}")
        return resultado

    def multiplicar(self, a, b):
        
        resultado = a * b
        self.historico.append(f"{a} * {b} = {resultado}")
        return resultado

    def dividir(self, a, b):
    
        if b != 0:
            resultado = a / b
            self.historico.append(f"{a} / {b} = {resultado}")
            return resultado
        else:
            self.historico.append(f"Erro: divisão por zero")
            return "Erro: divisão por zero"

    def mostrar_historico(self):
        
        if self.historico:
            print("Histórico de operações:")
            for operacao in self.historico:
                print(operacao)
        else:
            print("Nenhuma operação realizada.")


calc = Calculadora()


print(calc.adicionar(5, 3))  
print(calc.subtrair(10, 4))  
print(calc.multiplicar(7, 6))  
print(calc.dividir(12, 4))  
print(calc.dividir(5, 0))  


calc.mostrar_historico()
