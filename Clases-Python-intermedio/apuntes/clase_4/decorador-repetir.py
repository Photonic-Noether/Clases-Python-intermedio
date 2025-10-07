def repetir(n: int, nombre: str):
    def decorador(func) -> callable:
        def wrapper(*args, **kwargs) -> any:
            resultado: any
            for i in range(1, n + 1):
                print(f"Iteración {i} → Ejecutando '{func.__name__}' por {nombre}")
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorador


@repetir(3, "Miguel")
def saludar() -> str:
    print("Hola desde la función")
    return "Saludo final"



# **** test **

def test_repetir() -> None:
    resultado: str = saludar()
    assert resultado == "Saludo final"
