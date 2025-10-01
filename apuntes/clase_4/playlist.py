class Cancion:
    """
    Representa una canción con título y artista.
    """
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

    def __str__(self):
        return f"{self.titulo} - {self.artista}"

    def __repr__(self):
        return f"Cancion(titulo='{self.titulo}', artista='{self.artista}')"

    def __eq__(self, other):
        return isinstance(other, Cancion) and self.titulo == other.titulo and self.artista == other.artista


class Playlist:
    """
    Representa una lista de reproducción de canciones.
    Soporta acceso por índice, búsqueda, iteración y longitud.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar(self, cancion):
        self.canciones.append(cancion)

    def __str__(self):
        return f"Playlist '{self.nombre}' con {len(self)} canciones"

    def __repr__(self):
        return f"Playlist(nombre='{self.nombre}', canciones={self.canciones})"

    def __len__(self):
        return len(self.canciones)

    def __getitem__(self, index):
        return self.canciones[index]

    def __iter__(self):
        return iter(self.canciones)

    def __contains__(self, titulo):
        return any(c.titulo == titulo for c in self.canciones)


# ******* Ejemplos de uso *******

# Crear canciones
c1 = Cancion("Bohemian Rhapsody", "Queen")
c2 = Cancion("Imagine", "John Lennon")
c3 = Cancion("Stairway to Heaven", "Led Zeppelin")

# Crear playlist
rock = Playlist("Rock Clasico")
rock.agregar(c1)
rock.agregar(c2)
rock.agregar(c3)

# Imprimir playlist
print(str(rock))  # Playlist 'Rock Clásico' con 3 canciones

# Acceder por índice
print(rock[1])  # Imagine - John Lennon

# Iterar
for cancion in rock:
    print(cancion)

# Buscar por título
print("Imagine" in rock)  # True
print("Yesterday" in rock)  # False
