# crear un script que me indique:

# 1) el numero total de personas

# 2) mostrar el nombre y la ocupacion de los 12 primeros, en este formato (NOMBRE - OCUPACION)

# 3) programar una forma de crear una nueva columna is_remote y que a los ingenieros y desarrolladores se establezca en true, al resto, en false

import pandas as pd

# # Leer CSV e imprimir el total de lineas
df = pd.read_csv("data.csv")
#print(len(df))

df.insert(4, "is_remote", df["ocupacion"].str.lower().apply(lambda x: "desarrollador" in x or "ingeniero" in x))
print(df)

