class Filme:
    def __init__(self, titulo, duracao):
       
        self.titulo = titulo
        self.duracao = duracao

    def exibir_detalhes(self):
        
        print(f"Título: {self.titulo}")
        print(f"Duração: {self.duracao} minutos")


filme1 = Filme("O Senhor dos Anéis: A Sociedade do Anel", 178)
filme1.exibir_detalhes()
