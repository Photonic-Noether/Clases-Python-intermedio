import pytest
from clinica import (
    Paciente,
    Medico,
    MedicinaFarmacologica,
    MedicinaFisica,
    MedicinaTradicional
)

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
