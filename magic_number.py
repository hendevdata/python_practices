## Generaremos un programa que donde se genera un numero aleatorio y el usuario debe adivinar el numero segun sea la pista --> Numero magico

from random import randint ## Importamos las funciones random para generar un rando de numeros aleatorios
number = None ## Definimos el numero a comprar
random_number = randint(0,10) ## Generamos el rango de numeros aleatorios

#print(random_number)

while number != random_number: ## Mientras el numero sea diferente al que genera  randint
    number = int(
        input("Ingresa un numero: ") #str
    )
    
    if random_number > number: # Pistas --> numero mayor
        print("El numero aleatorio es mayor")
    else:
        print("El numero aleatorio es menor")
else:

    print(f">>> Econtraste el numero {random_number}")