'''
Crear un script que me indique:
 
1) el numero total de personas
2) mostrar el nombre y la ocupacion de los 12 primeros, en este formato (NOMBRE - OCUPACION)
3) programar una forma de crear una nueva columna is_remote y que a los ingenieros y 
desarrolladores se establezca en true, al resto, en false
'''

import pandas

dataframe = pandas.read_csv("data.csv")
print(f"El numero de personas es {len(dataframe)}")

dataframe_parcial = dataframe.head(12)
for i, row in dataframe_parcial.iterrows():
    print(f"{row['nombre']} - {row["ocupacion"]}")

dataframe.loc[(dataframe['ocupacion'] == "Desarrollador") | (dataframe['ocupacion'] == "Ingeniero"), 'is_remote'] = 'True'
dataframe.loc[(dataframe['ocupacion'] != "Desarrollador") & (dataframe['ocupacion'] != "Ingeniero"), 'is_remote'] = 'False'
print(dataframe)

