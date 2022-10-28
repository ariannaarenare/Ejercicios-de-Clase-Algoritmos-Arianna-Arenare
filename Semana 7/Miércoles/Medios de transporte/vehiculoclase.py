class Vehiculo_1:
    def __init__ (self, color, ruedas):
        self.color = color
        self.ruedas= ruedas
        
        
class Coche (Vehiculo_1):
    def __init__ (self, color, ruedas, velocidad, cc):
        Vehiculo_1.__init__ (color, ruedas)
        self.velocidad = velocidad
        self.cc = cc

class Camioneta (Coche):
    def __init__ (self, color, ruedas, velocidad, cc, carga):
        super.__init__ (color, ruedas, velocidad, cc)
        self.carga = carga

#super hace referencia a la clase superior, se puede acceder a a tributos o métodos

class Bicicleta (Vehiculo_1):
    def __init__ (self, color, ruedas, tipo):
        super.__init__ (color, ruedas)
        self.tipo = tipo

class Motocicleta (Bicicleta):
    def __init__ (self, color, ruedas, tipo, velocidad, cc):
        super.__init__ (color, ruedas, tipo)
        self.velocidad = velocidad
        self.cc = cc
