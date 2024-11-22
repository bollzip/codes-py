from pydantic import BaseModel
class Usuario (BaseModel):
    nome: str
    idade: int
    email: str
usuario = Usuario (nome="João", idade=54, email="joao@exemplo.com")
print (usuario.nome)
print (usuario.idade)
print (usuario.email)