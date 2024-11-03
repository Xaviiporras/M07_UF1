import connection as conn

def update(bastidor, matricula=None, marca=None, color=None, nombre_propietario=None, combustible=None):
    #Creo la conexión
    connect = conn.get_connection()
    if connect:
        try:
            cursor = connect.cursor()
            # Almacena las columnas a actualizar
            updates = []
            # Almacena los valores correspondientes
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
                #Creo la consulta introduciendole los updates con comas entre ellos
                sql = f"UPDATE COCHES SET {', '.join(updates)} WHERE bastidor = %s"
                values.append(bastidor)
                #Ejecuto la consulta y guardo los cambios
                cursor.execute(sql, values)
                connect.commit()
        except Exception as e:
            raise e
        finally:
            #Cierro la conexión
            cursor.close()
            connect.close()