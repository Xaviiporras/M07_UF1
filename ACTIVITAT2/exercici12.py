numUsuari = int(input("Introdueix un numero: "))

total = 0   #Inicialitzem la variable que finalment mostrarem per pantalla

for i in range (1, numUsuari+1):    #Fem un bucle que sigui desde el 1 fins el numero que ha introduit l'usuari
    total+= i   #Cada vegada que comença el bucle es va sumant la variable 'i' sobre si mateixa

print(f"El total de la suma de todos los numeros desde el 1 es: {total}")