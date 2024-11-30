import Libreria
a=input ("Introduce un número de DNI")
miDNI=Libreria.DNI(int(a))
miDNI.calcular()
print("El resultado es: "+str(miDNI.get_numero())+miDNI.get_letra())