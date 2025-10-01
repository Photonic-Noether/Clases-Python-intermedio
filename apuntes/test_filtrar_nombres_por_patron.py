# tests/test_eliminar_por_patron.py

from filtro_eliminar_por_patron import eliminar_por_patron

def test_eliminar_patron_joa():
    nombres = ["Joana", "Joaquín", "Juan", "Miguel", "Mateo"]
    resultado = eliminar_por_patron(nombres, "joa")
    assert resultado == ["Juan", "Miguel", "Mateo"]




# Usando Parametrize
# pytest
# from test_filtrar_nombres_por_patron import filtrar_por_patron  # Ajusta el nombre del módulo si es necesario
# 
# @pytest.mark.parametrize("patron,esperado", [
#     ("joa", []),
#     ("an", ["Antonella", "Antonella", "Andrés"]),
#     ("ma", ["Mateo", "Mariana", "Martina"]),
#     ("ca", ["Camila", "Carlos", "Camila"]),
#     ("ju", ["Julián", "Juan"]),
# ])
# def test_filtrar_por_patron(patron, esperado):
#     nombres = [
#         "Alejandro", "Valentina", "Santiago", "Isabella", "Mateo", "Camila",
#         "Sebastián", "Lucía", "Diego", "Mariana", "Daniel", "Sara",
#         "Julián", "Emma", "Gabriel", "Victoria", "Luis", "Antonella",
#         "Carlos", "Paula", "Miguel", "Natalia", "Andrés", "Renata",
#         "Fernando", "Elena", "Juan", "Mía", "Pablo", "Antonella",
#         "Ricardo", "Olivia", "Tomás", "Sofía", "Héctor", "Valeria",
#         "Álvaro", "Camila", "Javier", "Martina"
#     ]
#     resultado = filtrar_por_patron(nombres, patron)
#     assert resultado == esperado
