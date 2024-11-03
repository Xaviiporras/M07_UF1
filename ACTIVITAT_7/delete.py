import connection as conn

def delete():
    #Establece la conexión
    connect = conn.get_connection()
    if connect:
        try:
            cursor = connect.cursor()
            #Le pedimos al usuario el numero de bastidor que desea eliminar
            primary_key = input("Introduce el numero de bastidor del registro que desea eliminar: ")
            #Generamos la consulta sql
            sql = f"DELETE FROM COCHES WHERE bastidor = {primary_key}"
            #Ejecutamos la consulta sql y guardamos los datos en la base de datos
            cursor.execute(sql)
            connect.commit()
            
        except Exception as e:
            
            print(f"No se ha podido eliminar el registro: {e}")
        finally:
            #Cerramos la conexión
            cursor.close()
            connect.close()