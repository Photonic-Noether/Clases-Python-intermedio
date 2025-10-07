from abc import ABC, abstractmethod

class ProcesadorArchivo(ABC):
    @abstractmethod
    def leer(self, ruta: str):
        ...

    @abstractmethod
    def escribir(self, ruta: str, contenido):
        ...

# Implementaciones concretas de la interfaz

class ProcesadorCSV(ProcesadorArchivo):
    def leer(self, ruta: str):
        print(f"Leyendo CSV desde {ruta}")

    def escribir(self, ruta: str, contenido):
        print(f"Escribiendo CSV en {ruta}")

class ProcesadorJSON(ProcesadorArchivo):
    def leer(self, ruta: str):
        print(f"Leyendo JSON desde {ruta}")

    def escribir(self, ruta: str, contenido):
        print(f"Escribiendo JSON en {ruta}")

class ProcesadorTXT(ProcesadorArchivo):
    def leer(self, ruta: str):
        print(f"Leyendo TXT desde {ruta}")

    def escribir(self, ruta: str, contenido):
        print(f"Escribiendo TXT en {ruta}")

class ProcesadorXML(ProcesadorArchivo):
    def leer(self, ruta: str):
        print(f"Leyendo XML desde {ruta}")

    def escribir(self, ruta: str, contenido):
        print(f"Escribiendo XML en {ruta}")

# Fábrica con inyección directa

class FabricaInyectada:
    def __init__(self, clase_procesadora: type[ProcesadorArchivo]):
        if clase_procesadora.__name__.lower() == "procesadorini":
            raise ValueError("El formato .INI no esta soportado por esta fabrica.")
        self.clase = clase_procesadora

    def crear(self) -> ProcesadorArchivo:
        return self.clase()


# **** Ejemplos de uso ****

if __name__ == "__main__":
    # CSV
    csv = FabricaInyectada(ProcesadorCSV).crear()
    csv.leer("archivo.csv")
    csv.escribir("archivo.csv", "nombre,edad\nAna,30")

    # JSON
    json = FabricaInyectada(ProcesadorJSON).crear()
    json.leer("archivo.json")
    json.escribir("archivo.json", {"modo": "debug", "activo": True})

    # TXT
    txt = FabricaInyectada(ProcesadorTXT).crear()
    txt.leer("archivo.txt")
    txt.escribir("archivo.txt", "Notas de clase")

    # XML
    xml = FabricaInyectada(ProcesadorXML).crear()
    xml.leer("archivo.xml")
    xml.escribir("archivo.xml", "<config><modo>debug</modo></config>")

    # INI (simulado como clase interna para provocar excepción)
    class ProcesadorINI(ProcesadorArchivo):
        def leer(self, ruta: str): pass
        def escribir(self, ruta: str, contenido): pass

    try:
        FabricaInyectada(ProcesadorINI)
    except ValueError as e:
        print("Error:", e)
