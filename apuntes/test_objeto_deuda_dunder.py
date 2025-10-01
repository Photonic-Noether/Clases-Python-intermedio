from objeto_deuda_dunder import Deuda

def test_metodos_dunder_deuda():
    # Instancias base
    deuda1 = Deuda("Miguel", 1200)
    deuda2 = Deuda("Miguel", 800)
    deuda3 = Deuda("Miguel", -500)
    deuda4 = Deuda("Miguel", 0)

    # __str__: representación amigable
    assert str(deuda1) == "Deuda de Miguel: 1200€"

    # __repr__: representación técnica
    assert repr(deuda1) == "Deuda(titular='Miguel', monto=1200)"

    # __eq__: comparación de igualdad
    assert deuda1 == Deuda("Miguel", 1200)
    assert deuda1 != deuda2

    # __add__: suma de montos
    suma = deuda1 + deuda2
    assert isinstance(suma, Deuda)
    assert suma.titular == "Miguel"
    assert suma.monto == 2000

    # __len__: número de dígitos del monto absoluto
    assert len(deuda3) == 3  # abs(-500) → "500" → 3 dígitos

    # __lt__: comparación por monto
    assert deuda2 < deuda1

    # __abs__: valor nominal de la deuda
    assert abs(deuda3) == 500

    # __neg__: cancelación de deuda
    cancelada = -deuda1
    assert isinstance(cancelada, Deuda)
    assert cancelada.monto == 0
    assert cancelada.titular == "Miguel"

    # __bool__: estado booleano de la deuda
    assert bool(deuda1) is True
    assert bool(deuda4) is False




from objeto_deuda_dunder import Deuda

def test_metodos_dunder_deuda():

    deuda1 = Deuda("Miguel", 1200)
    deuda2 = Deuda("Miguel", 800)
    deuda3 = Deuda("Miguel", -500)
    deuda4 = Deuda("Miguel", 0)

    assert str(deuda1) == "Deuda de Miguel: 1200€"

    assert repr(deuda1) == "Deuda(titular='Miguel', monto=1200)"

    assert deuda1 == Deuda("Miguel", 1200)
    assert deuda1 != deuda2

  
    suma = deuda1 + deuda2
    assert isinstance(suma, Deuda)
    assert suma.titular == "Miguel"
    assert suma.monto == 2000

    assert len(deuda3) == 3 

    assert deuda2 < deuda1

    assert abs(deuda3) == 500

    cancelada = -deuda1
    assert isinstance(cancelada, Deuda)
    assert cancelada.monto == 0
    assert cancelada.titular == "Miguel"

    assert bool(deuda1) is True
    assert bool(deuda4) is False
