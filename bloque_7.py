# Bloque Laboratorio

'''
Se debe crear una lista  longitud 10. Utilizando un ciclo for each 
imprime en consola todos los numeros pares mayor al 5, la lista debe tener por nonombre,
my_list
'''

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in my_list: # se crea una variable temporal llamada numero para almacenar la siguiente operacion
    if numero > 5 and numero % 2 == 0:
        print (numero)

## busquemos lo numeros pares mayor a 2

for numero_ in my_list: 
    if numero_ > 2 and numero_ % 2 == 0 :
        print(numero_)      
        
        
##  Se require que se cree una variable llamada sentence y que se cree un while que lo que haga es que contabilice cuantos caracteres hay hata el primer punto

sentence =  "Hola Pedro. Espero estes bien"  # Varible de tipo str

contador = 0 # se inicia un contador para llevar la cuenta de los caracteres --> parecido a las variables temporales de el ejemplo anterior

while contador < len(sentence) and sentence[contador] != ".": # Se hace un cilo while para recorrenr la cadena de text
    contador += 1
print (contador)



## --> Funciones
## >>> Es de sumas importaciona, seremos capaces de cambiar de paradigma
## >>> Por ejemplo, programacion funcional o POO
## ... Implementar otros paradigmas de lenguaje
## Nos permite abstraer o reutilizar codigo
## Estructura -->
'''
def <nombre de la funcion> --> snake_case(parametros--> son Opcionales, N catidad):
'''

##Ejemplo -->

def say_goodbye():
    print("Terminamos el Script")

def hello():
    print("Hola mundo desde una funcion")
    

for _ in range(10): ## Se crea un for each con un rango de 10 reoeticiones y al finalizar se llama a la funcion say_goodbye()
    hello()
say_goodbye()

## --> Los parametros

    # Parametros
    # Son varialbes que podemos utilizar en el bloque de la funcion
    # Los parametros son usados para poder validar valores de entrada
    

def count_to(number): # Los parametros son variables que podemos utilizar dentro del bloque de la funcion
    for n in range(1, number + 1):# Hacemos storage con una variable temporal n y agreganmos el parametro dentro de range >>> Llamamos a la funcion con el parametro 10
        print(n)
count_to(10) # Iteramos 10 veces, #Argumento

def multiply(number1, number2): 
    result = number1 * number2 # Se plantea la operacion matematica
    print(f" El resultado de la operacion es: {result}") # Se crea un F string para concatenar valores dinamicos
    
multiply(10, 20) # Recuerda siempre pasar los argumentos

def full_name(first_name, last_name, prefix):
    full_name = f"{prefix} {first_name} {last_name}"
    print(full_name)
full_name(
    "Henry",
    "Larreal",
    "Mr."
)

# Retornar Valores
# Las funciones son vistas como cajas negras
# Nuetras funciones hasta ahora se apoyan en print
# Lo ideal seria crear funciones que tengan una sola accion 
# Cundo python ejecuta el return  finaliza la funcion  
    

def multiply(number1, number2): 
    result = number1 * number2 
    return result 
result = multiply (10, 20)
print(result - 76)
    
def full_name(first_name, last_name, prefix):
    full_name = f"{prefix} {first_name} {last_name}"
    return full_name
user_full_name = full_name("Henry" , "Larreal", "Mr")
print(f"El nombre del usuario es {user_full_name}")

## --> Sample

def user_name_1(name, sur_name, nick_name):
    full_name_1 = f"{name} {sur_name} and the nickname of this user is: {nick_name}"
    print("Fin del script")
    return full_name_1
full_user_name_1 = user_name_1("Henry", "Larreal", "Arkosi")
print(full_user_name_1)

## --> Sample  2

def division(number_one, number_two):
    if number_one == 0 or number_two == 0:
        return None
    # return division --> corto
    return number_one / number_two
print(
    division(10, 2)
)


## --> Retornar Valores


def foo():
    return "Ark", True, 12 # python va a agrupas estos valores en una tupla

result =  foo()
print(result)
print(type(result))

user_name, active, age  = foo() # Desempaquetado de tuplas 
print(user_name, active, age)




