import pytest
import random
from compresion_random_list_dict import (
    generar_lista_numeros,
    generar_nombres_aleatorios,
    asociar_nombres_a_numeros
)

@pytest.fixture
def datos_controlados():
    """
    Fixture que genera datos aleatorios reproducibles:
    - Lista de 10 números enteros entre 1 y 100.
    - Lista de 10 nombres aleatorios de 5 letras.
    
    Se utiliza random.seed(42) para garantizar que los datos
    sean siempre los mismos en cada ejecución del test.
    
    Returns:
        tuple: (lista de números, lista de nombres)
    """
    random.seed(42)
    numeros = generar_lista_numeros()
    nombres = generar_nombres_aleatorios()
    return numeros, nombres

def test_asociacion_aleatoria(datos_controlados):
    """
    Test que valida la asociación entre nombres y números:
    - Se genera un diccionario con comprensión usando zip().
    - Se verifica que haya 10 pares clave-valor.
    - Se comprueba que las claves sean cadenas de 5 letras.
    - Se comprueba que los valores sean enteros entre 1 y 100.
    
    Este test garantiza que la lógica de generación y asociación
    cumple con los requisitos esperados.
    """
    numeros, nombres = datos_controlados
    asociaciones = asociar_nombres_a_numeros(nombres, numeros)

    assert len(numeros) == 10
    assert len(nombres) == 10
    assert len(asociaciones) == 10
    assert all(isinstance(k, str) and len(k) == 5 for k in asociaciones.keys())
    assert all(isinstance(v, int) and 1 <= v <= 100 for v in asociaciones.values())

