"""Pide el nombre y la edad, saluda y muestra la edad cinco anos menor."""

# input devuelve texto; int convierte el dato de edad para poder restarlo.
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

# Las f-strings permiten insertar variables y expresiones en un mensaje.
print(f"Hola {nombre}, si restamos 5 anos tu edad seria {edad - 5}.")

# Ejemplo sin pedir datos: 30 - 5 da como resultado 25.
edad_ejemplo = 30
print(f"Ejemplo: {edad_ejemplo} - 5 = {edad_ejemplo - 5}")
