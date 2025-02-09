print("hello world, desde un script en python3")

# Para ejecutar el script, se debe correr el siguiente comando en la terminal python3 main.py
# o si se encuentra en el directorio donde se encuentra el archivo, se puede ejecutar direct
"""
    Un comentario multilinea

"""
# Variables
# Python es un lenguaje de tipo dinamico
# En python no se necesita declarar el tipo de dato de una variable, el interprete lo hace por nosotros
# Las variables son case sensitive
# Se pueden declarar con comillas simples o dobles
# Se puede concatenar variables con el signo +
# Se pueden declarar varias variables en una sola linea
# Se pueden declarar variables de tipo global y local
# Se pueden declarar variables de tipo constante


# Tipos de datos

var_1 = "Henry" #variable tipo de string
var_2 = 230_000_000 #variable tipo de integer +-
var_3 = 23.5 #variable tipo de float +-
var_4 = True #variable tipo de boolean
var_5 = False #variable tipo de boolean
var_6 = None #variable tipo de None
var_7 = "Henry"

is_active = True
print(is_active)
print(type(is_active))

print(type(var_1))
print(type(var_2))


#Constantes no existe el concepto de constantes pero podemos hacer algo similar  colocando su nombre en mayusculas.
PI = 3.1416
print(PI)
print(type(PI))
# No se puede cambiar el valor de una constante


#Numeros
# Python tiene 3 tipos de numeros
# int
# float
# complex

number = 10
result = number // 25 #Para obtener un resultado sin decimales en una division se usa //
print("El resultado es:", result)

#Operadores Relacionales
# == igual
# != diferente
# > mayor que
# < menor que
# >= mayor o igual que
# <= menor o igual que

number_1 = 10
number_2 = 20
result = number_1 == number_2
print(result)
print(type(result))


#Operadores Logicos
# and -- si o si todas las condiciones deben ser verdaderas para que sea True
# or -- con solo una afirmacion se podra ver que es True
# not -- si negamos verdadero es false y si negamos falso verdadero, sirve para negar un valor boolean
# True -> False | False -> True

number_one = 1
number_two = 2 
result = (True 
          or True 
          and number_1 != number_2 
          and number_1 > 200 
          and number_2 > 200) #Nuestra dos comparaciones deben ser verdaderas 
print(result)


# Pedir Valor por teclado
# input() -> siempre retorna un string
# int() -> convierte un string a un entero
# float() -> convierte un string a un float
# str() -> convierte un entero o float a un string

full_name = input("Ingresa tu nombre ")
print("Hola :", full_name)


# Generar Nuevos tipo de datos
#int - float - str - ==
first_name = input("Ingresa tu nombre: ") #String
edad = int(input("Ingresa tu edad: ")) #Integer
altura = float(input("Ingresa tu altura")) #Float
status = input("Tu usuario se encuentra activo?:  (yes/no)"  ) == "yes" #Boolean

print(first_name)
print(edad)
print(altura)
print(status)

print(
    str("10")
)

#Multiples variables en una sola linea

first_name, age, is_active = "Cody", 23, True # INTENTAR usar la menor cantida de variables por linea de codigo

print(first_name)
print(age)
print(is_active)
