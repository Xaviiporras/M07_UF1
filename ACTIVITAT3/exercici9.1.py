#AMB DICCIONARIS
assignatures = ["M1", "M2", "M3", "M4", "M5", "M6"]

notas = {}

for i in assignatures:
    nota = float(input(f"Nota de {i}: "))
    notas[i] = nota

for i, nota in notas.items():
    print(f"A {i} ha tret {nota}")