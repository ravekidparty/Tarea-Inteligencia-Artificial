import math


class Esfera:
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser un número positivo.")
        self.radio = radio

    def calcular_area(self):
        return 4 * math.pi * self.radio ** 2

    def calcular_volumen(self):
        return (4 / 3) * math.pi * self.radio ** 3

    def calcular_diametro(self):
        return 2 * self.radio


# Programa principal
try:
    radio = float(input("Ingrese el radio de la esfera: "))

    esfera = Esfera(radio)

    print(f"Área de la superficie: {esfera.calcular_area():.2f}")
    print(f"Volumen: {esfera.calcular_volumen():.2f}")
    print(f"Diámetro: {esfera.calcular_diametro():.2f}")

except ValueError as error:
    print(f"Error: {error}")
