import random

numRandom = random.randint(1, 100)

numUser = int(input("Introdueix un numero entre 1 y 100: "))

intentos = 1

while (numRandom != numUser):
    if (numRandom < numUser):
        print(f"{numUser} es més gran que el numero secret")
    else:
        print(f"{numUser} es més petit que el numero secret")
    numUser = int(input("Prova de nou: "))
    intentos+= 1

print(f"Enhorabona el numero secret era: {numRandom}")
print(f"Intentos: {intentos}")
    