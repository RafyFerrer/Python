class terreno:
    # zona propiedades
    ancho=0
    alto=0
    #zona setes y getes
    def set_ancho(self,v):
        self.ancho=v
    def set_alto(self,v):
        self.alto=v
    def get_ancho(self):
        return self.ancho
    def get_alto(self):
        return self.alto

    #constructor

    def __init__(self,an,al):
        self.set_alto(al)
        self.set_ancho(an)

class raton:
        #zona propiedades

    px=0
    py=0

        #zona setes y getes

    def set_px(self,v):
        self.px=v
    def set_py(self,v):
        self.py=v
    def get_px(self):
        return self.px
    def get_py(self):
        return self.py

        #constructor

    def __init__(self,x,y):
        self.set_px(x)
        self.set_py(y)

        # zona resto de metodos

    def avanzar_x(self,ter,cantidad):
        px_actual=self.get_px()
        px_calculada=px_actual+cantidad
        limite=ter.get_ancho()
        if px_calculada > limite:
            px_calculada=limite
        self.set_px(px_calculada)
    def retroceder_x(self,cantidad):
        px_actual = self.get_px()
        px_calculada = px_actual - cantidad
        if px_calculada < 0:
            px_calculada = 0
        self.set_px(px_calculada)
    def avanzar_y(self,ter,cantidad):
        py_actual = self.get_py()
        py_calculada = py_actual + cantidad
        limite = ter.get_alto()
        if py_calculada > limite:
            py_calculada = limite
        self.set_py(py_calculada)
    def retroceder_y(self,cantidad):
        py_actual = self.get_py()
        py_calculada = py_actual - cantidad
        if py_calculada < 0:
            py_calculada = 0
        self.set_py(py_calculada)

class manzana:
    px=0
    py=0
    activo=0
 #zona setes y getes

    def set_px(self,v):
        self.px=v
    def set_py(self,v):
        self.py=v
    def set_activo(self,v):
        self.activo=v
    def get_px(self):
        return self.px
    def get_py(self):
        return self.py
    def get_activo(self):
        return self.activo

        #constructor

    def __init__(self,x,y,a):
        self.set_px(x)
        self.set_py(y)
        self.set_activo(a)


