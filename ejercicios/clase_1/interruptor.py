class Interruptor():
    def __init__(self,apagado=True):
        self.apagado = False if apagado == True else False
    def estado(self):
        if self.apagado:
            print("ON")
        else: 
            print("OFF")
    
    def conmutar(self):
        NuevoeEstado = not self.apagado
        print("nuevo Estado: ", NuevoeEstado)
        self.apagado = True if NuevoeEstado else False




print("prueba interruptor Fernando martinez")
interr = Interruptor(True) #inicio variable con Interruptor apagado
interr.estado()
print("Enciendo")
interr.conmutar()
interr.estado()
print("vuelvo a darle (Apago)")
interr.conmutar()
interr.estado()


