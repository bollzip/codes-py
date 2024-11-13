def valida_email(email):
    arroba_encontrado = False
    ponto_encontrado = False
    tem_caracteres_antes_do_arroba = False
    tem_caracteres_apos_o_arroba = False
    
    for i, char in enumerate(email):
        if char == '@':
            if arroba_encontrado:  
                return False
            arroba_encontrado = True
            tem_caracteres_antes_do_arroba = i > 0
        if char == '.':
            if arroba_encontrado: 
                ponto_encontrado = True
            tem_caracteres_apos_o_arroba = arroba_encontrado and i < len(email) - 1
        
    if arroba_encontrado and ponto_encontrado and tem_caracteres_antes_do_arroba and tem_caracteres_apos_o_arroba:
        return True
    return False

email = "exemplo@dominio.com"
print({valida_email(email)})