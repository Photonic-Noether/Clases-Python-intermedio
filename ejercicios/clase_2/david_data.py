"""
En el archivo data.csv tenemos diferentes datos.

📌 Ejercicio:

1) Obtener el número total de personas.
2) Mostrar el nombre y la ocupación de las 12 primeras personas,
   en el siguiente formato: NOMBRE - OCUPACION
3) Crear una nueva columna llamada 'is_remote':
   - Para ingenieros y desarrolladores → True
   - Para el resto → False
"""

import pandas

class DBdatos:
    def __init__(self, csv_file):
        self.pandas = pandas.read_csv(csv_file)

    def total_personas(self):
        return len(self.pandas)

    def mostrar_12(self, n=12):
        print(f"\nPrimeros {n} registros (NOMBRE - OCUPACION):")
        for _, row in self.pandas.head(n).iterrows():
            print(f"{row['nombre']} - {row['ocupacion']}")


datos = DBdatos("../../apuntes/clase_1/data.csv")

print("Número total de personas:", datos.total_personas())

datos.mostrar_12(12)
