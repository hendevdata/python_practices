# Diccionarios

# Es otra estructura de datos que nos [ermite almacenar multiples valores]

# Losdiccionarios trabajancon el concepto, llave: valor

# clave : valor o llaves : valores

user = {
    'name': 'Nombre del usuario',
    'age': 30,
    'email': 'this is the mail'
}

# Los diccionarios se pueden anidar y son inmutables
# Strings, tuplas int, float, booleanos, diccionarios son inmutables y pueden ser usados como llaves de un diccionario
# Los diccionarios pueden almacenar todo tipo de datos
# Las llaves son unicas en los dioccionarios, es decir este no puede tener dos llaves iguales y tomara la ultima llave que se haya ingresado

user_1 = {
    'nombre': 'Nombre del usuario',
    'age': 30,
    'email': 'this is the mail',
    'lenguajes': ['Python', 'Java', 'JavaScript'],
    'settings' : ('color', 'blue')
}

print(user_1)

# Llaves de diccionarios
# en python conq ue se cumpla la regla con llave valor es suficiente, sin embargo es poco legible
# ES POSIBLE USAR FUNCIONES DENTRO DE LOS DICCIONARIOS COMO LLAVES
# Puede que los diccionarios sean el objeto mas versatil y usados en python


user_2 = {
    "name": 'Cody',
    20: 30,
    True: 'this is the mail',
    (1,2): ['Python', 'Java', 'JavaScript'],
}

# Obtener valores de un diccionario

print(
    'nombre' in user_1, # --> True
)

# Se puede usar la palabra reservada in para verificar si una llave existe en un diccionario este generara un valor booleano
print(
    "phone" in user_1, # --> False
)

#print(name["age"]) # --> 30


# Metodo get --> Se usa para obtener un valor de un diccionario
# SI la llave no existe en el diccionario, el metodo get devolvera None

user_name = user_2.get('name', 'Lo siento el valor no existe') # --> 'Henry', el segundo valor sirve para dar un valor por si la informacion no existe
print(user_name)

# Los diccionarios son objetos mutables

user_2["Last Name"] = "Larreal" # sirve para agregar un valor al diccionario, queda en el ultimo puesto 
print(user_2)

# Llaves , Valores y Pares

#  Metodos Keys, Values and Items --> son metodos que nos permiten saber sus valores, llaves y  Items

print(
    list(user_1.keys()) # Nos da el valor de todas las llaves del diccionario y se trnasforma en una lista
)

print(
    tuple(user_1.keys()) # Nos da el valor de todas las llaves del diccionario y se transforma en una tupla
)

print(
list(user_1.values()) # Nos da el valor de todas las llaves del diccionario
)

print(
    list(user_1.items()) # Nos da el valor en una lista de tuplas --> Es una buena practica simpre trabajar estos metodos para hacerlo mas legibles
)


# Actualiar diccionarios --> se pueden modificar en tiempo de ejecucion ya que  los diccionarios son objetos mutables


print(
    len(user_2) # Se puede usar para ver cuantos apres de llaves hay en el diccionario
)

# Actaulizamos el nombre
user_2["name"]  = "Codigo"
print(user_2)
print(len(user_2))

user_2["Last Name"] = "Facilito"
user_2["Perro"] = "Criollo"
print(len(user_2))
print(user_2)

# Metodo Update

user_2.update({
    "Carro" : 'Twingo'
    "Color Favorito"
})