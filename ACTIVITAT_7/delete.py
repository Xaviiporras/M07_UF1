import connection as conn

def delete():
    connect = conn.get_connection()
    if connect:
        try:
            cursor = connect.cursor()
            primary_key = input("Introduce el numero de bastidor del registro que desea eliminar: ")
            
            sql = f"DELETE FROM COCHES WHERE bastidor = {primary_key}"
            
            cursor.execute(sql)
            connect.commit()
            
        except Exception as e:
            
            print(f"No se ha podido eliminar el registro: {e}")
        finally:
            cursor.close()
            connect.close()