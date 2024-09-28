#Li demanem un valor al usuari
valor1 = float(input("Introdueix un numero: "))

#Utilitzem el '%' per obtenir el residu de la divisió
result = valor1 % 2

#En cas de que el residu sigui 0 el numero sera parell, del contrari sera senar
if (result == 0):
    print("El numero introduit es parell")
else:
    print("El numero introduir es senar")
