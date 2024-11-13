def inverte_string(s): 
    string_invertida = s[:: -1]
    result =  string_invertida
    return result
nome=input('escreva: ')
res=inverte_string(nome)
print("Invertido: ",res)