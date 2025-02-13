## Generaremos un programa que donde se genera un numero aleatorio y el usuario debe adivinar el numero segun sea la pista --> Numero magico

from random import randint
number = None
random_number = randint(0,10)

print(random_number)

while number != random_number:
    number = int(
        input("Ingresa un numero: ") #str
    )
    
    if random_number > number:
        print("El numero aleatorio es mayor")
    else:
        print("El numero aleatorio es menor")
else:

    print(f">>> Econtraste el numero {random_number}")