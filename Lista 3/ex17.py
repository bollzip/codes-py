
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatar_data(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano}"


data1 = Data(22, 11, 2024)


print(data1.formatar_data())
