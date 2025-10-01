from apuntes import *
from pytest import fixture
from abc import ABC, abstractmethod

def test_circuito():
    ventilador = Ventilador()
    mi_circuito = Circuito(ventilador)

    assert mi_circuito.aparato.on_off is False

    mi_circuito.click()
    assert mi_circuito.aparato.on_off is True

    mi_circuito.click()
    assert mi_circuito.aparato.on_off is False

def test_cambio_aparato():
    ventilador = Ventilador()
    mi_circuito = Circuito(ventilador)
    mi_circuito.click()  # Encendemos
    assert mi_circuito.aparato.on_off is True
    bombilla = Bombilla()
    mi_circuito.aparato = bombilla
    mi_circuito.click()  # Encendemos
    assert mi_circuito.aparato.on_off is True

def test_cambio_nuevo_aparato():
    class MandoTele(AparatoEncendible):
        pass

    mando = MandoTele()
    mi_circuito = Circuito(mando)
    assert mi_circuito.aparato.on_off is False
    mi_circuito.click()
    assert mi_circuito.aparato.on_off is True

# Hay que completar un poco este test!

paciente = Paciente()
medico = Medico()
terapia = Terapia()

def test_paciente():
    assert paciente.nombre == "Juan"



class Medico:
    def __init__(self, nombre, terapia: Terapia):
        self.nombre = nombre
        self.terapia = terapia
    
    def asignar_terapia(self, nueva_terapia: Terapia):
        self.terapia = nueva_terapia
    
    def tratar_paciente(self, paciente: Paciente):
        if self.terapia:
            return f"Dr. {self.nombre} trata a {paciente.nombre}: {self.terapia.administrar()}"
        return "No hay terapia asignada"
 

 # ---

import pytest
from apuntes import Terapia, Pastillas, Fisioterapia, Paciente, Medico

class TestSistemaMedico:
    def test_paciente_creacion(self):
        paciente = Paciente("Alberto")
        assert paciente.nombre == "Alberto"
    
    def test_medico_creacion(self):
        medico = Medico("Manolo")
        assert medico.nombre == "Manolo"
        assert medico.terapia is None
    
    def test_terapia_pastillas(self):
        terapia = Pastillas()
        assert terapia.administrar() == "Tomar pastillas"
    
    def test_terapia_fisioterapia(self):
        terapia = Fisioterapia()
        assert terapia.administrar() == "Hacer ejercicios"
    
    def test_medico_asignar_terapia(self):
        medico = Medico("Manolo")
        terapia = Pastillas()
        
        medico.asignar_terapia(terapia)
        assert medico.terapia == terapia
    
    def test_medico_tratar_paciente_con_terapia(self):
        medico = Medico("Manolo")
        paciente = Paciente("Alberto")
        terapia = Pastillas()
        
        medico.asignar_terapia(terapia)
        resultado = medico.tratar_paciente(paciente)
        
        assert resultado == "Dr. Manolo trata a Alberto: Tomar pastillas"
    
    def test_medico_tratar_paciente_sin_terapia(self):
        medico = Medico("Manolo")
        paciente = Paciente("Alberto")
        
        resultado = medico.tratar_paciente(paciente)
        assert resultado == "No hay terapia asignada"
    
    def test_cambio_terapia_facil(self):
        medico = Medico("Manolo")
        paciente = Paciente("Alberto")
        
        medico.asignar_terapia(Pastillas())
        resultado1 = medico.tratar_paciente(paciente)
        assert "Tomar pastillas" in resultado1
        
        medico.asignar_terapia(Fisioterapia())
        resultado2 = medico.tratar_paciente(paciente)
        assert "Hacer ejercicios" in resultado2
 


@pytest.fixture
def paciente():
    """Crea un paciente de prueba llamado Miguel."""
    return Paciente("Miguel")

@pytest.fixture
def medico_farmaco():
    """Crea un médico con terapia farmacológica."""
    return Medico(MedicinaFarmacologica())

@pytest.fixture
def medico_fisico():
    """Crea un médico con terapia física."""
    return Medico(MedicinaFisica())

def test_terapia_farmacologica(paciente, medico_farmaco):
    """Verifica que el médico aplica medicina farmacológica correctamente."""
    resultado = medico_farmaco.tratar(paciente)
    assert resultado == "Miguel recibió medicina farmacológica"
    assert paciente.historial[-1] == resultado

def test_terapia_fisica(paciente, medico_fisico):
    """Verifica que el médico aplica medicina física correctamente."""
    resultado = medico_fisico.tratar(paciente)
    assert resultado == "Miguel recibió medicina física"
    assert paciente.historial[-1] == resultado

def test_cambio_de_terapia(paciente, medico_farmaco):
    """Verifica que el médico puede cambiar de terapia a medicina tradicional."""
    medico_farmaco.cambiar_terapia(MedicinaTradicional())
    resultado = medico_farmaco.tratar(paciente)
    assert resultado == "Miguel recibió medicina tradicional"
    assert paciente.historial[-1] == resultado

def test_historial_multiple(paciente):
    """Verifica que el historial del paciente almacena múltiples terapias."""
    medico = Medico(MedicinaFarmacologica())
    medico.tratar(paciente)
    medico.cambiar_terapia(MedicinaFisica())
    medico.tratar(paciente)
    assert len(paciente.historial) == 2
    assert paciente.historial[0] == "Miguel recibió medicina farmacológica"
    assert paciente.historial[1] == "Miguel recibió medicina física"
 
