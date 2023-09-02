
#listas
frutas = ["manzana", "banana", "pera", "uva"]
# impresion del primer elemento
print(frutas[0])
# Agregar un elemento al final
frutas.append("naranja")  
# Eliminar un elemento por valor
frutas.remove("pera") 
# Longitud de la lista 
print(len(frutas))  

#Tuplas
coordenadas = (3, 5)
x, y = coordenadas  # Desempaquetar valores
print("x:", x, "y:", y)

#Diccionarios
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
# Impresion de un valor por clave
print(persona["nombre"])  
# Agregar un nuevo par clave-valor
persona["profesion"] = "Ingeniero"  
 # Eliminar un elemento por clave
del persona["ciudad"] 

#Conjuntos
colores = {"rojo", "verde", "azul"}
 # Agregar un elemento
colores.add("amarillo")
# Eliminar un elemento 
colores.remove("verde")  
# Verificar si un elemento está en el conjunto
print("amarillo" in colores)  
