def conta_ocorrencias_caracteres(s):
    contagem = {}
    for char in s:
        if char in contagem:
            contagem[char] += 1
        else:
            contagem[char] = 1
    return contagem
s = "banana"
print(conta_ocorrencias_caracteres(s)) 