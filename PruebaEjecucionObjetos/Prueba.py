class terreno:

# propiedades

    ancho=0
    alto=0

# setes y getes de las propiedades

    def set_ancho(self,v):
        self.ancho=v
    def set_alto(self,v):
        self.alto=v
    def get_ancho(self):
        return self.ancho
    def get_alto(self):
        return self.alto

# Método constructor

    def __init__(self,a,b):
        self.set_alto(a)
        self.set_ancho(b)


class cazador:

#propiedades

    posicionx=0
    posiciony=0
    lanzas=0

# Setes y Getes de las propiedades

    def set_posicionx(self,v):
        self.posicionx=v
    def set_posiciony(self,v):
        self.posiciony=v
    def set_lanzas(self,v):
        self.lanzas=v
    def get_posicionx(self):
        return self.posicionx
    def get_posiciony(self):
        return self.posiciony
    def get_lanzas(self):
        return self.lanzas

#Métodos restantes. Aquí iría el constructor, pero no hay en esta clase.


    def avanzarx(self,espacio):
        limitex=espacio.get_ancho()
        posicionactualx=self.get_posicionx()
        avancex=posicionactualx+10
        if avancex>limitex:
            avancex=limitex
        self.set_posicionx(avancex)

    def avanzary(self, espacio):
        limitey = espacio.get_alto()
        posicionactualy = self.get_posiciony()
        avancey = posicionactualy + 10
        if avancey > limitey:
            avancey = limitey
        self.set_posiciony(avancey)

