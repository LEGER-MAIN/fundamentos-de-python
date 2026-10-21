"""Herencia: Perro y Gato reutilizan los atributos y metodos de Animal."""


class Animal:
    def __init__(self, edad, numero_patas, alimentacion):
        self.edad = edad
        self.numero_patas = numero_patas
        self.alimentacion = alimentacion

    def caminar(self):
        print("El animal camina")

    def correr(self):
        print("El animal corre")


class Perro(Animal):
    def __init__(self, edad, raza, pelaje):
        super().__init__(edad, 4, "carnivora")
        self.raza = raza
        self.pelaje = pelaje

    def ladrar(self):
        print("El perro ladra")


class Gato(Animal):
    def __init__(self, edad, color):
        super().__init__(edad, 4, "carnivora")
        self.color = color

    def saltar(self):
        print("El gato salta")


# El perro hereda edad, patas y alimentacion de Animal.
perro = Perro(5, "Caniche", "blanco")
print(
    f"Perro: {perro.raza}, {perro.edad} anos, "
    f"{perro.numero_patas} patas, pelaje {perro.pelaje}"
)
perro.caminar()
perro.ladrar()

# Gato tambien hereda el comportamiento comun y agrega el suyo.
gato = Gato(3, "gris")
print(f"Gato: {gato.color}, alimentacion {gato.alimentacion}")
gato.correr()
gato.saltar()
