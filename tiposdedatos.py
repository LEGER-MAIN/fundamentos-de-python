"""Tipos basicos de datos y conversion de texto ingresado por teclado."""

# str: texto; int: entero; float: numero con decimales; bool: verdadero/falso.
nombre = "Belen"
edad = 21
altura = 1.75
persona_masculina = True

# input siempre devuelve texto, por eso se guarda como str explicitamente.
nombre_ingresado = input("Ingrese su nombre: ")
print(f"Hola {nombre_ingresado}, tu edad es {edad + 5}")

# Ejemplos de los otros valores y de sus tipos.
print(f"Nombre: {nombre} ({type(nombre).__name__})")
print(f"Edad: {edad} ({type(edad).__name__})")
print(f"Altura: {altura} m ({type(altura).__name__})")
print(f"Es masculino: {persona_masculina} ({type(persona_masculina).__name__})")
