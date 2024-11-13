def ordena_lista(lista):
    for i in range(0,len(lista)):
        for j in range(i, len(lista)):
            if(lista[i]>lista[j]):
                memoria = lista[i]
                lista[i] = lista[j]
                lista[j] = memoria
    return lista
lista = [100,20,4,10,2,1,30,40,100, 199, 150, 120]
print(ordena_lista(lista))