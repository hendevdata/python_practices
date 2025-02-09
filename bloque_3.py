# Tuplas 
# Las tuplas no son mutables o inmutables --> es decir no se pueden modificar--> se quedara asi por el resto del programa

# Un ejemplo de uso puede ser los datos apra conectarnos a una base de datos


# 0, 1,2 --> Recuerda usar los indices apra ahcer consultas
settings = ("localhost", 3306, True)

print(settings)
print(type(settings))

print(settings[0])
print(settings[1])
print(settings[2])

# Indices negativos 
print(settings[-3])
print(settings[-2])
print(settings[-1])


#settings[0] = "no se puede cambiar perro"
#Se usan para motivos y razones de lecturas

# Crear Tuplas
# Se pueden crear tuplas vacias
# Se pueden crear tuplas con un solo elemento
# Se pueden crear tuplas con varios elementos
# Se pueden crear tuplas con diferentes tipos de datos

numbers = 1 ,2 ,3 ,4 ,5 # tupla
print(type(numbers))

# Se pueden crear tuplas de un elemento siempre colocando una coma al final

numbers_1 = 1,
print(type(numbers_1))

#Desempaquetando Tuplas
# Se pueden desempaquetar tuplas
# Se pueden desempaquetar tuplas con un solo elemento
# Se pueden desempaquetar tuplas con varios elementos


courses = ("Python", "Django", "Flask", "Ruby", "Java")
print(courses)
print(type(courses))

# Como ahcer si tenemos esta tupla y queremos almacenar cada uno de los elementos en diferentes variables. 

#var_1 = courses[0]
#var_2 = courses[1]
#var_3 = courses[2]
#var_4 = courses[3]
#var_5 = courses[4]

var1, _, var3, var4, _ = courses[0], courses[1], courses[2], courses[3], courses[4]
var1, var2, var3, var4, var5 = courses



print(var1, var2 , var3, var4, var5)


# Desempaquetado de tuplas 2
# Seguiremos trabajando con la tupla courses
# se usa la convencion del _ para indicar que no se va a usar esa variable --> el Guion Bajo es una convencion no una palabra regitrada en python
# Se puede usar el guion bajo para indicar que no se va a usar una variable
# *var --> se usa para indicar que se va a almacenar el resto de los elementos en una variable

var1, var2, *var = courses
print(var1)
# Ejemplos de uso de * en las tuplas

# Ejemplo 1: Agrupar elementos en una tupla usando *
numbers = 1, 2, 3, 4, 5
*first_numbers, last_number = numbers
print(first_numbers)  # Output: [1, 2, 3, 4]
print(last_number)  # Output: 5

# Ejemplo 2: Desempaquetar una tupla y agrupar elementos usando *
courses = ("Python", "Django", "Flask", "Ruby", "Java")
first_course, *middle_courses, last_course = courses
print(first_course)  # Output: Python
print(middle_courses)  # Output: ['Django', 'Flask', 'Ruby']
print(last_course)  # Output: Java

# Ejemplo 3: Agrupar elementos en una tupla usando *
numbers = 1, 2, 3, 4, 5
first_number, *remaining_numbers = numbers
print(first_number)  # Output: 1
print(remaining_numbers)  # Output: [2, 3, 4, 5]


# Funcion ZIP
# Se pueden combinar tuplas usando la funcion zip
# Se pueden combinar tuplas con diferentes tamaños
# Se usa para agrupar los valores seguun sus indices

users = ("Henry", "Juan", "Carlos")
courses_zip = ("Python", "Django", "Flask", "Ruby", "Java")
score = [10,8,7,9,10]

repose = tuple(zip(users, courses_zip, score))
print(repose)

# Ejemplo de uso de zip
# Ejemplo 1: Combinar dos tuplas
users = ("Henry", "Juan", "Carlos")
courses = ("Python", "Django", "Flask")
result = tuple(zip(users, courses))
print(result)  # Output: (('Henry', 'Python'), ('Juan', 'Django'), ('Carlos', 'Flask'))

# Funciones de las Tuplas

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(numbers)) # Para saber la longitud de una tupla
print(sorted(numbers)) # Para ordenar una tupla (de menor a mayor)
print(sorted(numbers, reverse=True)) # Para ordenar una tupla (de mayor a menor)
print(numbers.count(5)) # Para contar cuantas veces se repite un elemento en una tupla
print(3 in numbers) # Para saber si un elemento esta en una tupla
print(numbers.index(3)) # Para saber el indice de un elemento en una tupla