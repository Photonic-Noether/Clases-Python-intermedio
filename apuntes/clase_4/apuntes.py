class Bombilla:
    def __init__(self):
        self.on_off = False  # Empieza apagada

class Circuito:
    def __init__(self):
        self.bombilla = Bombilla()

    def encender(self):
        self.bombilla.on_off = True

    def apagar(self):
        self.bombilla.on_off = False