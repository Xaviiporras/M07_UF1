diccicionario = {}
nomUser = input("Introdueix un nom: ")
edatUser = input("Introdueix la seva edat: ")

while nomUser != '':
    if nomUser in diccicionario:
        print(nomUser + " ya esta en el diccionario y no se volvera a añadir")
    diccicionario[nomUser] = edatUser
    nomUser = input("Introdueix un nom: ")
    edatUser = input("Introdueix la seva edat: ")
    
print(diccicionario)
    