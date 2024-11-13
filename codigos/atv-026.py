def soma_pares(lista):
    return sum(num for num in lista if num % 2==0)
numeros = [1,2,3,4,5,6,7,8,9,10]
print(soma_pares(numeros))