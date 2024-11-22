class Agenda:
    def __init__(self):
        
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        
        contato = {"nome": nome, "telefone": telefone}
        self.contatos.append(contato)
        print(f"Contato de {nome} adicionado com sucesso.")

    def listar_contatos(self):
      
        if self.contatos:
            print("Lista de Contatos:")
            for contato in self.contatos:
                print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")
        else:
            print("A agenda está vazia.")

agenda = Agenda()


agenda.adicionar_contato("João Silva", "1234-5678")
agenda.adicionar_contato("Maria Oliveira", "9876-5432")


agenda.listar_contatos()
