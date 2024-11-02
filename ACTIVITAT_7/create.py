import connection as conn

def create(bastidor, matricula, marca, color, nombre_propietario, combustible):
    connect = conn.get_connection()
    
    if connect:
        try:
            cursor = connect.cursor()
            sql = f"""
                INSERT INTO COCHES (bastidor, matricula, marca, color, nombre_propietario, combustible)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (bastidor, matricula, marca, color, nombre_propietario, combustible)
            cursor.execute(sql, values)
            connect.commit()
        except Exception as e:
            raise e
        
        finally:
            cursor.close()
            connect.close()
        