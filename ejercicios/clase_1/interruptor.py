def encender():
    print("encendido")

def apagar():
    print("apagar")

opcion = int(input("Ingrese 1 para encender, 0 para apagar: "))
if opcion == 1:
    encender()
elif opcion == 0:
    apagar()
else:
    print("opciones validas 1 / 0")
