#AMB LLISTES
assignatures = ["M1", "M2", "M3", "M4", "M5", "M6"]

notes = []

notes.append(float(input("Nota de M1: ")))
notes.append(float(input("Nota de M2: ")))
notes.append(float(input("Nota de M3: ")))
notes.append(float(input("Nota de M4: ")))
notes.append(float(input("Nota de M5: ")))
notes.append(float(input("Nota de M6: ")))

for i in range (0, len(assignatures)):
    print(f"A {assignatures[i]} ha tret {notes[i]}")

