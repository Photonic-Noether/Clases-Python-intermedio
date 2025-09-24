class Interruptor:
    def __init__(self, encendido = False):
        self.encendido = encendido

    def encender(self):
        self.encendido == True
        return "Encendido"
    
    def apagar(self):
        self.encendido == False
        return "Apagado"

    def alternar(self):
        self.encendido = not self.encendido

if __name__ == "__main__":
    interruptor = Interruptor()
    print(interruptor)
    print(interruptor.encender())
    print(interruptor.apagar())