abecedario = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

abecedarioFiltrado = []

for i in range(len(abecedario)):
    
    if ((i+1) % 3) != 0:
         abecedarioFiltrado.append(abecedario[i])
         
print(abecedarioFiltrado)

tupla = tuple(abecedarioFiltrado)

print(tupla)