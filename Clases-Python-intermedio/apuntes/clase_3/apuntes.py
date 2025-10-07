# Mixin

from datetime import datetime
from abc import ABC, abstractmethod
import pytest

FILE = "logs.txt"

class LogsMixin:
    def entrar(self):
        self.is_in = True
        self._log("ENTRAR")
        return f"{self.username} ha entrado al sistema"
    
    def salir(self):
        self.is_in = False
        self._log("SALIR")
        return f"{self.username} ha salido del sistema"
    
    def _log(self, action: str):
        timestamp = datetime.now()  # Que dia-mes-año-hora es AHORA
        with open(FILE, "a") as f:  # Añado a un archivo
            f.write(f"{timestamp} - {self.username} {action}\n")

class Usuario(ABC):
    def __init__(self, username: str):
        self.username = username

    @abstractmethod
    def trabajar():
        ...

class UsuarioSeguro(Usuario):
    def trabajar(self):
        print(f"{self.username} esta trabajando")

class UsuarioInseguro(Usuario, LogsMixin):
    def __init__(self, username):
        super().__init__(username)
        self.is_in = False

    def trabajar(self):
        if self.is_in:
            print(f"{self.username} esta trabajando")
        else:
            print("Debes entrar primero para trabajar")


# Property

class Drone:
    def __init__(self):
        self._bateria = 100

    @property
    def bateria(self):
        return self._bateria
 
    @bateria.setter
    def bateria(self, valor):
        if 0 <= valor <= 100:
            self._bateria = valor
        elif valor < 0:
            self._bateria = 0
        elif valor > 100:
            self._bateria = 100
        else:
            raise TypeError("This kind of batery is very strange!")
 
    @bateria.deleter
    def bateria(self):
        print("Batería reiniciada del dron.")
        self._bateria = 0


# Test
drone_test = Drone()  # Esta es mi "fixture"

def test_bateria_drone():
    assert drone_test.bateria >= 0
    assert drone_test.bateria <= 100  # Mi bateria deberia estar entre 0 y 100

def test_bateria_drone_sobreescribiendo():
    drone_test.bateria = 120  # Bateria de mas de 100 la deja cargada totalmente
    assert drone_test.bateria == 100
    drone_test.bateria = -10  # Bateria de menos de 0 la deja descargada totalmente
    assert drone_test.bateria == 0

def test_bateria_drone_eliminar():
    del drone_test.bateria  # Si elimino la bateria se queda descargada
    assert drone_test.bateria == 0



class Battery:
    def __init__(self):
        self.estado = 0

    def cargarBateria(self):
        return self.estado == 100

class Drone:  # 3 principio - Sustitucion de Liskov
    def __init__(self, bateria: Battery):
        self.bateria = bateria

    def volar(self):
        if self.bateria > 0:
            print(f"El dron esta volando con {self.bateria} de bateria")
        else:
            print("Hay que cargar la bateria")