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
    print(" Test Polars: lógica 'is_remote' correcta"