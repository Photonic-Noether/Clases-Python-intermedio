import pytest
from fabrica_procesadores_archivos import (
    FabricaInyectada,
    ProcesadorCSV,
    ProcesadorJSON,
    ProcesadorTXT,
    ProcesadorXML,
    ProcesadorArchivo
)


def test_csv():
    proc = FabricaInyectada(ProcesadorCSV).crear()
    assert isinstance(proc, ProcesadorCSV)

def test_json():
    proc = FabricaInyectada(ProcesadorJSON).crear()
    assert isinstance(proc, ProcesadorJSON)

def test_txt():
    proc = FabricaInyectada(ProcesadorTXT).crear()
    assert isinstance(proc, ProcesadorTXT)

def test_xml():
    proc = FabricaInyectada(ProcesadorXML).crear()
    assert isinstance(proc, ProcesadorXML)

def test_ini_exception():
    class ProcesadorINI(ProcesadorArchivo):
        def leer(self, ruta: str): pass
        def escribir(self, ruta: str, contenido): pass

    with pytest.raises(ValueError, match="INI"):
        FabricaInyectada(ProcesadorINI)
