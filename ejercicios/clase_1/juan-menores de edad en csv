import pandas as pd, pathlib

FILE = pathlib.Path('data.csv')          # cambia si tu archivo está en otra ruta

def hay_menor(ruta=FILE):
    df = pd.read_csv(ruta)
    return (df.edad < 18).any()

if __name__ == '__main__':
    print('¿Hay menores de edad?', 'Sí' if hay_menor() else 'No')