class Pessoa:
    def __init__(self, nome, altura, peso):
        
        self.nome = nome
        self.altura = altura
        self.peso = peso

    def calcular_imc(self):
      
        imc = self.peso / (self.altura ** 2)
        return imc

    def classificar_imc(self):
       
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidade"


pessoa1 = Pessoa(nome="Carlos", altura=1.75, peso=70)
pessoa2 = Pessoa(nome="Maria", altura=1.60, peso=50)


imc1 = pessoa1.calcular_imc()
imc2 = pessoa2.calcular_imc()

print(f"{pessoa1.nome} - IMC: {imc1:.2f}, Classificação: {pessoa1.classificar_imc()}")
print(f"{pessoa2.nome} - IMC: {imc2:.2f}, Classificação: {pessoa2.classificar_imc()}")
