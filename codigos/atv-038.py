def media_harmonica(lista):
    denominador = 0
    size = len(lista)
    for i in range(0, size):
        if(lista[i]==0):
            print('sem divisao por zero')
        else:
            denominador += (1/lista[i])
    return size/denominador
lista = [1,2,4]
print(media_harmonica(lista))