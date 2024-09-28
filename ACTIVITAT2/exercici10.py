import random

numRandom = random.randint(1, 100) #Generem un numero aleatori entre 1 i 100

numUser = int(input("Introdueix un numero entre 1 y 100: "))

intentos = 1 

while (numRandom != numUser):   #El bucle s'executara mentre que el numero de l'usuari sigui diferen al random
    if (numRandom < numUser):   #En cas que el numero del usuari sigui més gran s'executa la primera linea, en cas contrari la segona
        print(f"{numUser} es més gran que el numero secret")
    else:
        print(f"{numUser} es més petit que el numero secret")
    numUser = int(input("Prova de nou: "))
    intentos+= 1    #Es suma 1 intent per cada vegada que l'usuari fica un numero i no es correcte

print(f"Enhorabona el numero secret era: {numRandom}")
print(f"Intentos: {intentos}")
    