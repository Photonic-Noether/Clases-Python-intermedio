# test_tarea.py

from dataclass_tareas import Tarea  # Asumiendo que la clase está en tarea.py

def test_comparacion_por_prioridad():
    """
    Las tareas con mayor prioridad deben considerarse 'mayores'.
    """
    alta = Tarea(prioridad=5, nombre="Alta prioridad")
    media = Tarea(prioridad=3, nombre="Media prioridad")
    baja = Tarea(prioridad=1, nombre="Baja prioridad")

    assert alta > media
    assert media > baja
    assert alta > baja

def test_ordenamiento_de_tareas():
    """
    Las tareas deben ordenarse por prioridad descendente.
    """
    tareas = [
        Tarea(prioridad=2, nombre="Segundo"),
        Tarea(prioridad=4, nombre="Cuarto"),
        Tarea(prioridad=1, nombre="Primero"),
        Tarea(prioridad=3, nombre="Tercero")
    ]

    tareas_ordenadas = sorted(tareas, reverse=True)
    prioridades = [t.prioridad for t in tareas_ordenadas]

    assert prioridades == [4, 3, 2, 1]

def test_str_de_tarea():
    """
    El método __str__ debe mostrar la prioridad y el nombre.
    """
    tarea = Tarea(prioridad=7, nombre="Revisar documentación")
    assert str(tarea) == "[7] Revisar documentación"
