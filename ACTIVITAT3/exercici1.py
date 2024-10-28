numUser = int(input("Introdueix un numero del 10 al 100: ")) #Le pedimos al usuario qie introduzca un numero del 10 al 100

array = []  #Inicializamos una array

while (numUser > 100 or numUser < 10):  #Hago un bucle que se ejecutara mientras que el usuario no introduzca un valor correcto
    numUser = int(input("Introdueix un numero del 10 al 100: "))
else:
    for i in range(1, numUser+1):
        array.append(i) #En el bucle for vamos añadiendo numeros a la array hasta llegar al numero del usuario
    

myTupla = tuple(array)  #Metemos la array en una tupla

print(myTupla)