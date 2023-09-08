# Importar módulos del paquete
from mi_paquete import modulo1, modulo2

# Usar funciones y variables de modulo1
modulo1.saludo()
print("El valor de x en modulo1 es:", modulo1.x)

# Usar función de modulo2
modulo2.despedida()
# Contenido de modulo1.py
def saludo():
    print("¡Hola desde modulo1!")

x = 10
# Contenido de modulo2.py
def despedida():
    print("Adiós desde modulo2!")
