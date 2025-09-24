import pandas

df = pandas.read_csv("clase.csv")

print(f"El tamaño total es de {len(df)}")

df_parcial = df.head(12)
for i, row in df_parcial.iterrows():
    print(f"{row['nombre']} - {row['ocupacion']}")

#forma de crear nueva columna
