import random
import string

def generar_lista_numeros(cantidad=10, minimo=1, maximo=100):
    """
    Genera una lista de números aleatorios.

    Args:
        cantidad (int): Número de elementos.
        minimo (int): Valor mínimo.
        maximo (int): Valor máximo.

    Returns:
        list[int]: Lista de números aleatorios.
    """
    return [random.randint(minimo, maximo) for _ in range(cantidad)]

def generar_nombres_aleatorios(cantidad=10, longitud=5):
    """
    Genera una lista de nombres aleatorios de letras minúsculas.

    Args:
        cantidad (int): Número de nombres.
        longitud (int): Longitud de cada nombre.

    Returns:
        list[str]: Lista de nombres aleatorios.
    """
    return [''.join(random.choices(string.ascii_lowercase, k=longitud)) for _ in range(cantidad)]

def asociar_nombres_a_numeros(nombres, numeros):
    """
    Crea un diccionario que asocia cada nombre con un número.

    Args:
        nombres (list[str]): Lista de nombres.
        numeros (list[int]): Lista de números.

    Returns:
        dict[str, int]: Diccionario nombre → número.
    """
    return {nombre: numero for nombre, numero in zip(nombres, numeros)}


