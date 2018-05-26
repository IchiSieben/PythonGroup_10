class Reloj:
    def __init__(self, horas, minutos):
        self.horas = horas
        self.minutos = minutos

    def mostrar(self):
        print('{:02d}:{:02d}'.format(self.horas, self.minutos))

    def agregar_minuto(self):
        self.minutos += 1
        if self.minutos > 59:
            self.minutos = 0
            self.agregar_hora()

    def agregar_hora(self):
        self.horas += 1
        if self.horas > 23:
            self.horas = 0


rolex = Reloj(horas=23, minutos=59)
rolex.mostrar() # -> 23:59
rolex.agregar_minuto()
rolex.mostrar() # -> 00:00
rolex.agregar_hora()
rolex.mostrar() # -> 01:00
