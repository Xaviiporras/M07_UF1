numsUsuari = input("Introduce 10 numeros separados por espacios: ") #Le decimos al usuario que introduzca 10 numeros

numsSplit = numsUsuari.split(' ')   #Separamos los numeros y ahora estan en una array
arrayFinal = []

for i in range (1, len(numsSplit) + 1): #Hacemos un bucle para añadir los numeros en otra array para que sean int, ya que antes eran Strings
    arrayFinal.append(int(numsSplit[i - 1]))

arrayFinal.sort()   #Ahora que son numeros los ordenamos
tupla = tuple(arrayFinal)   #Los metemos en una tupla

print(tupla)    #Imprimimos la tupla