class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def verificar_aprovacao(self):
        if self.nota >= 7:
            print(f"{self.nome} está aprovado!")
        else:
            print(f"{self.nome} está reprovado.")


aluno1 = Aluno("Maria", 8)


aluno1.verificar_aprovacao()


aluno2 = Aluno("João", 5)


aluno2.verificar_aprovacao()
