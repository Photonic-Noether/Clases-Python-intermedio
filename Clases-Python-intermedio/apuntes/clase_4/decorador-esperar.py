import time

# Decorador que espera 'segundos' antes de ejecutar la función
def esperar(segundos: int):
    def decorador(func) -> callable:
        def wrapper(*args, **kwargs) -> any:
            time.sleep(segundos)
            return func(*args, **kwargs)
        return wrapper
    return decorador


@esperar(2)
def saludar() -> str:
    return "Hola después de esperar"

# **** test **

def test_esperar() -> None:
    inicio: float = time.time()
    resultado: str = saludar()
    fin: float = time.time()

    assert resultado == "Hola después de esperar"
    assert fin - inicio >= 2
