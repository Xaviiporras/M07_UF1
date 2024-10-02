userString = input("Introdueix una frase: ")
repetidos = []
stringFinal = ''

for i in range (0, len(userString)):
    char = userString[i]
    if char not in repetidos or char == ' ':
        repetidos.append(char)
        
for i in range (0, len(repetidos)):
    stringFinal = stringFinal + repetidos[i]
        

print(stringFinal)