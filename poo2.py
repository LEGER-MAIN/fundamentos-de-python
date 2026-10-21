"""Ejemplos de atributos de clase, metodos y metodos estaticos."""


class Usuario:
    cantidad_usuarios = 0

    def __init__(self, nombre, apellido, edad, persona_masculina):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.persona_masculina = persona_masculina
        self.premium = False
        Usuario.cantidad_usuarios += 1

    def __repr__(self):
        return (
            f"{self.nombre} {self.apellido}, {self.edad} anos, "
            f"premium={self.premium}"
        )

    def convertir_premium(self):
        self.premium = True

    def mirar_peliculas(self):
        if self.premium:
            print(f"{self.nombre} puede ver las peliculas")
        else:
            print(f"{self.nombre} necesita una cuenta premium")

    @staticmethod
    def es_mayor_de_edad(edad):
        """Responde una pregunta que no depende de un usuario concreto."""
        return edad >= 18

    @classmethod
    def obtener_cantidad_usuarios(cls):
        """Devuelve el contador compartido por la clase."""
        return cls.cantidad_usuarios


# Se crean dos usuarios para observar el estado individual y el compartido.
usuario = Usuario("Gaston", "Fenske", 21, True)
usuario_invitado = Usuario("Mia", "Lopez", 17, False)

print(usuario)
usuario.mirar_peliculas()
usuario.convertir_premium()
print(usuario)
usuario.mirar_peliculas()

print(usuario_invitado)
print(f"Es mayor de edad con 18: {Usuario.es_mayor_de_edad(18)}")
print(f"Usuarios creados: {Usuario.obtener_cantidad_usuarios()}")
