"""Una clase define atributos y comportamientos compartidos por sus objetos."""


class Auto:
    def __init__(self, marca, color, cantidad_ruedas, velocidad_max):
        self.marca = marca
        self.color = color
        self.cantidad_ruedas = cantidad_ruedas
        self.velocidad_max = velocidad_max
        self.motor = 2.0
        self.motores_disponibles = [2.0, 3.0]
        self.marcas_preestablecidas = {
            "alta_gama": "Audi",
            "economica": "Toyota",
        }

    def __str__(self):
        return (
            f"Auto: {self.marca}, color {self.color}, "
            f"{self.cantidad_ruedas} ruedas, motor {self.motor} L, "
            f"velocidad maxima {self.velocidad_max} km/h"
        )

    def acelerar(self):
        print(f"El {self.marca} puede alcanzar {self.velocidad_max} km/h")

    def frenar(self):
        print(f"El {self.marca} ha frenado")


# Cada instancia tiene sus propios atributos.
aventador = Auto("Lamborghini", "blanco", 4, 320)
huracan = Auto("Lamborghini", "rojo", 4, 300)

print(aventador)
print(f"Color del primer auto: {aventador.color}")
print(huracan)
print(f"Color del segundo auto: {huracan.color}")

aventador.acelerar()
aventador.frenar()
huracan.acelerar()

# Se puede modificar un atributo de una instancia.
aventador.color = "amarillo"
print(f"Nuevo color: {aventador.color}")

# Las listas y diccionarios tambien pueden ser atributos.
print(f"Motor alternativo: {aventador.motores_disponibles[1]} L")
print(f"Marca economica: {aventador.marcas_preestablecidas['economica']}")
