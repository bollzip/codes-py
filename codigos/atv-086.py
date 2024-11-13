def pares(n):
    for i in range(0, n + 1, 2):  
        yield i
for numero in pares(10):
    print(numero)