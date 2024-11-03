import create
import delete
import read
import update

def main():
    #Variable que detendra el bucle
    bool_main = True
    
    #Este bucle se ejecutara hasta que el boleano este en False
    while bool_main:
        #Depende de lo que introduzca el usuario se ejecutara una cosa o otra
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
            #En caso que no se introduzca nada se pondra el valor en None
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
            #Sale del bucle al poner el booleano en false
            bool_main = False
        else:
            print("Error: Seleccione una de las opciones")

main()