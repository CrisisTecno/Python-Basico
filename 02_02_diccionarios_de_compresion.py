


# Un diccionario por comprensión es una expresión similar a las listas por comprensión, pero crea un nuevo diccionario aplicando una 
# operación a cada par clave-valor de un diccionario existente o filtrando pares clave-valor según una condición.

# Ejemplo de diccionario por comprensión para crear un diccionario de cuadrados
numeros = [1, 2, 3, 4, 5]
diccionario_cuadrados = {x: x ** 2 for x in numeros}
print(diccionario_cuadrados)

# Diccionario por comprensión para filtrar elementos con valores mayores a 50
datos = {"a": 45, "b": 72, "c": 30, "d": 90}
datos_filtrados = {clave: valor for clave, valor in datos.items() if valor > 50}
print(datos_filtrados)

# Diccionario por comprensión para invertir las claves y valores de un diccionario
diccionario_original = {"manzana": "fruta", "zanahoria": "vegetal", "pescado": "proteína"}
diccionario_invertido = {valor: clave for clave, valor in diccionario_original.items()}
print(diccionario_invertido)
