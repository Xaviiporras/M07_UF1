import connection as conn

def read():
    connect = conn.get_connection()
    if connect:
        try:
            cursor = connect.cursor()
            sql = "SELECT * FROM COCHES"
            
            cursor.execute(sql)
            
            records = cursor.fetchall()
            for i in records:
                print(i)
                
        except Exception as e:
            raise e
        finally:
            cursor.close()
            connect.close()