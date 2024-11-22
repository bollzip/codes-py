class Livro:
    def __init__(self, titulo, autor, preco, estoque):
       
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.estoque = estoque

    def verificar_estoque(self):
        
        return self.estoque

    def vender_livro(self, quantidade):
       
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            print(f"{quantidade} livro(s) vendido(s). Estoque atual: {self.estoque}")
        else:
            print(f"Estoque insuficiente. Apenas {self.estoque} livro(s) disponível(is).")


livro1 = Livro(titulo="Python para Iniciantes", autor="João Silva", preco=49.90, estoque=10)


print(f"Estoque inicial do livro '{livro1.titulo}': {livro1.verificar_estoque()}")


livro1.vender_livro(3)


print(f"Estoque após a venda: {livro1.verificar_estoque()}")


livro1.vender_livro(8)
