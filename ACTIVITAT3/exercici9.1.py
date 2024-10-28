#AMB DICCIONARIS
assignatures = ["M1", "M2", "M3", "M4", "M5", "M6"] #Hacemos una array con las asignaturas

notas = {}  #Inicializamos un diccionario

for i in assignatures:  #Hacemos un bucle que le ira pidiendo al usuario que introduzca la nota de cada asignatura
    nota = float(input(f"Nota de {i}: "))
    notas[i] = nota #Aqui añade la nota y la asignatura al diccionario

for i, nota in notas.items():   #Hacemos un bucle para imprimir todas las notas y asignaturas
    print(f"A {i} ha tret {nota}")