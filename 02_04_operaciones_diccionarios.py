# Operaciones con Diccionarios

# Crear un diccionario de ejemplo
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Imprimir el diccionario original
print("\nDiccionario de persona:", persona)

# Obtener las claves del diccionario
claves = persona.keys()
print("Claves del diccionario:", claves)

# Obtener los valores del diccionario
valores = persona.values()
print("Valores del diccionario:", valores)

# Verificar si una clave existe en el diccionario
if "edad" in persona:
    print("La clave 'edad' existe en el diccionario")

# Agregar una nueva clave-valor al diccionario
persona["profesion"] = "Ingeniero"
print("Diccionario actualizado:", persona)

# Eliminar una clave del diccionario
del persona["ciudad"]
print("Diccionario después de eliminar 'ciudad':", persona)