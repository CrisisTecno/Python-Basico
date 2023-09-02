
# Una lista por comprensión es una expresión compacta que genera una nueva lista 
# aplicando una operación a cada elemento de una secuencia (como una lista, tupla, rango, etc.) 
# o filtrando elementos según una condición.


# Ejemplo de lista de comprensión para obtener los cuadrados de los números del 1 al 5
cuadrados = [x ** 2 for x in range(1, 6)]
print(cuadrados)

# Lista de comprensión para filtrar números pares de una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
print(pares)

# Lista de comprensión para combinar elementos de dos listas en una nueva lista
nombres = ["Ana", "Juan", "Eva"]
apellidos = ["Pérez", "López", "González"]
nombres_completos = [nombre + " " + apellido for nombre, apellido in zip(nombres, apellidos)]
print(nombres_completos)
