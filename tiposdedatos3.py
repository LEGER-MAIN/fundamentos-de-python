palabras_ingles = {"hello": "hola", "day": "dia"}
numeros = {"veinte": 20, "treinta": 30}

print(palabras_ingles)
print(palabras_ingles["hello"])

palabras_ingles["hello"] = "salut"
print(palabras_ingles)
print(palabras_ingles["hello"])

palabras_ingles["night"] = "noche"
print(palabras_ingles)

print(numeros["veinte"] + numeros["treinta"])

for palabra in palabras_ingles:
    print(palabra)

for clave in palabras_ingles:
    print(f"{clave} : {palabras_ingles[clave]}")

for clave, valor in palabras_ingles:
    print(clave, valor)

producto = {
    "nombre": "heladera",
    "precio": 2000,
    "stock": 20
}
#javascript object notation













