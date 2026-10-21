"""Da la bienvenida si la edad esta entre 18 y 64 anos."""

# Se convierten las respuestas a enteros para comparar edad y opcion.
edad = int(input("Ingresa tu edad: "))
sexo = int(input("""
Ingresa tu sexo:
[1] Masculino
[2] Femenino
>>> """))

# Valida primero la opcion para no asignar un saludo incorrecto.
if sexo == 1:
    saludo = "caballero"
elif sexo == 2:
    saludo = "dama"
else:
    print("Esa opcion no es valida")
    raise SystemExit

# El limite superior es exclusivo: se aceptan edades desde 18 hasta 64.
if 18 <= edad < 65:
    print(f"Hola {saludo} de {edad} anos de edad")
else:
    print("Para usar el programa debes tener entre 18 y 64 anos")
