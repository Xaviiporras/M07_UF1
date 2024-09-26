paraules = input("Introdueix entre 1 y 3 paraules separades per espais: ")

p = paraules.split(" ")

if (len(p) == 1):
    p1 = p[0]
    c1 = p1[0:1]
    print('Paraula: ' + p1 + ' Caracters: ' + format(len(p1)) + ' Primer caracter: ' + c1)
    
if (len(p) == 2):
    p1 = p[0]
    c1 = p1[0:1]
    print('Paraula: ' + p1 + ' Caracters: ' + format(len(p1)) + ' Primer caracter: ' + c1)
    p2 = p[1]
    c2 = p2[0:1]
    print('Paraula: ' + p2 + ' Caracters: ' + format(len(p2)) + ' Primer caracter: ' + c2)
    
if (len(p) == 3):
    p1 = p[0]
    c1 = p1[0:1]
    print('Paraula: ' + p1 + ' Caracters: ' + format(len(p1)) + ' Primer caracter: ' + c1)
    p2 = p[1]
    c2 = p2[0:1]
    print('Paraula: ' + p2 + ' Caracters: ' + format(len(p2)) + ' Primer caracter: ' + c2)
    p3 = p[2]
    c3 = p3[0:1]
    print('Paraula: ' + p3 + ' Caracters: ' + format(len(p3)) + ' Primer caracter: ' + c3)

