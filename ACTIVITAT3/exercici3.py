numUser = int(input("Introdueix un numero del 1 al 10: "))
resultados = []
ResultadoFinal = format(numUser)

for i in range (2, 11):
    multiplicacion = i * numUser
    resultados.append(multiplicacion)

for i in range (1, len(resultados) + 1):
    if (len(resultados) == i):
        ResultadoFinal = ResultadoFinal + ' i ' + format(resultados[i-1])
    else:
        ResultadoFinal = ResultadoFinal + ', ' + format(resultados[i-1])

print(ResultadoFinal)