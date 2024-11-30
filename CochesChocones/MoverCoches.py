class Coche:

    def __init__ (self, x:int, y:int):

        self.x=x
        self.y=y
        self.xchoquedcha = x+10
        self.xchoqueizq = x-10
        self.ychoquearriba = y-10
        self.ychoqueabajo = y+10
        self.reventado = False
    
    def aceleraDcha(self):
        self.x += 30
        self.y += 30
        self.xchoquedcha = self.x + 10
        self.xchoqueizq = self.x - 10
        self.ychoquearriba = self.y - 10
        self.ychoqueabajo = self.y + 10

    
Ferrary = Coche (0,0)
Porche = Coche (100,100)

while Ferrary.reventado == False or Porche.reventado == False:

    tecla = input ("Introduce la tecla")

    if tecla == "p":
        Ferrary.aceleraDcha()
        if Ferrary.xchoquedcha >= Porche.xchoquedcha:
            Ferrary.reventado = True
            Porche.reventado = True
            print ("se acabó el juego has reventado los coches")



