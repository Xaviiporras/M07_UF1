import connection as conn

def create(matricula, marca, color, nombre_propietario, combustible):
    # Obtiene la conexión a la base de datos
    connect = conn.get_connection()
    
    if connect:
        try:
            # Crea un cursor para ejecutar el SQL
            cursor = connect.cursor()
            # Creo la consulta sql
            sql = f"""
                INSERT INTO COCHES (matricula, marca, color, nombre_propietario, combustible)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (matricula, marca, color, nombre_propietario, combustible)
            #Ejecuto la consulta sql con los valores que se han pasado por parametros
            cursor.execute(sql, values)
            # Guarda los cambios en la base de datos
            connect.commit()
        except Exception as e:
            raise e
        
        finally:
            #Cerramos la conexión
            cursor.close()
            connect.close()
        