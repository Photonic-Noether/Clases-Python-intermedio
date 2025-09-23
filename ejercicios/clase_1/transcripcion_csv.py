# crear un script que me indique:

# 1) el numero total de personas

# 2) mostrar el nombre y la ocupacion de los 12 primeros, en este formato (NOMBRE - OCUPACION)

# 3) programar una forma de crear una nueva columna is_remote y que a los ingenieros y desarrolladores se establezca en true, al resto, en false

import pandas as pd

# # Leer CSV e imprimir el total de lineas
# total = pd.read_csv("../../apuntes/clase_1/data.csv")
# print(len(total))

# # Leer el CSV e imprimir las 12 primeras columnas de nombre y ocupacion
# datos_12 = pd.read_csv("../../apuntes/clase_1/data.csv", usecols=["nombre", "ocupacion"])
# print(datos_12.head(12))

# # Pasar todos los datos de 'datos_12' a mayuscula. La funcion 'map' actua elemento por elemento
# datos_mayus = datos_12.map(lambda x: str(x).upper())

# # Selecciona las columnas y las pasa a mayusculas
# datos_mayus.columns = datos_mayus.columns.str.upper()

# # Pasar el 'datos_12' a un nuevo CSV donde esté separado por guion y no muestre el index
# datos_mayus.to_csv("data_con_guion.csv",sep="-", index=False)

# # Leer el nuevo CSV e imprimir los datos con guion
# datos_guion = pd.read_csv("./data_con_guion.csv")
# print(datos_guion)

data = pd.read_csv("../../apuntes/clase_1/data.csv")
data["is_remote"] = data["ocupacion"].str.lower().apply(lambda x: "desarrollador" in x or "ingeniero" in x)
data.to_csv("column_is_remote.csv", index=False)

datos = pd.read_csv("./column_is_remote.csv")
print(datos)

#print(data[["nombre", "ocupacion", "is_remote"]])