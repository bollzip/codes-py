def fatorial(n):
    if n<0:
        raise ValueError
    elif n==0 or n==1:
        return 1
    else:
        return n * fatorial(n-1)

numero = int(input('escreva: '))
res = fatorial(numero)
print('Fatorial do número: ',res)