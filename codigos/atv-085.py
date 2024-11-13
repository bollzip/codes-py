def conta_ate_n(n):
    for i in range(0, n + 1):
        yield i

# Exemplo de uso
for numero in conta_ate_n(5):
    print(numero)