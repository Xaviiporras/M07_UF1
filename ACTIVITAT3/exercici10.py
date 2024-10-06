abecedario = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

abecedarioFiltrado = [] #Se iran guardando en esta array las letras que nos interesan

for i in range(len(abecedario)):    #Hacemos un for que ira añadiendo las letras a la array 'abecedarioFiltrado'
    
    if ((i+1) % 3) != 0:    #En caso de que i+1 / 3 su restante sea diferente de 0 añadira esa letra al abecedarioFiltrado
         abecedarioFiltrado.append(abecedario[i])
         
print(abecedarioFiltrado)   #Imprime el abecedarioFiltrado como array

tupla = tuple(abecedarioFiltrado)   #Pasa la array a una tupla

print(tupla)    #Imprime la tupla