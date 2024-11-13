def converte_segundos(h, m, s):
    m = m*60
    h = h * 3600
    return h+m+s

print(converte_segundos(2,2,2))