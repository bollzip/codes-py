def ocorrencias_palavras(texto):
    texto=texto.lower()
    texto=texto.replace(',','').replace('.','').replace('!','').replace('?','')
    palavras = texto.split()
    contagem={}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra]+=1
        else:
            contagem[palavra]=1
    return contagem
resultado=(ocorrencias_palavras('Vamos fumar mato no cachimbo'))
print(resultado)