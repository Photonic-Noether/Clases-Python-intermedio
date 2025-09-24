import pandas as pd
import polars as pl

def test_is_remote_pandas():
    """
    Test usando Pandas para verificar la lógica de 'is_remote'.
    """
    data = {
        "nombre": ["Carlos", "Raquel", "Ana"],
        "ocupacion": ["Ingeniero", "Directora de Marketing", "Desarrollador"]
    }
    df = pd.DataFrame(data)
    remotos = ["ingeniero", "desarrollador"]
    df["is_remote"] = df["ocupacion"].str.lower().apply(
        lambda x: any(r in x for r in remotos)
    )
    assert df["is_remote"].tolist() == [True, False, True]
    print(" Test Pandas: lógica 'is_remote' correcta")


def test_is_remote_polars():
    df = pl.DataFrame({
        "nombre": ["Carlos", "Raquel", "Ana", "Luis"],
        "ocupacion": ["Ingeniero", "Directora de Marketing", "Desarrollador", "Contable"]
    })

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

    expected = [True, False, True, False]
    result = df["is_remote"].to_list()

    assert result == expected, f"❌ Test Polars fallido: {result} ≠ {expected}"
    print(" Test Polars: lógica 'is_remote' correcta")

# Comprobar que los menores no estan en la lista


import pandas as pd
import polars as pl

def test_no_menores_pandas():
    """
    Verifica que no hay personas menores de edad en el DataFrame usando Pandas.
    """
    df = pd.read_csv("./apuntes/clase_1/data.csv")
    assert all(df["edad"] >= 18), "❌ Hay menores de edad en el DataFrame (Pandas)"
    print("✅ Test Pandas: no hay menores de edad")

def test_no_menores_polars():
    """
    Verifica que no hay personas menores de edad en el DataFrame usando Polars.
    """
    df = pl.read_csv("./apuntes/clase_1/data.csv")
    menores = df.filter(pl.col("edad") < 18)
    assert menores.shape[0] == 0, f"❌ Hay {menores.shape[0]} menores de edad en el DataFrame (Polars)"
    print("✅ Test Polars: no hay menores de edad")
