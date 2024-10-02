numsUsuari = input("Introduce 10 numeros separados por espacios: ")

numsSplit = numsUsuari.split(' ')
arrayFinal = []

for i in range (1, len(numsSplit) + 1):
    arrayFinal.append(int(numsSplit[i - 1]))

arrayFinal.sort()
tupla = tuple(arrayFinal)

print(tupla)