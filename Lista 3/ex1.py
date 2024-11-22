class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"


pessoa1 = Pessoa("João", 30)


print(pessoa1)
