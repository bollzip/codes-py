def potencia_recursiva(base, expoente):
    if(expoente == 0 ):
        return 1
    else:
        return base * potencia_recursiva(base, expoente-1)
print(potencia_recursiva(3,2))