class Interruptor:
    def __init__(self):
        self.estado = False

    def encender(self):
        self.estado = True

    def apagar(self):
        self.estado = False

    def mostrar_estado(self):
        return "ENCENDIDO" if self.estado else "APAGADO"
    
miInterruptor = Interruptor()

miInterruptor.encender()
print(miInterruptor.mostrar_estado())