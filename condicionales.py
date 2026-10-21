# Las condiciones permiten ejecutar bloques distintos segun los datos.
nombre = "Pia"
edad = 15
persona_masculina = True
persona_femenina = False

# if / elif / else comparan el nombre con varias alternativas.
if nombre == "Gaston":
    print("Tu nombre es Gaston")
elif nombre == "Mario":
    print("Tu nombre es Mario")
elif nombre == "Belen":
    print("Tu nombre es Belen")
else:
    print("Tu nombre no es Gaston, Mario ni Belen")
    if nombre == "Mia":
        print("Aunque no estaba en las primeras opciones, tu nombre es Mia")

# Una condicion tambien puede comparar numeros.
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# and exige que ambas condiciones sean verdaderas.
if persona_masculina and not persona_femenina:
    print("El ejemplo indica que la persona es masculina")
else:
    print("Las condiciones no se cumplen")

# or es verdadero cuando se cumple al menos una de las condiciones.
if edad < 18 or nombre == "Pia":
    print("La persona es menor de edad o se llama Pia")

# not invierte el resultado de una condicion.
if not persona_femenina:
    print("La variable persona_femenina es falsa")
