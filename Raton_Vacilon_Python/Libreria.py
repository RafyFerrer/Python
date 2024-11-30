class terreno:
    ancho=0
    alto=0

    def set_ancho(self,x):
        self.ancho=x
    def set_alto(self,y):
        self.alto=y
    def get_ancho(self):
        return self.ancho
    def get_alto(self):
        return self.alto
    def __init__(self,an,al):
        self.set_ancho(an)
        self.set_alto(al)



class raton:
    posicionx=0
    posiciony=0
    vivo=1
    movimientos=0

    def set_vivo(self,v):
        self.vivo=v
    def set_posicionx(self,x):
        self.posicionx=x
    def set_posiciony(self,y):
        self.posiciony=y
    def set_movimientos(self,m):
        self.movimientos=m

    def get_vivo(self):
        return self.vivo
    def get_posicionx(self):
        return self.posicionx
    def get_posiciony(self):
        return self.posiciony
    def get_movimientos(self):
        return self.movimientos

    def izquierda(self,x):
        posicion=self.get_posicionx()-x
        self.set_posicionx(posicion)
    def abajo(self,y):
        posicion=self.get_posiciony()-y
        self.set_posiciony(posicion)
    def arriba(self,y,espacio):
        posicion=self.get_posiciony()+y
        self.set_posiciony(posicion)
    def derecha(self,x,espacio):
        posicion=self.get_posicionx()+x
        self.set_posicionx(posicion)

    def __init__(self,an,al,mov):
        self.set_posicionx(an)
        self.set_posiciony(al)
        self.set_movimientos(mov)

class manzana:
    posicionx=0
    posiciony=0
    saltos=0

    def set_posicionx(self,x):
        self.posicionx=x
    def set_posiciony(self,y):
        self.posiciony=y
    def get_posicionx(self):
        return self.posicionx
    def get_posiciony(self):
        return self.posiciony
    def set_saltos(self,s):
        self.saltos=s
    def get_saltos(self):
        return self.saltos

    def __init__(self,anm,alm,sal):
        self.set_posicionx(anm)
        self.set_posiciony(alm)
        self.set_saltos(sal)

class barreras:
    posicionx=0
    posiciony=0
    longitud=0

    def set_longitud(self,l):
        self.longitud=l
    def set_posicionx(self,x):
        self.posicionx=x
    def set_posiciony(self,y):
        self.posiciony=y

    def get_longitud(self):
        return self.longitud
    def get_posicionx(self):
        return self.posicionx
    def get_posiciony(self):
        return self.posiciony

    def __init__(self,px,py,lon):
        self.set_posicionx(px)
        self.set_posiciony(py)
        self.set_longitud(lon)

class gato:
    posicionx=0
    posiciony=0

    def set_posicionx(self,x):
        self.set_posicionx(x)
    def set_posiciony(self,y):
        self.set_posiciony(y)

    def get_posicionx(self):
        return self.get_posicionx()
    def get_posiciony(self):
        return self.get_posiciony()

    def __init__(self,x,y):
        self.set_posicionx(x)
        self.set_posiciony(y)