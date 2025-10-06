from dataclasses import dataclass, asdict

@dataclass
class Usuario:
    nombre: str
    email: str

    def como_tupla(self):
        """
        Devuelve los atributos como una tupla: (nombre, email)
        """
        return (self.nombre, self.email)

    def como_dict(self):
        """
        Devuelve los atributos como un diccionario: {'nombre': ..., 'email': ...}
        """
        return asdict(self)

usuario = Usuario(nombre="Miguel", email="miguel@example.com")

print(usuario.como_tupla())  # ('Miguel', 'miguel@example.com')
print(usuario.como_dict())   # {'nombre': 'Miguel', 'email': 'miguel@example.com'}
