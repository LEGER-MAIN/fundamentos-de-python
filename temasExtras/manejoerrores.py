"""Capturar errores comunes para que el programa pueda explicarlos."""


def dividir(numerador, denominador):
    """Devuelve una division o un mensaje claro ante entradas no validas."""
    try:
        resultado = numerador / denominador
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    else:
        print(f"El resultado es {resultado}")


try:
    menu = int(input("Ingrese una opcion numerica: "))
except ValueError as error:
    # ValueError ocurre, por ejemplo, si se escribe una palabra en vez de un numero.
    print(f"La opcion debe ser un numero entero: {error}")
else:
    print(f"Ha ingresado la opcion {menu}")

# Ejemplos de division correcta y del caso especial de divisor cero.
dividir(10, 2)
dividir(10, 0)
