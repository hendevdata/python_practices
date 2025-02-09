# Strings
# Los strings son coleciones inmutables al igualq ue las tuplas, unas vez creemos un string quedara asi por el resto del programa
# Se usaran los strings solo para motivos de lectura

message = "Hola Mundo!" # Coleccion de caracteres, solo se puede agregar o quitar caracteres
print(message)
print(type(message))
print(len(message)) # Longitud de la cadena de caracteres
print("!" in message) # Para saber si un caracter esta en la cadena de caracteres
print("0" in message) # Para saber si un caracter no esta en la cadena de caracteres
print(message[0]) # Para saber el primer caracter de la cadena de caracteres
print(message.index("M")) # Para saber la posicion de un caracter en la cadena de caracteres

# Es posible crear sub strings

message_2 = message[0:4] # Hola, creada a partir del slicing
print(message_2)

# Strings como listas
# Split --> Va a generar a partir de un string una lista de strings
# Join --> Va a generar a partir de una lista de strings un string

cursos = "Python, php, java, c++, ruby"
list_cursos = cursos.split(", ") # Se va a dividir el string por los espacios
print(cursos)
print(list_cursos)

# Metodo join

courses_join = ["Python", "php", "java", "c++", "ruby"]
message_join = " ".join(courses_join) # Se va a unir la lista de strings en un solo string
print(message_join)

# Generar nuevos strings a partir de otros strings

name = "Henry"
last_name = "Larreal"

# string_full_name = name + " " + last_name --> se usan para unir strings
full_name = name + " " + last_name # Agregar un espacio entre los strings para que se vea mejor--> los espacios son caracteres validos en un string
print(full_name)
# No se pueden concatenar strings con numeros pero se podria usar el metodo str() para convertir un numero a string

full_name = name + " " + last_name  + " " + str (30)
print(full_name)

# Se podria usar el metodo join para unir strings
full_name_join = " ".join([name, last_name, str(30)]) # Se va a unir la lista de strings en un solo string
print(full_name_join)

# (%S) --> Se usa para concatenar strings   (%d) --> Se usa para concatenar numeros enteros
# --> Es normal verlo en versiones antiguas de python y en logs

full_name_s = "%s %s" % (name, last_name) # 
print(full_name_s)

# Metodo format --> Se usa para concatenar strings

base = "El nombre completo es: {name} {last_name}. soy un programador de {age} años" #--> {} Valores dinamicos
full_name_format = base.format(name=name, last_name=last_name, age=30)
print(full_name_format)

#Ejemplo de concatenacion de strings

name = input("Ingresa tu nombre: ")
last_name = input("Ingresa tu apellido: ")
age = input("Ingresa tu edad: ")

full_name_format = base.format(name = name,last_name = last_name,age = age)
print(full_name_format)

# F-strings --> Se usa para concatenar strings
# --> Es la forma mas moderna de concatenar strings
name_f = "Henry"
last_name_f = "Larreal"
full_name_f = f'El nombre completo es: {"Henry"} {last_name}. soy un programador de {10 + 20} años' # los F string s nos permite la interpolacion en tiempos de ejecucion
print(full_name_f) # Se puede usar cualquier tipo de operacion en los F 

# Funcion print --> Sirve para imprimir valores
# Se puede usar para imprimir cualquier tipo de valor
print(name_f, last_name_f, 30) # Se pueden imprimir varios valores a la vez y se puede agregar espacios para mayor legibilidad
# Se puede usar para imprimir cualquier tipo de valor y combinar con strings y variables
print("Hola", name_f, last_name_f, "como estas?", sep=" !!!") # Se puede agregar un separador para que se vea mejor, este se puede modificar para agregar cualquier tipo de valor como espaciado.

# Busquedas en lISTAS

title = "Curso de Python 3"
# se debe estandarizar con el metodo lower para poder hacer busquedas
# Ya que python es case sensitive
print(
    title.lower(), # Para convertir un string en minusculas
)

# Metodo upper
print(
    
    title.upper(), # Para convertir un string en mayusculas
)


print(
    'Python' in title, # Para saber si un caracter esta en la cadena de caracteres
    # En en caso que se usen las mismas palabras pero en minusculas en  aca es valor es False
)
# Metodo count
print(
    title.count('u'), # Para saber cuantas veces se repite un caracter en la cadena de caracteres
)

# Metodo starts with
print(
    title.startswith("Curso"), # Para saber si la cadena de caracteres empieza con un caracter
)

# Metodo endswith
print(
    title.endswith("3"), # Para saber si la cadena de caracteres termina con un caracter
)

# Metodo de lISTAS  --> para poder generar busquedas en listas siempre es bueno estandarizar los valores con el metodo lower

title_listas = "Curso de Python 3"


print(
    title_listas.upper() # Para convertir un string en mayusculas
)

print(
    title_listas.lower() # Para convertir un string en minusculas
)

print(
    title_listas.strip() # Para eliminar los espacios en blanco al inicio y al final de la cadena de caracteres
)

print(
    title_listas.find("P") # Para saber si la cadena de caracteres termina con un caracter
)

'''print(
    title_listas[7] # Para saber si la cadena de caracteres termina con un caracter)
print("6".isnumeric()) # Para saber si un caracter es un numero
name = "henry"
print(name.capitalize()) # Para convertir la primera letra de un string en mayuscula

print(name[0].upper() + name[1:]) # Para convertir la primera letra de un string en mayuscula
'''