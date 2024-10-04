divisas = {}

divisas["Euro"] = "€"
divisas["Dolar"] = "$"
divisas["Libra"] = "£"

divisaUser = input("Que divisa quiere: ")

if (divisaUser in divisas):
    print(divisas[divisaUser])
else:
    print(f"{divisaUser} no esta en el diccionario")
