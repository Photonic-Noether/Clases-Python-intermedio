CACHE = {}

def cache(func):
    def wrapper(*args):
        if args in CACHE:
            return CACHE[args]
        resultado = func(*args)
        CACHE[args] = resultado
        return resultado
    return wrapper

@cache
def sumar(n1, n2):
    return n1 + n2

calculo_1 = sumar(10, 20)
calculo_2 = sumar(10, 20)
calculo_3 = sumar(5, 7)


# Diccionario global que actuará como almacenamiento de resultados ya calculados
CACHE = {}

# Definimos el decorador 'cache'
def cache(func):
    # Esta función interna envuelve la original y controla el acceso a la cache
    def wrapper(*args):
        # Verificamos si los argumentos ya están en la cache
        if args in CACHE:
            # Si están, devolvemos el resultado almacenado sin volver a ejecutar la función
            return CACHE[args]
        
        # Si no están, ejecutamos la función original con los argumentos
        resultado = func(*args)
        
        # Guardamos el resultado en la cache usando los argumentos como clave
        CACHE[args] = resultado
        
        # Devolvemos el resultado recién calculado
        return resultado
    
    # Retornamos la función decorada
    return wrapper

# Aplicamos el decorador a la función 'sumar'
@cache
def sumar(n1, n2):
    # Esta función simplemente suma dos números
    return n1 + n2

# Primera llamada: calcula y guarda en cache
calculo_1 = sumar(10, 20)

# Segunda llamada con los mismos argumentos: recupera de cache
calculo_2 = sumar(10, 20)

# Tercera llamada con nuevos argumentos: calcula y guarda
calculo_3 = sumar(5, 7)
