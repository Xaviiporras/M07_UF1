numUser = int(input("Introdueix un numero del 1 al 10: ")) #Le decimos al usuario que introduzca un numero del 1 al 10
resultados = [] #Inicializamos una array
ResultadoFinal = format(numUser)

for i in range (2, 11): #Hacemos un bucle para que calcule la tabla de multiplicar y vamos añadiendo los resultados a la array 'resultados'
    multiplicacion = i * numUser
    resultados.append(multiplicacion)

for i in range (1, len(resultados) + 1):    #Hacemos un for para añadir los resultados en ResultadoFinal y finalmente mostrarlo por pantalla
    if (len(resultados) == i): #Si es el ultimo valor pondra una i en vez de una coma
        ResultadoFinal = ResultadoFinal + ' i ' + format(resultados[i-1])
    else:
        ResultadoFinal = ResultadoFinal + ', ' + format(resultados[i-1])

print(ResultadoFinal)