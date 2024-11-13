def conta_maiusculas(texto):
    count = 0
    for char in texto:
        if char.isupper():
            count += 1
    return count
texto = "Capivara Selvagem"
print(conta_maiusculas(texto))  