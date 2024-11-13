def conta_palavras(texto):
    return len (texto.split())

plv =input('escreva uma palavra: ')
res= (conta_palavras(plv))
print('Total de palavras: ',res)