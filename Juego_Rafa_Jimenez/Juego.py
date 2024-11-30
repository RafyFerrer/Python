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
    def __init__(self,an,alt):
        self.set_ancho(an)
        self.set_alto(alt)

class manzana:
    posicionx=0
    posiciony=0

    def set_posicionx(self,x):
        self.posicionx=x
    def set_posiciony(self,y):
        self.posiciony=y
    def get_posicionx(self):
        return self.posicionx
    def get_posiciony(self):
        return self.posiciony
    def __init__(self,anm,alm):
        self.set_posicionx(anm)
        self.set_posiciony(alm)

class serpiente:
    posicionx=0
    posiciony=0
    vivo=1
    longitud=0

    def set_vivo(self,v):
        self.vivo=v
    def set_longitud(self,l):
        self.longitud=l
    def set_posicionx(self,x):
        self.posicionx=x
    def set_posiciony(self,y):
        self.posiciony=y

    def get_vivo(self):
        return self.vivo
    def get_longitud(self):
        return self.longitud
    def get_posicionx(self):
        return self.posicionx
    def get_posiciony(self):
        return self.posiciony

    def izquierda(self,x):
        posicion=self.get_posicionx()-x
        if posicion<=0:
            self.set_vivo(0)
        self.set_posicionx(posicion)
    def abajo(self,y):
        posicion=self.get_posiciony()-y
        if posicion<=0:
            self.set_vivo(0)
        self.set_posiciony(posicion)
    def arriba(self,y,espacio):
        posicion=self.get_posiciony()+y
        if posicion >= espacio.get_alto():
            self.set_vivo(0)
        self.set_posiciony(posicion)
    def derecha(self,x,espacio):
        posicion=self.get_posicionx()+x
        if posicion >=espacio.get_ancho():
            self.set_vivo(0)
        self.set_posicionx(posicion)
    def crecer(self,c,manzana):
        if (manzana.get_posicionx() and manzana.get_posiciony())==(self.get_posicionx and self.get_posiciony):
            c=self.get_longitud()+1
        self.set_longitud(c)

    def __init__(self,an,al,lon):
        self.set_posicionx(an)
        self.set_posiciony(al)
        self.set_longitud(lon)