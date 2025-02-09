numbers = [1,2,3]
print(numbers[0] + numbers[-1])

print(numbers[0] + numbers[1] + numbers[2])

strings_list = [
	"uno",
    "dos",
  	"tres",
  	"cuatro",
  	"cinco",
  	"seis",
  	"siete",
  	"ocho",
  	"nueve",
  	"diez"
]

sublista = strings_list[:3] + strings_list[-3:]
print(sublista)

if "CodigoFacilito" in strings_list:
    print("Existe")
else:
    print("No existe")
    
    
matrix = [
    [2, 5, 8],
    [4, 1, 7],
    [6, 3, 9]
]
todos_pares = True

for fila in matrix:
    if fila[0] % 2 != 0 :
        todos_pares = False
        break
print(todos_pares)



lista = [1,2,3,4,5,6,7,8,9,10]
pares = tuple(num for num in lista if num % 2 == 0)
print(pares)