
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self, outra_pessoa):
        print(f"Olá, {outra_pessoa.nome}!")


pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)


pessoa1.cumprimentar(pessoa2)
