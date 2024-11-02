import connection as conn

def update(bastidor, matricula=None, marca=None, color=None, nombre_propietario=None, combustible=None):
    connect = conn.get_connection()
    if connect:
        try:
            cursor = connect.cursor()
            updates = []
            values = []
            
            if matricula:
                updates.append("matricula = %s")
                values.append(matricula)
            if marca:
                updates.append("marca = %s")
                values.append(marca)
            if color:
                updates.append("color = %s")
                values.append(color)
            if nombre_propietario:
                updates.append("nombre_propietario = %s")
                values.append(nombre_propietario)
            if combustible:
                updates.append("combustible = %s")
                values.append(combustible)
                
                
            if updates:
                sql = f"UPDATE COCHES SET {', '.join(updates)} WHERE bastidor = %s"
                values.append(bastidor)
                cursor.execute(sql, values)
                connect.commit()
        except Exception as e:
            raise e
        finally:
            cursor.close()
            connect.close()