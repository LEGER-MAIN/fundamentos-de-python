"""Encapsulamiento: acceder a datos privados mediante metodos publicos."""


class Curso:
    def __init__(self, titulo, duracion):
        self.__titulo = titulo
        self.__duracion = duracion

    def adquirir_curso(self):
        print(f"Has adquirido el curso {self.__titulo}")

    def obtener_titulo(self):
        return self.__titulo

    def cambiar_titulo(self, titulo):
        if not titulo.strip():
            raise ValueError("El titulo no puede estar vacio")
        self.__titulo = titulo

    def obtener_duracion(self):
        return self.__duracion


# Los metodos publicos permiten consultar o cambiar el estado interno.
curso = Curso("Backend Python 3", 20)
curso.adquirir_curso()
print(f"Titulo: {curso.obtener_titulo()}")
print(f"Duracion: {curso.obtener_duracion()} horas")

curso.cambiar_titulo("Backend Python avanzado")
print(f"Nuevo titulo: {curso.obtener_titulo()}")
