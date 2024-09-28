paraules = input("Introdueix entre 1 y 3 paraules separades per espais: ")

p = paraules.split(" ") #Amb el split es crea una array

if (len(p) == 1):   #Aixo s'executa en cas que la array tingui nomes una paraula
    p1 = p[0]    #Guardem en p1 la primera paraula de la array
    c1 = p1[0:1]    #Guardem a la variable c1 el primer caracter de la primera paraula
    print('Paraula: ' + p1 + ' Caracters: ' + format(len(p1)) + ' Primer caracter: ' + c1)
    
if (len(p) == 2):   #Aixo s'executa en cas que la array tingui 2 paraules
    p1 = p[0]
    c1 = p1[0:1]
    print('Paraula: ' + p1 + ' Caracters: ' + format(len(p1)) + ' Primer caracter: ' + c1)
    p2 = p[1]    #Guardem en p2 la segona paraula de la array
    c2 = p2[0:1]    #Guardem a la variable c2 el primer caracter de la segona paraula
    print('Paraula: ' + p2 + ' Caracters: ' + format(len(p2)) + ' Primer caracter: ' + c2)
    
if (len(p) == 3):   #Aixo s'executa en cas que la array tingui 3 paraules
    p1 = p[0]
    c1 = p1[0:1]
    print('Paraula: ' + p1 + ' Caracters: ' + format(len(p1)) + ' Primer caracter: ' + c1)
    p2 = p[1]
    c2 = p2[0:1]
    print('Paraula: ' + p2 + ' Caracters: ' + format(len(p2)) + ' Primer caracter: ' + c2)
    p3 = p[2]    #Guardem en p3 la tercera paraula de la array
    c3 = p3[0:1]    #Guardem a la variable c3 el primer caracter de la tercera paraula
    print('Paraula: ' + p3 + ' Caracters: ' + format(len(p3)) + ' Primer caracter: ' + c3)

