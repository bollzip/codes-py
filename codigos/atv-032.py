import math
def raiz_quadrada(n):
    if n <0:
        raise ValueError('não é possivel calcular a raiz quadrada de um numero negativo ')
    return math.sqrt(n)
numero = 4
print(raiz_quadrada(numero))