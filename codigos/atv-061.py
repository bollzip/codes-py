def bubblesort(lista):
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
        if not trocou:
            break
    return lista
lista = [64, 34, 25, 12, 22, 11, 90]
print(bubblesort(lista)) 