
class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def exibir_horario(self):
        return f"{self.hora:02d}:{self.minuto:02d}"


relogio1 = Relogio(15, 45, 30)


print(relogio1.exibir_horario())
