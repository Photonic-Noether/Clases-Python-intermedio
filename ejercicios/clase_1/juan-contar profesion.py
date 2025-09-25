df = pandas.read_csv("data.csv")
print(f"El tamaño total es de: {len(df)}")
for i, row in df_parcial.iterrows():
    print(f"{row['nombre']} - {row['ocupacion']}")