class Interruptor:
    def __init__(self):
        self.encendido = False

    def alternar(self):
        self.encendido = not self.encendido
        print("ON" if self.encendido else "OFF")


sw = Interruptor()

while True:
    comando = input("Pulsa Enter para alternar o escribe 'salir': ")
    if comando.lower() == "salir":
        break
    sw.alternar()