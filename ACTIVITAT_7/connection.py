import psycopg2

def get_connection():
    try:
        connection = psycopg2.connect(
            database="postgres",
            user='user_postgres',
            password='pass_postgres',
            host='localhost',
            port='5432'
        )
        return connection
    except Exception as e:
        print(f"No se ha podido establecer la conexión: {e}")
    finally:
        connection.close()