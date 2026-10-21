"""Ejemplos de tuplas y conjuntos (set)."""

# La tupla conserva el orden y puede contener valores de distintos tipos.
tupla = (100, "hello", ["familia", "amigos"], {"hello": "hola"})
print(f"Tupla completa: {tupla}")
print(f"Primer elemento: {tupla[0]}")
print(f"Ultimo elemento: {tupla[-1]}")
print(f"Cantidad de elementos: {len(tupla)}")

# No se puede reasignar un elemento: tupla[0] = 200 daria un TypeError.
# Para crear una version ampliada, se convierte temporalmente en lista.
tupla_modificable = list(tupla)
tupla_modificable.append(200)
tupla = tuple(tupla_modificable)
print(f"Nueva tupla: {tupla}")

# Un set elimina duplicados y permite comparar colecciones.
nuestro_set = {21, 24, 23, 14, 21, 21, 29}
otro_set = {14, 30, 31}
print(f"Conjunto sin duplicados: {nuestro_set}")
print(f"Elementos comunes: {nuestro_set & otro_set}")
print(f"Elementos de ambos conjuntos: {nuestro_set | otro_set}")
