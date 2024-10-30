import psycopg2 as pg
import connection as conn

def create_table():
    
    connection = conn.get_connection
    if connection:
        try:
            cursor = connection.cursor()
            query = f"""CREATE TABLE COCHES(
                bastidor SERIAL PRIMARY KEY,
                matricula VARCHAR(20),
                marca VARCHAR(20),
                color VARCHAR(20),
                nombre_propietario VARCHAR(20),
                combustible VARCHAR(20)
            )"""
            
            cursor.execute(query)
            connection.commit()
        except Exception as e:
            print(f"Error al crear la tabla: {e}")
        finally:
            cursor.close()
            connection.close()
    