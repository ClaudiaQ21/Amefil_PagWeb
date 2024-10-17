from bd import obtener_conexion

def insertar_pedido(usuario_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO pedido_cesta (usuario_id) VALUES (%s) RETURNING id", (usuario_id,))
        pedido_id = cursor.fetchone()[0]  
    conexion.commit()
    conexion.close()
    return pedido_id

def insertar_detalle_pedido(cantidad, id_producto, id_pedido):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO detalle_cesta (cantidad, id_producto, id_pedido) VALUES (%s, %s, %s)",
                       (cantidad, id_producto, id_pedido))
    conexion.commit()
    conexion.close()