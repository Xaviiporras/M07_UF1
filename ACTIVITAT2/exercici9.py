p1 = input("Introdueix la primera paraula: ")
p2 = input("Introdueix la segona paraula: ")

c1 = p1[0:2]    #Guardem en c1 els dos primers caracter de la paraula1
c2 = p2[0:2]    #Guardem en c2 els dos primers caracter de la paraula2

p1 = c2 + p1[2:]    #Li afegim els dos primers caracters de la paraula2 a la paraula1 i a la paraula 1 li treiem els dos primers caracters
p2 = c1 + p2[2:]    #Li fem el mateix que a la de dalt pero a la inversa

print(p1)
print(p2)