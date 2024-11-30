class Coche:
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        self.activo=True
        self.x1=self.x + 10
        self.y1=self.y - 10
        self.x2=self.x + 10
        self.y2=self.y + 10
        self.x3=self.x - 10
        self.y3=self.y + 10
        self.x4=self.x - 10
        self.y4=self.y - 10
    
    def actualizarPerimetroCoche (self):
        self.x1=self.x + 10
        self.y1=self.y - 10
        self.x2=self.x + 10
        self.y2=self.y + 10
        self.x3=self.x - 10
        self.y3=self.y + 10
        self.x4=self.x - 10
        self.y4=self.y - 10
    
    def acelerarDerecha(self):
        self.x = self.x + 1
        self.actualizarPerimetroCoche()
    
    def acelerarIzquierda(self):
        self.x=self.x - 1
        self.actualizarPerimetroCoche()
    
    def acelerarArriba(self):
        self.y=self.y-1
        self.actualizarPerimetroCoche()
    
    def acelerarAbajo(self):
        self.y = self.y + 1
        self.actualizarPerimetroCoche()
    
    def chocarRomper (self):
        self.activo = False
    

# EMPEZAMOS EL PROGRAMA PRINCIPAL

Ferrari = Coche (100,100)
SeatPanda = Coche (150,150)
tecla = input ("pulsa P para mover a derecha, O para mover a la izquierda, q para arriba y a para abajo")

if tecla == "p":
    velocidad = int (input ("Introduce velocidad"))
    for i in range (1,velocidad+1):
        Ferrari.acelerarDerecha()
        # me quedo por comprobar los posibles choques para romper el ferrari







