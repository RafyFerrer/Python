class terreno:
    ancho=0
    alto=0
    def set_alto(self,v):
        self.alto=v
    def set_ancho(self,v):
        self.ancho=v
    def get_alto(self):
        return self.alto
    def get_ancho(self):
        return self.ancho
    def __init__(self,al,an):
        self.set_ancho(an)
        self.set_alto(al)

    class cazador:
        posicionx=0
        posiciony=0
        lanzas=0
        activo=1
        def set_posicionx(self,v):
            self.posicionx=v
        def set_posiciony(self,v):
            self.posiciony=v
        def set_lanzas(self,v):
            self.lanzas=v
        def set_activo(self,v):
            self.activo=v
        def get_posicionx(self):
            return self.posicionx
        def get_posiciony(self):
            return self.posiciony
        def get_lanzas(self):
            return self.lanzas
        def get_activo(self):
            return self.activo
        def __init__(self,px,py,lz,act):
            self.set_posicionx(px)
            self.set_posiciony(py)
            self.set_lanzas(lz)
            self.set_activo(act)
        def avanzarx(self,x,espacio):
            if self.get_activo()==1:
                posicionactual=self.get_posicionx()+x
                if posicionactual>espacio.get_ancho():
                    posicionactual=espacio.get_ancho()
                self.set_posicionx(posicionactual)
        def avanzary(self,y,espacio):
            if self.get_activo()==1:
                posicionactual=self.get_posiciony()+y
                if posicionactual>espacio.get_alto():
                    posicionactual=espacio.get_alto()
                self.set_posiciony(posicionactual)
        def retrocederx(self,x):
            if self.get_activo()==1:
                posicionactual=self.get_posicionx()-x
                if posicionactual<0:
                    posicionactual=0
                self.set_posicionx(posicionactual)
        def retrocedery(self,y):
            if self.get_activo()==1:
                posicionactual=self.get_posiciony()-y
                if posicionactual<0:
                    posicionactual=0
                self.set_posiciony(posicionactual)
        def recargar(self,cantidad):
            if self.get_activo()==1:
                actual=self.get_lanzas()
                self.set_lanzas(actual+cantidad)
        def disparar(self):
            if self.get_activo()==1:
                lanzas=self.get_lanzas()-1
                self.set_lanzas(lanzas)
                if lanzas==0:
                    self.set_activo(0)

