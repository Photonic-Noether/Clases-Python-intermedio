from collections import Counter

def contar_letras_nombres_unicos(nombres):
    frecuencia = Counter(nombres)
    return {nombre.lower(): len(nombre) for nombre in nombres if frecuencia[nombre] == 1}
