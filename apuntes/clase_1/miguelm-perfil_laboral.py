from pathlib import Path
import pandas as pd
import polars as pl

# Ruta al archivo CSV como objeto Path
ruta_csv = Path("./apuntes/clase_1/data.csv")

# --- Versión Pandas ---
df_pd = pd.read_csv(ruta_csv)

# 1) Número total de personas
print(f" Total de personas: {len(df_pd)}")

# 2) Mostrar los 12 primeros en formato "NOMBRE - OCUPACION"
print("\n Primeros 12 perfiles:")
for _, row in df_pd.head(12).iterrows():
    print(f"{row['nombre']} - {row['ocupacion']}")

# 3) Crear columna is_remote usando .str.lower().isin()
remotos = ["ingeniero", "desarrollador"]
df_pd["is_remote"] = df_pd["ocupacion"].str.lower().isin(remotos)

# Mostrar resumen
print("\n Distribución de 'is_remote':")
print(df_pd["is_remote"].value_counts())

# --- Versión Polars ---
df_pl = pl.read_csv(ruta_csv)

# Mostrar total de personas
print(f"\n Total de personas: {df_pl.shape[0]}\n")

# Mostrar los primeros 12 perfiles
print(" Primeros 12 perfiles:")
for nombre, ocupacion in zip(df_pl["nombre"][:12], df_pl["ocupacion"][:12]):
    print(f"{nombre} - {ocupacion}")

# Crear columna 'is_remote' según ocupación
df_pl = df_pl.with_columns([
    df_pl["ocupacion"]
    .str.to_lowercase()
    .is_in(remotos)
    .alias("is_remote")
])

# Mostrar distribución de 'is_remote'
print("\n Distribución de 'is_remote':")
print(df_pl.select([
    pl.col("is_remote").value_counts()
]))

# 