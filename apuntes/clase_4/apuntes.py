from abc import ABC

class AparatoEncendible(ABC):
    def __init__(self):
        self.on_off = False

class Bombilla(AparatoEncendible):
    pass

class Ventilador(AparatoEncendible):
    pass

class Circuito:
    def __init__(self, aparato: AparatoEncendible):
        self.aparato = aparato  # Bombilla, ventilador, lavadora

    def click(self):
        self.aparato.on_off = not self.aparato.on_off

# Ejercicio
# Pacientes y Medicos que les administran Terapias

from abc import ABC, abstractmethod

class Terapia(ABC):
    tipo_de_accion: str

    def administrar(self):
        return self.tipo_de_accion

class Pastillas(Terapia):
    def __init__(self):
        self.tipo_de_accion = "Tomar pastillas"

class Fisioterapia(Terapia):
    def __init__(self):
        self.tipo_de_accion = "Dar masaje"

class Paciente:
    def __init__(self, nombre):
        self.nombre = nombre

# --- Otro compañero`

class Paciente:
    """
    Representa a un paciente que puede recibir terapias y almacenar su historial.

    Atributos:
        nombre (str): Nombre del paciente.
        historial (list): Lista de terapias aplicadas.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []

    def recibir_terapia(self, terapia):
        """
        Aplica una terapia al paciente y la registra en el historial.

        Args:
            terapia (Terapia): Instancia de una terapia.

        Returns:
            str: Resultado de la terapia aplicada.
        """
        resultado = terapia.aplicar(self)
        self.historial.append(resultado)
        return resultado

class Terapia(ABC):
    """
    Clase base abstracta para definir terapias.

    Método:
        aplicar(paciente): Debe ser implementado por subclases.
    """
    @abstractmethod
    def aplicar(self, paciente):
        pass

class MedicinaFarmacologica(Terapia):
    """Terapia basada en medicamentos farmacológicos."""
    def aplicar(self, paciente):
        return f"{paciente.nombre} recibió medicina farmacológica"

class MedicinaFisica(Terapia):
    """Terapia basada en ejercicios o tratamientos físicos."""
    def aplicar(self, paciente):
        return f"{paciente.nombre} recibió medicina física"

class MedicinaTradicional(Terapia):
    """Terapia basada en prácticas tradicionales o naturales."""
    def aplicar(self, paciente):
        return f"{paciente.nombre} recibió medicina tradicional"

class Medico:
    """
    Representa a un médico que administra terapias a pacientes.

    Atributos:
        terapia (Terapia): Terapia actual que el médico administra.
    """
    def __init__(self, terapia: Terapia):
        self.terapia = terapia

    def cambiar_terapia(self, nueva_terapia: Terapia):
        """
        Cambia la terapia que el médico administra.

        Args:
            nueva_terapia (Terapia): Nueva terapia a aplicar.
        """
        self.terapia = nueva_terapia

    def tratar(self, paciente: Paciente):
        """
        Aplica la terapia actual al paciente.

        Args:
            paciente (Paciente): Paciente a tratar.

        Returns:
            str: Resultado de la terapia aplicada.
        """
        return paciente.recibir_terapia(self.terapia)

 # ---

from dataclasses import dataclass

@dataclass
class Ciudad:
    nombre:str

@dataclass
class Persona:
    nombre: str
    edad: int
    ciudad: Ciudad
    es_trabajador: bool = False

class Trabajador(Persona):
    def __init__(self, nombre, edad, ciudad, es_trabajador=True, *, trabajo):
        super().__init__(nombre, edad, ciudad, es_trabajador)
        self.trabajo = trabajo

ciudad = Ciudad("Madrid")
trabajador = Trabajador("Jose", 55, ciudad, trabajo="desarrollador")

print(trabajador)