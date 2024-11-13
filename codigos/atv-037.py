def eh_armstrong(n):
    lista = []
    size = len(str(n))
    case = str(n)
    for i in range(0, size):
        lista.append(int(case[i])**size) 
    if sum(lista) == n:
        return 'é um número de armstrong'
    else:
        return 'não é um número de armstrong'
print(eh_armstrong(1634))