"""Comprobar si un elemento esta incluido en una lista."""

lista = [1, 2, 3, 4, 5]

# in y not in comprueban la presencia de un valor.
if 3 in lista:
    print("El numero 3 esta en la lista")

if 6 not in lista:
    print("El numero 6 no esta en la lista")

# La misma comprobacion funciona con texto.
frutas = ["manzana", "pera", "uva"]
fruta_buscada = "pera"
print(f"{fruta_buscada} esta en la lista: {fruta_buscada in frutas}")
