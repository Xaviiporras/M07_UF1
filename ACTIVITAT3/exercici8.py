numsUser = input("Introdueix 10 numeros separats per espais: ") #Se le pide al usuario que introduzca  10 numeros

numsArray = numsUser.split(' ') #Separamos los numeros
arrayFinal = []
sumTotal = 0
mediaTotal = 0

while (len(numsArray) != 10): #Se ejecutara mientras la longitud de numsArray sea diferente de 10
    print("Cantidad de numeros incorrecto")
    numsUser = input("Introdueix 10 numeros separats per espais: ")
    numsArray = numsUser.split(' ')

for i in numsArray: #Hacemos un for para añadir los numeros de la array a otra array pero como int
    arrayFinal.append(int(i))

for i in arrayFinal:    #hacemos un for para calcular la suma total de los numeros
    sumTotal+= i

mediaTotal = sumTotal / 10  #Calculamos la media

arrayFinal.append(sumTotal) #Añadimos la suma total y la media al final de la array
arrayFinal.append(mediaTotal)
    
print(f"Numeros de l'usuari: {arrayFinal[0:10]}")   #Imprimimos los numeros que ha puesto el usuario, la suma total y la media
print(f"Suma total: {arrayFinal[10]}")
print(f"Mitjana: {arrayFinal[-1]}")

