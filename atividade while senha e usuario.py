while True:
    Usuario = (input("Informe o usuario: "))
    Senha = (input("Informe sua senha: "))
    if Senha != Usuario:
        print ("Concluido")
        break
    elif Usuario == Senha:
        print ("A senha não pode ser igual o usuario")
        continue

