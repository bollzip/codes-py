def alterna_maiusculas(texto):
    return ''.join(c.isupper() and c.lower() or c.upper() for c in texto)
print(alterna_maiusculas("cADA UM TEM AQUILO QUE MERECE "))