class Interruptor:
    def __init__(self):
        self.encendido = False

    def pulsar(self):
        if self.encendido:
            self.encendido = False
            self.encender()
        else:
            self.encendido = True
            self.apagar()         

    def encender(self):
        print("Encendido")

    def apagar(self):
        print("Apagado")

i = Interruptor()
i.pulsar()
i.pulsar()
i.pulsar()
i.pulsar()