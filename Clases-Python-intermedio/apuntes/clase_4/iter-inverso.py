class ContadorInverso:
    """
    Iterable que genera números desde un límite hacia 0.
    """
    def __init__(self, inicio):
        self.inicio = inicio

    def __iter__(self):
        return IteradorInverso(self.inicio)


class IteradorInverso:
    """
    Iterador que recorre números en orden descendente hasta 0.
    """
    def __init__(self, inicio):
        self.actual = inicio

    def __next__(self):
        if self.actual < 0:
            raise StopIteration
        valor = self.actual
        self.actual -= 1
        return valor

for numero in ContadorInverso(10):
    print(numero)


# Generador con un While
def contador_inverso(inicio):
    """
    Generador que produce números desde 'inicio' hasta 0 (inclusive),
    sin usar la función range.

    Ejemplo:
        contador_inverso(5) → 5, 4, 3, 2, 1, 0
    """
    actual = inicio
    while actual >= 0:
        yield actual
        actual -= 1

for numero in contador_inverso(10):
    print(numero)
