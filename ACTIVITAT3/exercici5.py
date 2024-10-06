userString = input("Introdueix una frase: ")    #Le pedimos al usuario que introduzca una frase
repetidos = []  #Inicializamos array donde iremos añadiendo los caracteres
stringFinal = ''    #Inicializamos String donde ira el resultado final

for i in range (0, len(userString)):    #Bucle for donde recorreremos cada caracter de la frase
    char = userString[i]
    if char not in repetidos or char == ' ':    #Si el caracter no esta en la array repetidos la añadimos
        repetidos.append(char)
        
for i in range (0, len(repetidos)): #Vamos añadiendo los valores de la array repetidos en el stringFinal
    stringFinal = stringFinal + repetidos[i]
        

print(stringFinal)