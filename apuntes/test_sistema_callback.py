import pytest
import random
from sistema_callback_password import (
    validate_password,
    validator_min_length,
    validator_has_uppercase,
    validator_has_digit,
    validator_no_spaces,
    validator_strong_password
)

@pytest.fixture
def sample_passwords():
    """
    Fixture que genera contraseñas de prueba reproducibles.
    Usa random.seed para garantizar consistencia en los tests.
    
    Returns:
        dict: Diccionario con contraseñas etiquetadas por tipo.
    """
    random.seed(42)
    return {
        "valida": "ClaveSegura2025",
        "corta": "abc123",
        "sin_mayuscula": "clave2025",
        "sin_numero": "ClaveSegura",
        "con_espacios": "Clave 2025"
    }

def test_validador_min_length(sample_passwords):
    """
    Valida que la contraseña tenga al menos 8 caracteres.
    """
    assert validate_password(sample_passwords["valida"], validator_min_length)
    assert not validate_password(sample_passwords["corta"], validator_min_length)

def test_validador_has_uppercase(sample_passwords):
    """
    Valida que la contraseña contenga al menos una letra mayúscula.
    """
    assert validate_password(sample_passwords["valida"], validator_has_uppercase)
    assert not validate_password(sample_passwords["sin_mayuscula"], validator_has_uppercase)

def test_validador_has_digit(sample_passwords):
    """
    Valida que la contraseña contenga al menos un número.
    """
    assert validate_password(sample_passwords["valida"], validator_has_digit)
    assert not validate_password(sample_passwords["sin_numero"], validator_has_digit)

def test_validador_no_spaces(sample_passwords):
    """
    Valida que la contraseña no contenga espacios.
    """
    assert validate_password(sample_passwords["valida"], validator_no_spaces)
    assert not validate_password(sample_passwords["con_espacios"], validator_no_spaces)

def test_validador_compuesto(sample_passwords):
    """
    Valida que la contraseña cumpla todos los criterios del validador compuesto.
    """
    assert validate_password(sample_passwords["valida"], validator_strong_password)
    assert not validate_password(sample_passwords["corta"], validator_strong_password)
    assert not validate_password(sample_passwords["sin_mayuscula"], validator_strong_password)
    assert not validate_password(sample_passwords["sin_numero"], validator_strong_password)
    assert not validate_password(sample_passwords["con_espacios"], validator_strong_password)
