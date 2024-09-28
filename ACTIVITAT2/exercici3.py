#Li demanem dos valors al usuari 
valor1 = float(input("Introdueix el valor 1: "))
valor2 = float(input("Introdueix el valor 2: "))

#En cas de que el valor 1 sigui major al valor 2 es quedara al primer print del contrari anira al segon
if (valor1 > valor2):
    print(f"El valor més gran es {valor1}")
else:
    print(f"El valor més gran es {valor2}")