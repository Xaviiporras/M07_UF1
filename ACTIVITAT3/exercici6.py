areas_pis = ['Menjador', 10.15, 'Rebedor', 9.56, 'Habitació1', 12.34, 'Terrassa', 15.55, 'Lavabo', 7.98, 'Cuina', 12, 'Habitació2', 12.23]

#Segon element
print(areas_pis[1:2])

#Ultim element
print(areas_pis[-1:])

#Area terrassa
print(areas_pis[7:8])

#Imprimir del primer al tercer
print(areas_pis[0:3])

#Imprimir del tercer a l'ultim
print(areas_pis[2:])

#Imprimir el total de l'àrea de les dues habitacions
iHab1 = areas_pis.index('Habitació1')
iHab2 = areas_pis.index('Habitació2')
print(areas_pis[iHab1 + 1] + areas_pis[iHab2 + 1])

#Modificar area lavabo i introduir
iLavabo = areas_pis.index('Lavabo')
areas_pis[iLavabo + 1] = 33.47
print(areas_pis)

#Afegir pati interior i area a ultimes posicions
areas_pis.append("Pati interior")
areas_pis.append(2.78)
print(areas_pis)

#Sumar el total de l'area del pis
areaTotal = 0.0
for i in areas_pis:
    if type(i) == float:
        areaTotal = areaTotal + i
print(areaTotal)
        
