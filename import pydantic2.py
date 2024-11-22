from pydantic import BaseModel
class Usuario (BaseModel):
    nome: str
    idade: int
    sexo: str
usuario = Usuario (nome="Rafael", idade=22, sexo="masculino")
print (usuario.nome)
print (usuario.idade)
print (usuario.sexo)