# Definición de la clase Rectangulo
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        """
        Calcula y devuelve el área del rectángulo.
        Fórmula: Área = Largo x Ancho
        """
        return self.largo * self.ancho

    def calcular_perimetro(self):
        """
        Calcula y devuelve el perímetro del rectángulo.
        Fórmula: Perímetro = 2 x (Largo + Ancho)
        """
        return 2 * (self.largo + self.ancho)

# Creación de un objeto Rectangulo
mi_rectangulo = Rectangulo(5, 3)

# Acceso a atributos y métodos
area = mi_rectangulo.calcular_area()
perimetro = mi_rectangulo.calcular_perimetro()

# Impresión de resultados
print("Características del Rectángulo:")
print(f"Largo: {mi_rectangulo.largo}")
print(f"Ancho: {mi_rectangulo.ancho}")
print(f"Área: {area}")
print(f"Perímetro: {perimetro}")
