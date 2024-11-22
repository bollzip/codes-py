class Jogo:
    def __init__(self, nome):
        
        self.nome = nome
        self.pontuacao = 0  

    def iniciar_jogo(self):
    
        print(f"Iniciando o jogo: {self.nome}")
        self.pontuacao = 0  

    def registrar_pontuacao(self, pontos):
     
        if pontos > 0:
            self.pontuacao += pontos
            print(f"Pontuação de {pontos} registrada. Pontuação total: {self.pontuacao}")
        else:
            print("Valor de pontos inválido. A pontuação deve ser maior que zero.")

    def exibir_pontuacao(self):
        
        print(f"Pontuação atual no jogo {self.nome}: {self.pontuacao}")


jogo = Jogo(nome="Aventura no Espaço")


jogo.iniciar_jogo()


jogo.registrar_pontuacao(50)
jogo.registrar_pontuacao(30)


jogo.exibir_pontuacao()


jogo.registrar_pontuacao(-10)
