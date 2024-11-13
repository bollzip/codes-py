def encontra_palavra(texto,palavra):
    texto =texto.lower()
    palavra = palavra.lower()
    palavras=texto.split()

    try:
        indice=palavras.index(palavra)
        return indice
    except ValueError:
        return -1
print(encontra_palavra('ensinando esses manos viver uma vida gangsta','uma'))