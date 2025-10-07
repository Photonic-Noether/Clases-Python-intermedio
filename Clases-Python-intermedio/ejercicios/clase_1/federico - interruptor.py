
class Interruptor:
    def __init__(self):
        self.state = False

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False 