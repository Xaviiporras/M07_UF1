divisas = {}    #Inicializamos un diccionario

divisas["Euro"] = "€"   #Le añadimos algunos valores
divisas["Dolar"] = "$"
divisas["Libra"] = "£"

divisaUser = input("Que divisa quiere: ")   #Le pedimos al usuario que introduzca una divisa

if (divisaUser in divisas): #Si la divisa que ha introducido el usurio esta en nuestro diccionario la imprimira por pantalla
    print(divisas[divisaUser])
else:   #En caso de que no este le informara al usuario de que no esta en el diccionario
    print(f"{divisaUser} no esta en el diccionario")
