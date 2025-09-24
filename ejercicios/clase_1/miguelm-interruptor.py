class Interruptor:
    """Representa un interruptor con estado encendido o apagado."""

    def __init__(self):
        """Inicializa el interruptor en estado apagado."""
        self.encendido = False

    def encender(self):
        """Activa el interruptor."""
        self.encendido = True

    def apagar(self):
        """Desactiva el interruptor."""
        self.encendido = False

    def estado(self):
        """Devuelve el estado actual como texto."""
        return "Encendido" if self.encendido else "Apagado"

# Ejemplo de uso
interruptor = Interruptor()
print(interruptor.estado())  # Apagado
interruptor.encender()
print(interruptor.estado())  # Encendido
interruptor.apagar()
print(interruptor.estado())  # Apagado
