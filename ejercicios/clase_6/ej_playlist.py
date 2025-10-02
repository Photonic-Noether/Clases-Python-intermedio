# Crear una Playlist con Canciones, y que esa playlist se pueda tratar como una lista
import pytest

class Cancion:
    def __init__(self, nombre:str, artista:str, estilo:str, duracion:float):
        self.nombre = nombre
        self.artista = artista
        self.estilo = estilo
        self.duracion = duracion


class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = {}

    def añadirCancion(self, cancion:Cancion):
        self.canciones[cancion.nombre] = cancion

    def __getitem__(self, nombre):
        return self.canciones[nombre]
    
    def __len__(self):
        return len(self.canciones)
    
    def __iter__(self):
        return iter(self.canciones)
    
c = Cancion("Wonderwall", "Oasis", "Rock", 2.30)
p = Playlist("MiMusica")


@pytest.fixture
def playlist():
    p = Playlist("MiMusica")
    return p
@pytest.fixture
def cancion():
    return Cancion("Wonderwall", "Oasis", "Rock", 2.30)

def test_nombre(playlist):
    assert playlist.nombre == "MiMusica"

def test_añadir_cancion(cancion, playlist):
    p = playlist
    p.añadirCancion(cancion)
    assert p["Wonderwall"].artista == "Oasis"
    assert p["Wonderwall"].estilo == "Rock"
    assert p["Wonderwall"].duracion == 2.30

def test_tamaño_playlist(playlist, cancion):
    playlist.añadirCancion(cancion)
    assert len(playlist) == 1

def test_iterar_playlist(playlist, cancion):
    c2 = Cancion("Wonderwall2", "Oasis2", "Rock22", 2.30)
    playlist.añadirCancion(cancion)
    playlist.añadirCancion(c2)

    cancion = playlist.canciones["Wonderwall"]

    p = list(playlist)  # Esto llama a __iter__ automáticamente

    assert len(p) == 2
    assert p["Wonderwall"].artista == "Oasis"
    assert p["Wonderwall"].estilo == "Rock"
    assert p["Wonderwall2"].artista == "Oasis2"
    assert p["Wonderwall2"].estilo == "Rock22"