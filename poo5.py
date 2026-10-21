"""Polimorfismo: distintos objetos responden a un mismo metodo."""


class Arma:
    def __init__(self, balas, peso):
        self.balas = balas
        self.peso = peso

    def disparar(self):
        print("El arma dispara")


class Pistola(Arma):
    def disparar(self):
        print("La pistola dispara")


class Ametralladora(Arma):
    def disparar(self):
        print("La ametralladora dispara")


# Las tres instancias pueden tratarse de la misma manera.
elementos = [
    Arma(15, 7),
    Pistola(12, 5),
    Ametralladora(50, 12),
]

for elemento in elementos:
    elemento.disparar()
    print(f"Municion: {elemento.balas}; peso: {elemento.peso} kg")
