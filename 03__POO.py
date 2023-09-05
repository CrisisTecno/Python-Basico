# Pilar de Encapsulación
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Encapsulamos el atributo nombre
        self.__edad = edad      # Encapsulamos el atributo edad

    # Getter para obtener el nombre
    def get_nombre(self):
        return self.__nombre

    # Setter para actualizar el nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Método para mostrar detalles de la persona
    def mostrar_informacion(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}")

# Pilar de Abstracción
class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base
        self.matricula = matricula

    # Método para mostrar detalles del estudiante (abstracción)
    def mostrar_informacion(self):
        print(f"Nombre: {self.get_nombre()}, Edad: {self._Persona__edad}, Matrícula: {self.matricula}")

# Pilar de Herencia
class Profesor(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base
        self.salario = salario

# Pilar de Polimorfismo
def presentar_persona(persona):
    persona.mostrar_informacion()

# Creación de objetos
juan = Estudiante("Juan", 20, "12345")
ana = Profesor("Ana", 35, 50000)

# Uso del polimorfismo para presentar información
print("Información del Estudiante:")
presentar_persona(juan)

print("\nInformación del Profesor:")
presentar_persona(ana)
