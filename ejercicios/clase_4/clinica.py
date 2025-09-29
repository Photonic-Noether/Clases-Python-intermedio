from abc import ABC

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
    def aplicar(self, paciente):
        raise NotImplementedError("Debes implementar el método aplicar")


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
