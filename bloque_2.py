#Listas--> es una estructura de datos o colleccion que nos permite gestionar varios tipos de datos, como str, bools, int



"""_summary_
    <variable = []
    """


my_list = ["string", True, 3.14, [1, 2, 3]]

print(my_list)    
print(type(my_list))

# Buenas practicas --> trabajar con listas homogenias o que usen un tipo de dato
# Las listas son mutables y se rigen por los indices es decir el primer elemento es  0

cursos = ["Python", "Django", "Flask", "Ruby"]
numeros = [1, 2, 3, 4]

print(cursos)
print(numeros)

# Los indices son sumamente importantes para saber trabajar con listas.
# El  indice se maneja desde el numero 0 y el ultimo suele ser el -1
# Se puede sar el metodo len()
# Se puede usar el metodo append() para agregar al final
# se podria impirmir por consola el ultimo valor utilizadon len -1 quedaria --> value = cursos([len(cursos)) - 1]
# Se podria obtener el ultimo index utilizadon numeros negativos
# Usando los indices se pueden cambiar los valores de las listas
# Todas las listas poseen indices para su facil manejo, recuerda usar numeros negaticos para la optimizacion de las busquedas

cursos[-1] = "MongoDB" # Se pueden actualizar usando los indices sin mbargo se podria usar  el metodo append() o el metodo pop() para eliminar usando los indices


value = cursos[-1]
print(
    value
)

value = cursos[len(cursos) - 1]
print(
    value
)



# Sublistas --> usando Slicing

# creamos una sublista que tenga los primeros 3 elementos originales

new_list = [
    cursos[0],
    cursos[1],
    cursos[2]
]

print(new_list)


new_list_slicing = cursos[:3] # Se puede usar el metodo slicing para obtener sublistas, es la buena practia para reducir la busqueda
# Se debe mirar y tomar en cuenta sumar uno mas cuando se hace el slicing ya que solo toma 3 elementos

new_list_negative = cursos[:-2]
print(new_list_negative)


complete_list = cursos[:] # Se puede obtener una copia completa de la lista --> ShallowCopy
print(complete_list)

cursos_lista_skips = cursos[::2] # Aca se esta haciendo un ShalloCopy y se estan haciendo saltos de 2 indices
print(cursos_lista_skips)

# Metodos de las listas
# append() --> agrega un elemento al final de la lista
# insert() --> agrega un elemento en un indice especifico
# remove() --> elimina un elemento de la lista
# pop() --> elimina el ultimo elemento de la lista
# clear() --> elimina todos los elementos de la lista
# index() --> devuelve el indice de un elemento
# count() --> devuelve la cantidad de veces que se repite un elemento
# sort() --> ordena la lista
# reverse() --> invierte la lista
# copy() --> devuelve una copia de la lista
# extend() --> extiende la lista con otra lista
# count() --> devuelve la cantidad de veces que se repite un elemento
# Las listas son mutables, se pueden incrementar o decrecer, en tiempos de ejecucion se pueden modificar los valores de las listas



cursos.append("Go")  # Append sirve para agregar informacion al final de la lista
cursos.append("PHP")
cursos.append("Laravel") 

print(cursos)
print(len(cursos))

#Metodo Insert

cursos.insert(0,"Rust") # el metodo insert utiliza primero un numero entero para definir el index en donde agregara la informacion.
cursos.insert(4,"C#")

print(cursos)


# Metodo Extend

new_cursos = ["React", "Next"] # Este agrega una lista a otra pero al final
cursos.extend(new_cursos)
print(cursos)

print(#palabra reservada in para poder ver si el streing esta dentro de la coleccion
    "Python" in cursos
)

print(
    cursos.index("Python")
)


# Metodos que nos permite quitar elementos de una coleccion.

cursos.remove("Python") # Elimina el primer elemento que coincida con el valor
cursos.pop() #Extrae el ultimo elemento y lo imprime


first_element = cursos.pop(0)

print(cursos)

print(first_element)

#cursos.clear()# Elimina todos los elementos de la lista

# Copy 
# reverse
# sort

cursos_copy = cursos[:] # Shallow copy
print(cursos_copy)
cursos_copy_1 = cursos.copy() # obtendiamos una copia

# Rever list sin el metodo
# cursos_copy = cursos_copy[::-1] --> se esta usando slicing

# Reverse, se inviertan las listas usando este metodo

cursos_copy_1.reverse()
print(cursos_copy_1)


# Sort

cursos_copy_1.sort() # Ordena la lista de forma ascendente
print(cursos_copy_1)
cursos_copy_1.sort(reverse=True) # Ordena la lista de forma descendente



# Matrices --> Genramos 3x3 --> una matriz de dos dimensiones

#3x3
matrix = [
    [1,2,3], #Index 0
    [4,5,6], #Index 1
    [7,8,9] #Index 2
]

print(matrix)

print(
    matrix[2][2] # El primer valor es para buscar el index de la lista y el segundo es para bsucar el index dentro de la lista
)

#  CREA UNA matrix 3x3 y verifica si el rpimer valor es par 
# si es par imprime la matriz
# si no es par imprime la matriz invertida
# Crear una matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Verificar si el primer valor es par
if matriz[0][0] % 2 == 0:
    # Imprimir la matriz si el primer valor es par
    for fila in matriz:
        print(fila)