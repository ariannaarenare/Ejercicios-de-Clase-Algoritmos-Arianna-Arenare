from vehiculoclase import Vehiculo_1

class Coche (Vehiculo_1):
    def __init__ (self, color, ruedas, velocidad, cc):
        Vehiculo_1.__init__ (color, ruedas)
        self.velocidad = velocidad
        self.cc = cc

class Camioneta (Coche):
    def __init__ (self, color, ruedas, velocidad, cc, carga):
        super.__init__ (color, ruedas, velocidad, cc)
        self.carga = carga