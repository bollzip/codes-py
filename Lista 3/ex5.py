class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def exibir_detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")


livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")

livro1.exibir_detalhes()
