def quadrados(n):
    for i in range(1, n + 1):  
        yield i ** 2  
for quadrado in quadrados(5):
    print(quadrado)