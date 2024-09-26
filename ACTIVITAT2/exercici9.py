p1 = input("Introdueix la primera paraula: ")
p2 = input("Introdueix la segona paraula: ")

c1 = p1[0:2]
c2 = p2[0:2]

p1 = c2 + p1[2:]
p2 = c1 + p2[2:]

print(p1)
print(p2)