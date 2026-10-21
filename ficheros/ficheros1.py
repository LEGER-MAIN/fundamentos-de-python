"""Leer y escribir archivos de texto usando la ruta de este ejemplo."""

from pathlib import Path

RUTA_FICHERO = Path(__file__).with_name("file.txt")


def leer_fichero():
    """Muestra todo el contenido del archivo."""
    with RUTA_FICHERO.open("r", encoding="utf-8") as fichero:
        contenido = fichero.read()
    print(contenido)


def escribir_fichero(contenido):
    """Reemplaza el contenido existente por el texto indicado."""
    with RUTA_FICHERO.open("w", encoding="utf-8") as fichero:
        fichero.write(contenido)


def agregar_linea(linea):
    """Agrega una linea al final sin borrar el contenido anterior."""
    with RUTA_FICHERO.open("a", encoding="utf-8") as fichero:
        fichero.write(f"\n{linea}")


if __name__ == "__main__":
    # Ejemplo de lectura. Las funciones de escritura estan disponibles arriba:
    # escribir_fichero("Texto inicial")
    # agregar_linea("Una segunda linea")
    leer_fichero()
