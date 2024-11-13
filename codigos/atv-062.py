import re

def valida_senha(senha):
    if len(senha) < 8 or len(senha) > 16:
        return False
    if not re.search(r'[A-Z]', senha):
        return False
    if not re.search(r'[a-z]', senha):
        return False

    if not re.search(r'[0-9]', senha):
        return False
    if not re.search(r'[\W_]', senha):
        return False

    return True

print(valida_senha("Exemplo@123"))  # Saída esperada: True
print(valida_senha("exemplo123"))   # Saída esperada: False (sem maiúscula e caractere especial)