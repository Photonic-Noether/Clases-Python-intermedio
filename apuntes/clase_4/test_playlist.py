from objeto_deuda_dunder import Cancion, Playlist

def test_metodos_dunder_playlist():
    # Crear canciones
    c1 = Cancion("Bohemian Rhapsody", "Queen")
    c2 = Cancion("Imagine", "John Lennon")
    c3 = Cancion("Stairway to Heaven", "Led Zeppelin")

    # Crear playlist y agregar canciones
    lista = Playlist("Rock Clásico")
    lista.agregar(c1)
    lista.agregar(c2)
    lista.agregar(c3)

    # __str__: resumen amigable
    assert str(lista) == "Playlist 'Rock Clásico' con 3 canciones"

    # __repr__: representación técnica
    assert repr(lista).startswith("Playlist(nombre='Rock Clásico', canciones=[")

    # __len__: número de canciones
    assert len(lista) == 3

    # __getitem__: acceso por índice
    assert lista[1] == c2

    # __iter__: recorrido con for
    titulos = [c.titulo for c in lista]
    assert titulos == ["Bohemian Rhapsody", "Imagine", "Stairway to Heaven"]

    # __contains__: búsqueda por título
    assert "Imagine" in lista
    assert "Yesterday" not in lista

def test_metodos_dunder_cancion():
    c1 = Cancion("Imagine", "John Lennon")
    c2 = Cancion("Imagine", "John Lennon")
    c3 = Cancion("Yesterday", "The Beatles")

    # __str__: formato amigable
    assert str(c1) == "Imagine - John Lennon"

    # __repr__: formato técnico
    assert repr(c1) == "Cancion(titulo='Imagine', artista='John Lennon')"

    # __eq__: comparación de canciones
    assert c1 == c2
    assert c1 != c3
