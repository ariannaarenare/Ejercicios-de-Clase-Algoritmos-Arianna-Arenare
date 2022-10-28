from vehiculoclase import Vehiculo_1

class Bicicleta (Vehiculo_1):
    def __init__ (self, color, ruedas, tipo):
        super.__init__ (color, ruedas)
        self.tipo = tipo

class Motocicleta (Bicicleta):
    def __init__ (self, color, ruedas, tipo, velocidad, cc):
        super.__init__ (color, ruedas, tipo)
        self.velocidad = velocidad
        self.cc = cc
