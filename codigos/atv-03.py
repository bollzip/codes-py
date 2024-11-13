def par(x):
    if (x%2)==0:
        return True
    else:
        return False
while True:
    eh_par = int(input('escreva um numero: '))
    if par(eh_par):
        print('é par')
    else:
        print('é impar')