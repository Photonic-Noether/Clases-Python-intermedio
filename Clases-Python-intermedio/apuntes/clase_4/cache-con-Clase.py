from time import sleep

class Cache:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        resultado = self.func(*args)
        self.cache[args] = resultado
        return resultado

@Cache
def sumar(a, b):
    sleep(2)
    return a + b

print("Empiezo a calcular!")
print(sumar(10, 20))
print(sumar(10, 20))
print(sumar(10, 20))
print(sumar(10, 20))
print(sumar(10, 20))
print(sumar(5, 15))
print(sumar(5, 15))





