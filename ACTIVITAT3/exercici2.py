tuplaMeses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
#Le decimos al usuario que introduzca un numero del 1 al 12
mesUsuario = int(input("Introduce un numero del 1 al 12 para saber que mes es, si quiere finalizar introduce 0: "))
#El bucle se ejecutara mientras que el usuario ponga un numero diferente a 0
while (mesUsuario != 0):
    if (mesUsuario < 0 or mesUsuario > 12): #Se ejecutara en caso de que el usuario ponga un numero no valido
        mesUsuario = int(input("Numero no valido. Introduce un numero del 1 al 12 para saber que mes es, si quiere finalizar introduce 0: "))
    else:
        print(tuplaMeses[mesUsuario-1]) #Mostramos por pantalla el mes que ha elegido el usuario y luego le decimos que introduzca otro numero
        mesUsuario = int(input("Introduce un numero del 1 al 12 para saber que mes es, si quiere finalizar introduce 0: "))
    
