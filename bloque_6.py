# Ciclos y Condiciones

## None--> Ausencia de Valor --> este representa un alto nivel de abstraccion
## Get -->  Nos permite tener el valor de una llave, si no existe puede retornar None

user = None # --> Ausencia de valor --> es una abstraccionq ue representa nada --> == Null or Nil
## es importante ya que nos dejara condicionar ciertos bloques

print(user)


# Valores Falsos

## True --> Objetos Verdadero
## False --> Objetos Falso 
## Es importane mencionar que existen otros objetas que permiten representar Verdadero o falso
## Es Posible representar valores falsos con lo siguiente
## --> "", '', 0, 0.0, False, (), [], {},  NONE --> Falsos
## --> Cualquier objeto que no este en la lista superior  sera considerado True



## IF palabra reservada
## Estructura -- Es importante tener en cuenta la identacion usando 4 espacios o un tab
'''
if <bool (True)>: # se esjecuta si el valor bool es verdadero
    print("Hola Mundo)
    print("Estamos haciendo el curso de python)

'''

## Ejemplo 

number_one = 10
number_two = 20


if number_one == 10 and number_two == 20 or (number_one > number_two) : # Se ejecutara si el valor es verdadero
    print("hola, la condicion es True")
    print("Nos encontramos en el bloque de if")

print("Fin del Programa")  ## Este print como no se encuentra identado, no le pertenece al if
## Recuerda que la identacion sirve para agregar funcionalidad al if

value = "cody" # Si la variable esta vacia --> False

## --> "", '', 0, 0.0, False, (), [], {},  NONE --> Falsos
if value: ## --> Verificamos que tiene valor, se podria negar usando not
    print(">>> La variable tiene valor")
print("Fin del programa")

## Else: 
if not value: ## --> Verificamos que tiene valor, se podria negar usando not
    print(">>> La variable tiene valor")
else: 
    print(">>> Lo sentimos la condicion no se cumple") ## Sirve para generar comportamientos si el la primera condicion no se cumple
    print(">>> Este bloque se ejecuta si la condicion no se cumple")
print("Fin del programa")


## Condiciones Anidadas
## Condiciones que se encuentran dentro de otras condiciones
## If anidados

number_one =  10
number_two = 20

if number_one >= 10:
    print(">>> Number one es mayor o igual a 10")
    ## Se puede seguir condicionando las N cantidades anidadas
    ## En la medida de lo posible evitar las condiciones anidadas para mayor legibilidad
    
    if number_one > number_two:
        print(" number one es mayor a number two ")
        
    else:
        print(">>> number one no es mayor a number two")
   
        
## Elif --> nor permite agregar N catidad de condiciones
## Parecido al switch case

## --> Semaforo.py # Implementar condiciones anidadas puede ocacionar problemas

color = input(">>> De que color esta la luz del semaforo? ")

if color == "Verde":
    print('>>> Puedes Avanzar')

elif color == "Amarillo":
    print(">>> Alto Parcial")
    
elif color == "Rojo":
    print(">>> Alto Total")
else: 
    print(">>> El color no es valido")
# Elif se ejecuta de manera descendente, si la primera condicion se ejecuta, no se continua
print(">>> Fin del programa")

## Match --> estructura de control

score = 4
'''
match score:
    case 10: 
        print(">>>  Muchas Felicidades tu calificacion es 10")
    case 9 | 8: 
        print(">>> Felicidades tu calificacion es aprobatoria")
    case 6 | 7: 
        print(">>> Bien hecho, aprobaste")
    case _:
        print(">>> Lo siento reprobaste")
print(">>> Fin del programa")
'''


## Operador Ternario
## Sirve para poder llevar acabo operaciones en una sola linea de codigo

score = 5

## One Liner
## Operador Ternario 
## En Otros lenguajes de programacion se usa el operado ?
## Se pueden Agregar difierentes condiciones al one liner
message = "Aprobaste la mate" if score > 5 else "No aprobaste"
print(message)


## For each
## while
## Nos permite iterar sobre cada uno de los elementos de una coleccion y en esta se pueden obtener cada uno de los valores de los elementos

numbers = [10, 20, 30, 40, 50]
numbers_t = (23, 23 ,23 ,23)
message = "Hola Mundo"
user = {
    "user": "Henry",
    "age": 30,
    "password": "pass123"
}

'''
for <variable> esta va almacenar los elementos de la coleccion 
in <collection>: 
    bloque
'''
for number in numbers:
    print(">>> Hola nos encontramos en un nuevo bloque:", number)
print(">>> Fin del programa")


## Desempaquetado de tuplas
for key, value in user.items():
    print(">>> La llave es", key, "El valor es", value)
## El ciclo for each terminara cuando este paso hasta el ultimo elemento



## Puede causar un cilo infinito
## No es recomendable usar el metodo .append() en un for each
## Se recomienda usar tuplas ante otro tipo de colecciones
'''
numbers_app = [1, 2, 3]

for i in numbers_app:
    numbers_app.append(10)
'''

## Funcion Range
## Nos permite generar un rango de numeros enteros
## Normalmente es una coleccion
## El rango por default es 0
## Range (start, stop + 1)

number = 0

for number in range(10): # quiero una coleccion del 0 al numero 9
    print(number)
    
for number in range(5,11): # Se suma uno para que vaya de 5 - 10
    print(number)
    
## Se puede usar range para iterar colecciones

courses = ["Python", "Go", "Java"]

for index in range(len(courses)): 
    print(courses[index])
    
## Se recomienda usar  el ciclo for  each y no usando indices
for course in courses: 
    print(courses)
    
    
## Ciclo While Parte 1
## For each & While

'''
while <condicion>:
    bloque
'''

counter = 0
while counter < 10:
    print("valor", counter)
    #counter = counter + 1 ## Se agrega para evirtar que itere
    counter += 1 ## Mucho mas legible
    
## El cilo while no es la mejor opcion --> lo usamos si no sabemos cuantas iteraciones vamos a realizar
for counter in range(0,10):
    print(counter)
    
    
number = int(input("Ingrese en consola el numero "))
counter_l = 0 

while number > 0: 
    number = number // 10 ## Se divide sobre 10, el punto decimal se va corriendo
    counter_l += 1
print("La cantidad de digitos es:", counter_l)

## Continue & Break
## Nos permite saltarnos una iteracion o detener esta misma

for number in range(1,101): ## Se hace un for con range() para obtener numeros del 1 - 10
    if number % 2 == 0 : # Se busca que no se ejecute o se salta los numeros pares
        continue ## Palabra reservada para que haga estos saltos
    if number == 7:
        break ## Rompe el ciclo for
    print(number)
    
## La palabra break nos permite finalizar de forma abrupta

## Pass --> Palabra reservada --> Bloques vacios

var = None

if var == None:
    pass ## Con esto le indicamos a Python que el bloque esta vacio y no hara nada
    ... ## Se pueden usar elipsis
