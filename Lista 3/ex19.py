class ConversorMoeda:
    def __init__(self, taxa_conversao):
     
        self.taxa_conversao = taxa_conversao

    def converter_dolares_para_reais(self, dolares):
       
        reais = dolares * self.taxa_conversao
        return reais


conversor = ConversorMoeda(taxa_conversao=5.30)


dolares = 100
reais = conversor.converter_dolares_para_reais(dolares)

print(f"{dolares} dólares são equivalentes a {reais} reais.")
