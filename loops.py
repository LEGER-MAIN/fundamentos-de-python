"""Ejemplos de ciclos for, range y while."""

tabla_a_calcular = int(input("Ingrese la tabla que desea calcular: "))
hasta_donde = int(input(
    f"Hasta que numero desea calcular la tabla del {tabla_a_calcular}: "
))

# range empieza en cero y no incluye el limite superior.
# Se usa +1 para imprimir desde la multiplicacion por 1 hasta el limite.
for multiplicador in range(1, hasta_donde + 1):
    print(
        f"{tabla_a_calcular} x {multiplicador} = "
        f"{tabla_a_calcular * multiplicador}"
    )

# Un ciclo while debe cambiar su condicion para terminar.
contador = 1
while contador <= 3:
    print(f"Ejemplo de while: vuelta {contador}")
    contador += 1

# range tambien puede crear una secuencia de numeros.
for numero in range(1, 4):
    print(f"Numero de ejemplo: {numero}")
