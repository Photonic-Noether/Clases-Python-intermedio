class Bombilla:
    def __init__(self):
        self.on_off = False  # Empieza apagada

class Circuito:
    def __init__(self):
        self.bombilla = Bombilla()

    def encender(self):
        pass  # Enciende la bombilla

    def apagar(self):
        pass  # Apaga la bombilla