import Libreria_1
a=input ("Introduce un número de DNI")
miDNI=Libreria_1.DNI(int(a))
print("El resultado es: "+str(miDNI.get_numero())+miDNI.get_letra())