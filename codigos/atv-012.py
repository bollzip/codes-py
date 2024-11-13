def eh_palindromo (s):
    s=s.replace(" ", "").lower()
    return s == s[::-1]
plv= input("escreva uma palavra: ")
res = (eh_palindromo(plv))
print("É Palindromo?: ",res)