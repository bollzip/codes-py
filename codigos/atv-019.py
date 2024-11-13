def apaga_vogais(s):
    vogais= 'aeiouAEIOU'
    return ''.join([c for c in s if c not in vogais])
print(apaga_vogais("juro que amanhã não é ontem"))