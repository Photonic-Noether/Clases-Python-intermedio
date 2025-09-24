from pathlib import Path
import pandas as pd
import polars as pl

# Ruta al archivo CSV como objeto Path
ruta_csv = Path("./apuntes/clase_1/data.csv")

# Ocupaciones consideradas remotas
remotos = ["ingeniero", "desarrollador"]

# -------------------- TESTS CON PANDAS --------------------

def test_total_personas_pandas():
    """
    Verifica que el número total de personas en el DataFrame (Pandas) es mayor a cero.
    """
    df = pd.read_csv(ruta_csv)
    assert len(df) > 0, "❌ El DataFrame está vacío (Pandas)"

def test_is_remote_pandas():
    """
    Verifica que la columna 'is_remote' se genera correctamente en Pandas.
    """
    df = pd.read_csv(ruta_csv)
    df["is_remote"] = df["ocupacion"].str.lower().isin(remotos)
    assert "is_remote" in df.columns, "❌ La columna 'is_remote' no fue creada (Pandas)"
    assert df["is_remote"].dtype == bool or df["is_remote"].dtype == object, "❌ Tipo incorrecto en 'is_remote' (Pandas)"

def test_no_menores_pandas():
    """
    Verifica que no hay personas menores de edad en el DataFrame usando Pandas.
    Si las hay, muestra cuántas y quiénes son con nombre y edad.
    """
    df = pd.read_csv(ruta_csv)
    df["edad"] = pd.to_numeric(df["edad"], errors="coerce")  # Asegura tipo numérico
    menores = df[df["edad"] < 18]

    assert menores.empty, (
        f"❌ Hay {len(menores)} menores de edad:\n" +
        "\n".join(f"- {row['nombre']} ({int(row['edad'])})" for _, row in menores.iterrows())
    )

# -------------------- TESTS CON POLARS --------------------

def test_total_personas_polars():
    """
    Verifica que el número total de personas en el DataFrame (Polars) es mayor a cero.
    """
    df = pl.read_csv(ruta_csv)
    assert df.shape[0] > 0, "❌ El DataFrame está vacío (Polars)"

def test_is_remote_polars():
    """
    Verifica que la columna 'is_remote' se genera correctamente en Polars.
    """
    df = pl.read_csv(ruta_csv)
    df = df.with_columns([
        df["ocupacion"]
        .str.to_lowercase()
        .is_in(remotos)
        .alias("is_remote")
    ])
    assert "is_remote" in df.columns, "❌ La columna 'is_remote' no fue creada (Polars)"
    assert df["is_remote"].dtype == pl.Boolean, "❌ Tipo incorrecto en 'is_remote' (Polars)"

def test_no_menores_polars():
    """
    Verifica que no hay personas menores de edad en el DataFrame usando Polars.
    Si las hay, muestra cuántas y quiénes son con nombre y edad.
    """
    df = pl.read_csv(ruta_csv)
    df = df.with_columns([
        df["edad"].cast(pl.Int64)
    ])
    menores = df.filter(pl.col("edad") < 18)

    assert menores.is_empty(), (
        f"❌ Hay {menores.shape[0]} menores de edad:\n" +
        "\n".join(f"- {row['nombre']} ({row['edad']})" for row in menores.rows())
    )
