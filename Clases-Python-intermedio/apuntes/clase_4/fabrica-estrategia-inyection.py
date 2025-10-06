from abc import ABC

class Persona(ABC):
    def __init__(self, nombre: str):
        self.nombre = nombre

class Desarrollador(Persona):
    def desarrollar(self):
        print(f"Soy {self.nombre} y me dedico a desarrollar")

class Medico(Persona):
    def curar(self):
        print(f"Soy {self.nombre} y me dedico a curar")

class Profesor(Persona):
    def educar(self):
        print(f"Soy {self.nombre} y me dedico a enseñar Python!")

class FabricaConEstrategia:
    def __init__(self):
        self._estrategias = {
            "dev": Desarrollador,
            "doc": Medico,
            "teacher": Profesor
        }

    def crear(self, tipo: str, nombre: str) -> Persona:
        try:
            clase = self._estrategias[tipo]
            return clase(nombre)
        except KeyError:
            raise ValueError(f"Tipo desconocido: {tipo}")

# *******************

class FabricaConInyeccion:
    def __init__(self, clase_persona):
        self.clase_persona = clase_persona

    def crear(self, nombre: str) -> Persona:
        return self.clase_persona(nombre)

# **** Ejemplo de uso ****

# Usando estrategia
estrategia = FabricaConEstrategia()
joa = estrategia.crear("doc", "Joaquin")
alberto = estrategia.crear("dev", "Alberto")

print(joa, joa.nombre)
print(alberto, alberto.nombre)

# Usando inyección
inyeccion = FabricaConInyeccion(Profesor)
ana = inyeccion.crear("Ana")

print(ana, ana.nombre)
