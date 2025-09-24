import pandas as pd

# Cargar datos desde apuntes/clase_1
# df = pd.read_csv("../../apuntes/clase_1/data.csv")
df = pd.read_csv("./apuntes/clase_1/data.csv")     #  correcta


# 1) Número total de personas
print(f" Total de personas: {len(df)}")

# 2) Mostrar los 12 primeros en formato "NOMBRE - OCUPACION"
print("\n Primeros 12 perfiles:")
for _, row in df.head(12).iterrows():
    print(f"{row['nombre']} - {row['ocupacion']}")

# 3) Crear columna is_remote
remotos = ["ingeniero", "desarrollador"]
df["is_remote"] = df["ocupacion"].str.lower().apply(
    lambda x: any(r in x for r in remotos)
)

# Mostrar resumen
print("\n Distribución de 'is_remote':")
print(df["is_remote"].value_counts())


# version Polars

import polars as pl

# Cargar datos desde el CSV
df = pl.read_csv("./apuntes/clase_1/data.csv")

# Mostrar total de personas
print(f"\n Total de personas: {df.shape[0]}\n")

# Mostrar los primeros 12 perfiles
print(" Primeros 12 perfiles:")
for nombre, ocupacion in zip(df["nombre"][:12], df["ocupacion"][:12]):
    print(f"{nombre} - {ocupacion}")

# Crear columna 'is_remote' según ocupación
df = df.with_columns([
    (
        df["ocupacion"]
        .str.to_lowercase()
        .str.contains("ingeniero") |
        df["ocupacion"]
        .str.to_lowercase()
        .str.contains("desarrollador")
    ).alias("is_remote")
])

# Mostrar distribución de 'is_remote'
print("\n Distribución de 'is_remote':")
print(df.select([
    pl.col("is_remote").value_counts()
]))

# 