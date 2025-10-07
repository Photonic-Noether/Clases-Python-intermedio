from abc import ABC, abstractmethod


# Clase base abstracta
class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        ...

# Estrategias concretas
class Push(Notificacion):
    def enviar(self, mensaje: str):
        print("Enviando por Push:", mensaje)

class SMS(Notificacion):
    def enviar(self, mensaje: str):
        print("Enviando por SMS:", mensaje)

class Email(Notificacion):
    def enviar(self, mensaje: str):
        print("Enviando por Email:", mensaje)

class WhatsApp(Notificacion):
    def enviar(self, mensaje: str):
        print("Enviando por WhatsApp:", mensaje)
        
# Fábrica de notificaciones

class FabricaNotificaciones:
    def __init__(self):
        self._estrategias = {
            "push": Push,
            "sms": SMS,
            "email": Email,
            "whatsapp": WhatsApp
        }

    def crear(self, metodo: str) -> Notificacion:
        try:
            clase = self._estrategias[metodo]
            return clase()
        except KeyError:
            raise ValueError(f"Método desconocido: {metodo}")

# Ejemplo de uso

metodo = "sms"
fabrica = FabricaNotificaciones()
notificador = fabrica.crear(metodo)
notificador.enviar("Hola, esto es una notificacion importante.")
