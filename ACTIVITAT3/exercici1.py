numUser = int(input("Introdueix un numero del 10 al 100: "))

array = []

while (numUser > 100 or numUser < 10):
    numUser = int(input("Introdueix un numero del 10 al 100: "))
else:
    for i in range(1, numUser+1):
        array.append(i)
    

myTupla = tuple(array)

print(myTupla)