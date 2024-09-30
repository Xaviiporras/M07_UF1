tuplaMeses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

mesUsuario = int(input("Introduce un numero del 1 al 12 para saber que mes es, si quiere finalizar introduce 0: "))

while (mesUsuario != 0):
    if (mesUsuario < 0 or mesUsuario > 12):
        mesUsuario = int(input("Numero no valido. Introduce un numero del 1 al 12 para saber que mes es, si quiere finalizar introduce 0: "))
    else:
        print(tuplaMeses[mesUsuario-1])
        mesUsuario = int(input("Introduce un numero del 1 al 12 para saber que mes es, si quiere finalizar introduce 0: "))
    
