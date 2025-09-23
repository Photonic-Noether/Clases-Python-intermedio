class Interruptor:
    def __init__(self):
        self.estado = False

    def encender(self):
        self.estado = True
        print("El interruptor esta encendido")

    def apagar(self):
        self.estado = False
        print("El interruptor esta apagado")
        
    def mostrar_estado(self):
        return "ENCENDIDO" if self.estado else "APAGADO"



interruptor1 = Interruptor()

print(interruptor1.mostrar_estado())