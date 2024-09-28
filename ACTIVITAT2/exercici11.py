multiplicador = int(input("Introdueix el multiplicador: "))

for i in range(1, 11):  #Fem un bucle for que recorri del 1 fins al 10
    result = multiplicador * i  #Multipliquem el numero de l'usuari amb el del bucle
    print(f"{i} * {multiplicador} = {result}")  #El mostrem per pantalla