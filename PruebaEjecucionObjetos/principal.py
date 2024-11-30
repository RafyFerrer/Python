import Prueba
espaciojuego = Prueba.terreno(100,200)
juan=Prueba.cazador()
control=input("introduce letra")
if control=="a":
    juan.avanzarx(espaciojuego)
    print(str(juan.get_posicionx()))

