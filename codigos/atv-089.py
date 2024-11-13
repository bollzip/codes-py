def fibonacci_gen(n):
    a, b = 0, 1  
    for i in range(n):
        yield a 
        a, b = b, a + b 
for numero in fibonacci_gen(10):
    print(numero)