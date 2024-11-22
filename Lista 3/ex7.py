class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def aplicar_desconto(self, percentual):
        desconto = (self.preco * percentual) / 100
        self.preco -= desconto
        print(f"O preço com desconto de {percentual}% é: R${self.preco:.2f}")


produto1 = Produto("Camiseta", 50.00)


produto1.aplicar_desconto(20)
