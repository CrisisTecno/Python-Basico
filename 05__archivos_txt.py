# Ejemplo de entrada y salida de archivos en Python

# Escribir datos en un archivo
with open('archivo_salida.txt', 'w') as archivo_salida:
    archivo_salida.write('Hola, este es un ejemplo de escritura en archivo.\n')
    archivo_salida.write('Estamos aprendiendo Python.\n')

# Leer datos desde un archivo
with open('archivo_salida.txt', 'r') as archivo_entrada:
    contenido = archivo_entrada.read()
    print('Contenido del archivo:')
    print(contenido)

# Agregar datos a un archivo existente
with open('archivo_salida.txt', 'a') as archivo_salida:
    archivo_salida.write('¡Añadiendo más información al archivo!\n')

# Leer el archivo actualizado
with open('archivo_salida.txt', 'r') as archivo_entrada:
    contenido_actualizado = archivo_entrada.read()
    print('\nContenido del archivo actualizado:')
    print(contenido_actualizado)
