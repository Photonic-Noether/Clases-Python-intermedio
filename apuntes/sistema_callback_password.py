def validate_password(password: str, validator_function: callable) -> bool:
    """
    Aplica una función de validación sobre la contraseña.

    Args:
        password (str): La contraseña a validar.
        validator_function (callable): Función que recibe un string y devuelve True o False.

    Returns:
        bool: True si la contraseña pasa la validación, False en caso contrario.
    """
    return validator_function(password)


# 🔐 Validadores definidos por el administrador (usando lambdas)

# Validador: mínimo 8 caracteres
validator_min_length = lambda password: len(password) >= 8

# Validador: al menos una letra mayúscula
validator_has_uppercase = lambda password: any(char.isupper() for char in password)

# Validador: al menos un número
validator_has_digit = lambda password: any(char.isdigit() for char in password)

# Validador: sin espacios
validator_no_spaces = lambda password: " " not in password

# Validador compuesto: todos los anteriores
validator_strong_password = lambda password: (
    validator_min_length(password) and
    validator_has_uppercase(password) and
    validator_has_digit(password) and
    validator_no_spaces(password)
)


#  Ejemplo de uso
if __name__ == "__main__":
    sample_password = "ClaveSegura2025"
    is_valid = validate_password(sample_password, validator_strong_password)
    print(f"¿el password introducido '{sample_password}' es valido?: - {is_valid}")
