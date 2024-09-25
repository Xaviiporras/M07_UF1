valorUsuari = int(input("Introdueix un valor en € "))
ivaUsuari = int(input("Introdueix el IVA que vols aplicar (4%, 10%, 21%) "))

while(ivaUsuari != 4 and ivaUsuari != 10 and ivaUsuari != 21):
    print("Has introduit un valor pel IVA que no es correcte")
    ivaUsuari = input("Introdueix el IVA que vols aplicar (4%, 10%, 21%) ")
    
resultat = valorUsuari - (valorUsuari * ivaUsuari / 100)

print(f"Valor introduit pel usuari: {valorUsuari}")
print(f"Valor de l'IVA introduit pel usuari: {ivaUsuari}")
print(f"Resultat amb l'IVA aplicat: {resultat}")


    