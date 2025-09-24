"""
crear un script que me indique:
1) el numero total de personas
2) mostrar el nombre y la ocupacion de los 12 primeros, en este formato (NOMBRE - OCUPACION)
3) programar una forma de crear una nueva columna is_remote y que a los ingenieros у desarrolladores se establezca en true, al resto, en false


cd 'apuntes/clase_2'
uv run 'javier_perez - pandas.py'
"""


import pandas


dataframe = pandas.read_csv('data.csv')

assert len(dataframe) == 80, 'El número total de personas es distinto de 80'

print(f'1) el numero total de personas: {len(dataframe)}')
print()

print('2) mostrar el nombre y la ocupacion de los 12 primeros, en este formato (NOMBRE - OCUPACION)')
for i in range(0, 12):
    print(f"{dataframe.iloc[i]['nombre']} - {dataframe.iloc[i]['ocupacion']}")
print()    

print('3) programar una forma de crear una nueva columna is_remote y que a los ingenieros у desarrolladores se establezca en true, al resto, en false')
lista_is_remote = []
for i in range(0 , len(dataframe)):
    if dataframe.iloc[i]['ocupacion'] == 'Ingeniero' or dataframe.iloc[i]['ocupacion'] == 'Desarrollador':
        lista_is_remote.append('true')
    else:
        lista_is_remote.append('false')
dataframe['is_remote'] = lista_is_remote
print(dataframe)
print()    
