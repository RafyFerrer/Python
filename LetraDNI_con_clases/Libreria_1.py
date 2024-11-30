class DNI:
    numero=0
    letra=''
    matriz='TRWAGMYFPDXBNJZSQVHLCKE'
    # Sobre este patrón, el número de DNI se divide entre 23 y se saca el resto de la división entera
    # Este resto de división entera será entre 0 y 22. Esta es la posición de la matriz la letra correspondiente.

    def set_numero(self,v):
        self.numero=v

    def set_letra(self,v):
        self.letra=v

    def get_numero(self):
        return self.numero

    def get_letra(self):
        return self.letra

    def get_matriz(self):
        return self.matriz

    def __init__(self,n):
        self.set_numero(n)
        posicion=self.get_numero()%23
        letracalculada=self.get_matriz()[posicion]
        self.set_letra(letracalculada)

    