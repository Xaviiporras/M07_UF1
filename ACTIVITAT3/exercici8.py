numsUser = input("Introdueix 10 numeros separats per espais: ")

numsArray = numsUser.split(' ')
arrayFinal = []
sumTotal = 0
mediaTotal = 0

while (len(numsArray) != 10):
    print("Cantidad de numeros incorrecto")
    numsUser = input("Introdueix 10 numeros separats per espais: ")
    numsArray = numsUser.split(' ')

for i in numsArray:
    arrayFinal.append(int(i))

for i in arrayFinal:
    sumTotal+= i

mediaTotal = sumTotal / 10

arrayFinal.append(sumTotal)
arrayFinal.append(mediaTotal)
    
print(f"Numeros de l'usuari: {arrayFinal[0:10]}")
print(f"Suma total: {arrayFinal[10]}")
print(f"Mitjana: {arrayFinal[-1]}")

