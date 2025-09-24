class Interruptor:

    def __init__ (self):
        self.status = False

    def encender(self):
        if not self.estado: 
            self.estado = True
            print("Encendido")
        else:
            print("Ya estaba encendido")
    
    def apagar(self):
        if self.estado: 
            self.estado = False
            print("Está apagado")
        else:
            print("Ya estaba apagado")

    def estado (self):
        return self.status
    
    def info (self):
        if self.status:
            print("El interruptor está encendido")
        else:
            print("El interruptor está apagado")
