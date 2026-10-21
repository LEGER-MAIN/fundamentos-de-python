"""Ejemplos de funciones, parametros, valores de retorno y una calculadora."""


def saludar():
    """Imprime un saludo general."""
    print("Hola, que tal")


def saludar_persona(persona="Persona generica"):
    """Saluda a la persona indicada o usa el valor predeterminado."""
    print(f"Hola, que tal {persona}")


def sumar(num1, num2):
    return num1 + num2


def restar(num1, num2):
    return num1 - num2


def dividir(num1, num2):
    if num2 == 0:
        raise ValueError("No se puede dividir por cero")
    return num1 / num2


def multiplicar(num1, num2):
    return num1 * num2


def programa():
    """Solicita una operacion y muestra el resultado."""
    menu = input("""
[1] Sumar
[2] Restar
[3] Dividir
[4] Multiplicar
[5] Salir
>>> """)

    if menu == "5":
        return False
    if menu not in {"1", "2", "3", "4"}:
        print("Esa opcion no esta en el menu")
        return True

    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    operaciones = {
        "1": ("suma", sumar),
        "2": ("resta", restar),
        "3": ("division", dividir),
        "4": ("multiplicacion", multiplicar),
    }
    nombre_operacion, funcion = operaciones[menu]

    try:
        resultado = funcion(num1, num2)
    except ValueError as error:
        print(f"No se pudo realizar la operacion: {error}")
    else:
        print(f"El resultado de la {nombre_operacion} es {resultado}")
    return True


if __name__ == "__main__":
    # Ejemplos directos de funciones antes de iniciar la calculadora.
    saludar()
    saludar_persona("Gaston")
    print(f"Ejemplo de suma: 3 + 3 = {sumar(3, 3)}")

    while programa():
        pass
