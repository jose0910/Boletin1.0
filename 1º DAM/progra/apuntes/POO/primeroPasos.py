from progra.Prueba import cadeas


class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #todos lso metodos de clase necesitan estar referenciados sobre ellos mismos
    def toString(self):
        cadeaPunto = "As coordenadas do punto son: \n x = " + str(self.x) + " \n y = " + str(self.y)

        return cadeaPunto
    def __str__(self):
        return self.toString()