from filtro_contar_letras_nombres_unicos import contar_letras_nombres_unicos

def test_contador_nombres_unicos():
    nombres = ["Joana", "Miguel", "Mateo", "Joana", "Lucía"]
    resultado = contar_letras_nombres_unicos(nombres)
    assert resultado == {
        "miguel": 6,
        "mateo": 5,
        "lucía": 5
    }
