class Pares:
    """
    Iterable que genera números pares desde 0 hasta 10 (exclusivo).
    """
    def __iter__(self):
        return IteradorDePares(10)


class IteradorDePares:
    """
    Iterador que recorre solo los números pares hasta el límite dado.
    """
    def __init__(self, limite):
        self.limite = limite
        self.actual = 0

    def __next__(self):
        if self.actual > self.limite:
            raise StopIteration
        par = self.actual
        self.actual += 2
        return par
    
for numero in Pares():
    print(numero)
