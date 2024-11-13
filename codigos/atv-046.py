def inverte_string_recursiva(lista):
    if not lista:
        return ''
    a, *b = lista[::-1]
    return a + inverte_string_recursiva(b[::-1])

    

print(inverte_string_recursiva('bolacha'))  