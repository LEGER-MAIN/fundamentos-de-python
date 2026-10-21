"""Modulo de ejemplo: define una funcion y una clase para reutilizar."""

nombre = "Gaston"
edad = 21


def saludar(nombre):
    """Devuelve un saludo para el nombre recibido."""
    return f"Hola {nombre}"


class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.es_premium = False

    def activar_premium(self):
        self.es_premium = True


if __name__ == "__main__":
    # Estos ejemplos solo se ejecutan al iniciar este archivo directamente.
    print(saludar(nombre))
    print(f"Edad de {nombre}: {edad}")
    usuario = Usuario("Mia", "mia@example.com")
    usuario.activar_premium()
    print(f"{usuario.nombre} tiene premium: {usuario.es_premium}")
