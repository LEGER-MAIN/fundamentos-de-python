"""Composicion: un catalogo contiene una lista de objetos Pelicula."""


class Catalogo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.peliculas = []

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def mostrar_peliculas(self):
        print(f"Peliculas de {self.nombre}:")
        for pelicula in self.peliculas:
            print(f"- {pelicula}")


class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

    def __repr__(self):
        return f"{self.nombre} ({self.duracion} min, {self.genero})"


# Un catalogo guarda varias peliculas y permite consultarlas.
catalogo = Catalogo("Catalogo de peliculas")
catalogo.agregar_pelicula(Pelicula("Actividad Paranormal", 120, "terror"))
catalogo.agregar_pelicula(Pelicula("Toy Story", 81, "animacion"))

catalogo.mostrar_peliculas()
print(f"Primera pelicula: {catalogo.peliculas[0].nombre}")
