# Supongamos que tienes la siguiente estructura de directorios:
# mi_paquete/
#     __init__.py
#     modulo1.py
#     modulo2.py
#     modulo3.py

# Importar módulos del paquete
from mi_paquete import modulo1, modulo2, modulo3

# Usar funciones y variables de los módulos
print(modulo1.saludo())
print(modulo2.multiplicar(5, 3))
print(modulo3.mensaje)


#Módulo 1 (modulo1.py):
def saludo():
    return "¡Hola desde el módulo 1!"

#Módulo 2 (modulo2.py):
def multiplicar(a, b):
    return a * b

#Módulo 3 (modulo3.py):
mensaje = "Este es el módulo 3."
