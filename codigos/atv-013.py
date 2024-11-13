def conta_letras(s,letra):
    s =s.lower()
    letra = letra.lower()
    return s.count(letra)
print(conta_letras('é de lei, mes a mes ','e'))