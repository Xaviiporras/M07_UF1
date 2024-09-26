numUsuari = int(input("Introdueix un numero: "))

total = 0

for i in range (1, numUsuari+1):
    total+= i

print(f"El total de la suma de todos los numeros desde el 1 es: {total}")