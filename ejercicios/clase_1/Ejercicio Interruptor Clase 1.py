class Interruptor:
    
    def __init__(self):
        self.estado = False     #Inicializamos el interruptor en apagado
    
    def encender(self):
        self.estado = True      #definimos una función para que encienda el interruptor

    def apagar(self):
        self.estado = False     #definimos una función para que apague el interruptor.
    
    def mostrar_estado(self):
        if self.estado:
            print("El interruptor está Encendido")
        else:
            print("El interruptor está apagado")

interruptor = Interruptor()

interruptor.mostrar_estado()
interruptor.encender()
interruptor.mostrar_estado()
interruptor.apagar()
interruptor.mostrar_estado()




        