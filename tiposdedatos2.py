"""Las listas guardan varios valores en un orden que se puede modificar."""

nombres = ["Gaston", "Belen", "Mia", "Pia"]
edades = [20, 21, 25, 35, 64, 14, 12]
apellidos = [
    ["Fenske", "Benitez"],
    ["Lopez", "Rodriguez"],
    ["Gonzales", "Vilches"],
]

# Agregar, quitar, contar y acceder a elementos.
nombres.append("Ramon")
print(f"Lista actualizada: {nombres}")
nombres.pop()
print(f"Cantidad de nombres: {len(nombres)}")
print(f"Primer nombre: {nombres[0]}")

# Una lista puede contener otras listas.
print(f"Segundo apellido del primer registro: {apellidos[0][1]}")

# Funciones utiles para consultar y ordenar numeros.
print(f"Edad mayor: {max(edades)}")
print(f"Edad menor: {min(edades)}")
print(f"Edades ordenadas: {sorted(edades)}")
edades.remove(64)
print(f"Edades sin 64: {edades}")

# Recorrer una lista y construir otra con una comprension.
for nombre in nombres:
    print(f"Hola {nombre}")

pares_con_ciclo = []
for numero in range(10):
    if numero % 2 == 0:
        pares_con_ciclo.append(numero)
print(f"Pares con un ciclo: {pares_con_ciclo}")

pares_con_compresion = [numero for numero in range(10) if numero % 2 == 0]
print(f"Pares con comprension: {pares_con_compresion}")
