"""Los diccionarios relacionan claves unicas con valores."""

# Cada clave identifica un valor; las claves son unicas.
palabras_ingles = {"hello": "hola", "day": "dia"}
numeros = {"veinte": 20, "treinta": 30}

print(f"Diccionario inicial: {palabras_ingles}")
print(f"Traduccion de hello: {palabras_ingles['hello']}")

# Se puede actualizar un valor o agregar una clave nueva.
palabras_ingles["hello"] = "saludo"
palabras_ingles["night"] = "noche"
print(f"Diccionario actualizado: {palabras_ingles}")
print(f"Suma de valores: {numeros['veinte'] + numeros['treinta']}")

# Iterar por claves y valores.
for clave in palabras_ingles:
    print(f"Clave: {clave}")

for clave, valor in palabras_ingles.items():
    print(f"{clave}: {valor}")

# Un diccionario puede describir un objeto con campos de distintos tipos.
producto = {
    "nombre": "heladera",
    "precio": 2000,
    "stock": 20,
}
print(
    f"Producto: {producto['nombre']}, "
    f"precio: {producto['precio']}, stock: {producto['stock']}"
)
