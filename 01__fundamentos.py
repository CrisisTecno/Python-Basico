

#Fudamentos
nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True


#declaracion
a = 10
b = 3


#Operadores y Expresiones
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b
potencia = a ** b

#Estructuras de Control

edad=20

#if == si cumple una condicion 
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#for == para cada elemento i en un rango de 5

for i in range(5):
    print(i)

#while == mientras numero sema menor a 5 se realizara el bucle
numero = 0
while numero < 5:
    print(numero)
    numero += 1

#Funciones 
def saludar(nombre):
    print("Hola,", nombre)

def suma(a, b):
    return a + b
#en este caso invocamos a la funcion saludar dando a "ana" como el valor de 
#nombre dentro de la funcion
saludar("Ana")
#de la misma manera sabiendo el retorno de cada funcion podemos alamacenar 
#el resultado en una variable al momento de invocar la funcion
resultado = suma(5, 3)
print(resultado)


#Manejo de Excepciones con try-except
#nos sirve para el manejo de los posibles errores en nuestro codigo 
try:
    num = int(input("Ingresa un número: "))
    #si num es 0 entonces causaria el error por ese motivo en particular en este caso usamos el try-except
    resultado = 10 / num
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("No puedes dividir por cero")
except ValueError:
    print("Debes ingresar un número válido")
