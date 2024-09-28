valorUsuari = float(input("Introdueix un valor en € ")) #Es fa un input perquè el usuari introdueixi el valor que desitji
ivaUsuari = int(input("Introdueix el IVA que vols aplicar (4%, 10%, 21%) ")) #Es fa un input perquè el usuario introdueix el IVA que vol

while(ivaUsuari != 4 and ivaUsuari != 10 and ivaUsuari != 21):  #Es fa un bucle que entrara si el usuari no posa el IVA correctament
    print("Has introduit un valor pel IVA que no es correcte")
    ivaUsuari = input("Introdueix el IVA que vols aplicar (4%, 10%, 21%) ") #Li demana el IVA una altra vegada
    
resultat = valorUsuari - (valorUsuari * ivaUsuari / 100) #Calculem el resultat
print(f"Valor introduit pel usuari: {valorUsuari}")
print(f"Valor de l'IVA introduit pel usuari: {ivaUsuari}")
print(f"Resultat amb l'IVA aplicat: {resultat}")


    