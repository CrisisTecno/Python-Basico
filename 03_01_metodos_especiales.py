# Clase Punto en 2D
class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, otro_punto):
        nueva_x = self.x + otro_punto.x
        nueva_y = self.y + otro_punto.y
        return Punto2D(nueva_x, nueva_y)

# Creación de objetos
punto1 = Punto2D(1, 2)
punto2 = Punto2D(3, 4)

# Uso de métodos especiales
print("Punto 1:", punto1)
print("Punto 2:", punto2)

suma_puntos = punto1 + punto2
print("Suma de puntos:", suma_puntos)
