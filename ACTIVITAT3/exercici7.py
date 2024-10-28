diccicionario = {}  #Inicializamos un diccionario
nomUser = input("Introdueix un nom: ")  #Le pedimos al usuario que introduzca un nombre
edatUser = input("Introdueix la seva edat: ")   #Le pedimos al usuario que introduzca la edad del nombre que ha introducido

while nomUser != '':    #El bucle se ejecutara mientras que el nombre sea diferente a ''
    if nomUser in diccicionario:    #En caso que el nombre ya este en el diccionario imprimimos un mensaje
        print(nomUser + " ya esta en el diccionario y no se volvera a añadir")
    diccicionario[nomUser] = edatUser   #Introducimos el nombre y la edad en el diccionario y despues le pedimos otro nombre y edad al usuario
    nomUser = input("Introdueix un nom: ")
    edatUser = input("Introdueix la seva edat: ")
    
print(diccicionario)    #Cuando sale del bucle imprime el diccionario
    