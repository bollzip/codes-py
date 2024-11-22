class Pessoa:
    def __init__(self, nome, idade, altura):
  
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def verificar_altura(self):
      
        if self.altura > 1.75:
            return True
        else:
            return False


pessoa1 = Pessoa(nome="João", idade=30, altura=1.80)
pessoa2 = Pessoa(nome="Maria", idade=25, altura=1.60)

print(f"{pessoa1.nome} é mais alta que 1,75m? {pessoa1.verificar_altura()}")
print(f"{pessoa2.nome} é mais alta que 1,75m? {pessoa2.verificar_altura()}")
