from bd import obtener_conexion

def guardar_pedido(id_usuario, carrito):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO pedido_cesta (id_usuario, fecha_registro) VALUES (%s, NOW())", (id_usuario,))
            id_pedido = cursor.lastrowid  
            for item in carrito:
                cursor.execute("""
                    INSERT INTO detalle_cesta (id_pedido, id_producto, cantidad, total)
                    VALUES (%s, %s, %s, %s)
                """, (id_pedido, item['id'], item['quantity'], item['price'] * item['quantity']))
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        conexion.close()
    return id_pedido