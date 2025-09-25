import abc   # abstract base class

class InterfazPersona(abc.ABC):
    def __init__(self):
        self.nombre = ...
        self.edad = ...

    @abc.abstractmethod
    def comer():
        pass

class Persona(InterfazPersona):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print("Estoy comiendo")

inst = Persona("Bob", 30)
print(inst.nombre)