"""Ejemplos de importaciones estandar y de una dependencia externa."""

import importlib.util
import math
import random

# math y random forman parte de la biblioteca estandar de Python.
print(f"La raiz cuadrada de 81 es {math.sqrt(81)}")
print(f"Elemento aleatorio: {random.choice(['rojo', 'verde', 'azul'])}")

# PyMySQL es externo: instalarlo con `python -m pip install pymysql`.
# Despues de instalarlo se puede usar `import pymysql` en el programa.
if importlib.util.find_spec("pymysql") is None:
    print("PyMySQL no esta instalado; los ejemplos estandar siguen funcionando")
else:
    print("PyMySQL esta instalado y puede importarse en otro ejemplo")
