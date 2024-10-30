import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            database="postgres",
            user='user_postgres',
            password='pass_postgres',
            host='localhost',
            port='5432'
        )
        connection = conn.cursor()
        return connection
    except Exception as e:
        print(f"No se ha podido establecer la conexión: {e}")
    finally:
        connection.close()