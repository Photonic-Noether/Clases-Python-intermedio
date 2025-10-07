class Desarrollador:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def desarrollar(self):
        print(f"Soy {self.nombre} y me dedico a desarrollar")

class Medico:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def curar(self):
        print(f"Soy {self.nombre} y me dedico a curar")

class Profesor:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def educar(self):
        print(f"Soy {self.nombre} y me dedico a enseñar Python!")

def crear_persona(tipo: str, nombre: str):
    if tipo == "dev":
        return Desarrollador(nombre)
    elif tipo == "doc":
        return Medico(nombre)
    elif tipo == "teacher":
        return Profesor(nombre)
    else:
        raise ValueError(f"Tipo desconocido: {tipo}")

# Ejemplos de uso
joa = crear_persona("doc", "Joaquin")
alberto = crear_persona("dev", "Alberto")

print(joa, joa.nombre)
print(alberto, alberto.nombre)
