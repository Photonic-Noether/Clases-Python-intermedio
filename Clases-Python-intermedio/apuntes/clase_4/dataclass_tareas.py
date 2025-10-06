from dataclasses import dataclass

@dataclass(order=True)
class Tarea:
    prioridad: int
    nombre: str

    def __str__(self):
        return f"[{self.prioridad}] {self.nombre}"


# Ejemplo de salida:

t1 = Tarea(prioridad=3, nombre="Enviar informe")
t2 = Tarea(prioridad=5, nombre="Revisar código")
t3 = Tarea(prioridad=1, nombre="Responder emails")

tareas = [t1, t2, t3]
tareas_ordenadas = sorted(tareas, reverse=True)  # Mayor prioridad primero

for tarea in tareas_ordenadas:
    print(tarea)

    
