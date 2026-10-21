"""Importar codigo propio y modulos de la biblioteca estandar."""

import random
from math import sqrt

# El import relativo funciona al ejecutar como paquete; el segundo caso permite
# ejecutar directamente este archivo desde la carpeta temasExtras.
if __package__:
    from .programa1 import Usuario, saludar
else:
    from programa1 import Usuario, saludar

# Se reutilizan la funcion y la clase definidas en programa1.py.
usuario = Usuario("Gaston", "gaston@example.com")
usuario.activar_premium()
print(saludar(usuario.nombre))
print(f"Cuenta premium: {usuario.es_premium}")

# sqrt y choice son ejemplos de importacion desde modulos de Python.
print(f"Raiz cuadrada de 25: {sqrt(25)}")
print(f"Numero aleatorio entre 1 y 10: {random.randint(1, 10)}")
