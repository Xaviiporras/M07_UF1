import connection
import create_table
import create
import delete
import read
import update

def main():
    bool_main = True
    while bool_main:
        eleccion = input("Elige que quieres hacer (create, read, update, delete, exit): ")
        
        if eleccion == 'create':
            matricula = input('Introduce la matrícula del vehículo: ')
            marca = input('Introduce la marca del vehículo: ')
            color = input('Introduce el color del vehículo: ')
            nombre_propietario = input('Introduce el nombre del propietario: ')
            combustible = input('Introduce el tipo de combustible: ')
            create.create(matricula, marca, color, nombre_propietario, combustible)
        
        elif eleccion == 'read':
            read.read()
            
        elif eleccion == 'update':
            bastidor = int(input("Introduce el bastidor del vehículo que quieres actualizar: "))
            
            matricula = input("Nueva matrícula (dejar vacío para no actualizar): ") or None
            marca = input("Nueva marca (dejar vacío para no actualizar): ") or None
            color = input("Nuevo color (dejar vacío para no actualizar): ") or None
            nombre_propietario = input("Nuevo nombre del propietario (dejar vacío para no actualizar): ") or None
            combustible = input("Nuevo tipo de combustible (dejar vacío para no actualizar): ") or None
            
            update.update(bastidor, matricula, marca, color, nombre_propietario, combustible)
            
        elif eleccion == 'delete':
            delete.delete()
            
        elif eleccion == 'exit':
            print("Finalitzant CRUD")
            bool_main = False
        else:
            print("Error: Seleccione una de las opciones")

main()