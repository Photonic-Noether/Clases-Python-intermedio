import pytest

"""
Ejercicio para casa (traer mañana hecho):
 
2 - Crear un sistema de callback en el que se valide una contraseña (la funcion de validacion sera definida por el administrador!) -._/
"""

CARACTERES_ESPECIALES = "!@#$%^&*()_+=-`~[]{}'|;':\",./<>?\\"
# atajo de validar_completo ->  f_validar_completo(contraseña_valida, f_validar_mayusculas, f_validar_caracter_especial, f_validar_longitud)

# Esto es una fixture (para cambiar las contraseñas)
@pytest.fixture 
def contraseña_valida():
    return "dddssddddd/Adddddh"

def test_contraseña(contraseña_valida):
    validador = f_validar_completo(
        f_validar_mayusculas, 
        f_validar_caracter_especial, 
        f_validar_longitud
    )
    assert validar_contraseña(contraseña_valida, validador) is True



# Función principal para validar una contraseña (Usa una funcion callable)

def validar_contraseña(contraseña, funcion: callable): 
    return funcion(contraseña)


# Validaciones tipicas de contraseña:

def f_validar_mayusculas(contraseña):                           # Validar si tiene al menos una mayuscula
    return any(char.isupper() for char in contraseña)

def f_validar_caracter_especial(contraseña):                    # Validar si contiene al menos 1 caracter especial
    special_characters = CARACTERES_ESPECIALES
    return any(char in special_characters for char in contraseña)

def f_validar_longitud(contraseña):                             # Validar si la longitud llega a un minimo de 12 caracteres
    return len(contraseña) >= 12

def f_validar_completo(*validaciones: callable):                # Validar todas las validaciones a la vez
    def validaciones_combi(contraseña):                         # Funcion a la que le pasas una contraseña
        for f in validaciones:                                  # Para la funcion de validaciones
            if not f(contraseña):                               # Si es False, devuelve False
                return False
        return True                                             # Si ninguna funcion es falsa, devuelve True
    return validaciones_combi



# Validaciones hechas con lambda

validar_mayusculas = lambda contr: any(char.isupper() for char in contr )
validar_caracter_especial = lambda contr: any(char in CARACTERES_ESPECIALES for char in contr)
validar_longitud = lambda contr: len(contr) >= 12