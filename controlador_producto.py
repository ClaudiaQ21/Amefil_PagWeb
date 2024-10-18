from bd import obtener_conexion
import base64


def insertar_producto(nombre, precio, id_tipo, vigencia, stock, descripcion, id_color, id_temporada, imagen):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO producto ( nombre, precio, id_tipo, vigencia, stock, descripcion, id_color, id_temporada, imagen) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (nombre, precio, id_tipo, vigencia, stock, descripcion, id_color, id_temporada, imagen))
    conexion.commit()
    conexion.close()


def obtener_productos():
    conexion = obtener_conexion()
    productos = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT P.id_producto, P.nombre, P.precio, P.vigencia, P.stock, P.descripcion, P.imagen, TP.nombre AS tipo_producto, C.nombre as color,TE.nombre AS temporada, D.tasa AS tasa_descuento FROM producto P LEFT JOIN tipo_producto TP ON TP.id_tipo = P.id_tipo LEFT JOIN detalle_descuento DD ON DD.id_producto = P.id_producto LEFT JOIN temporada TE ON TE.id_temporada = P.id_temporada LEFT JOIN descuento D on D.id_descuento = DD.id_descuento LEFT JOIN color C on C.id_color = P.id_color")
        productos = cursor.fetchall()
    productos_con_imagen = []
    for producto in productos:
        imagen_base64 = base64.b64encode(producto[6]).decode('utf-8')
        productos_con_imagen.append((
            producto[0],  # id_producto
            producto[1],  # nombre
            producto[2],  # precio
            producto[3],  # vigencia
            producto[4],  # stock
            producto[5],  # descripcion
            imagen_base64,  # imagen convertida a Base64
            producto[7],  # coleccion
            producto[8],  # color
            producto[9],  # temporada
            producto[10]  # descuento
        ))
            
    conexion.close()
    return productos_con_imagen

def eliminar_producto(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM producto WHERE id_prodcuto = %s", (id))
    conexion.commit()
    conexion.close()


def obtener_producto_por_id(id_producto):
    conexion = obtener_conexion()
    producto = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT P.id_producto, P.nombre, P.precio, P.vigencia, P.stock, P.descripcion, P.imagen, TP.nombre AS tipo_producto, C.nombre as color,TE.nombre AS temporada, D.tasa AS tasa_descuento, TA.nombre AS talla FROM producto P LEFT JOIN tipo_producto TP ON TP.id_tipo = P.id_tipo LEFT JOIN detalle_descuento DD ON DD.id_producto = P.id_producto LEFT JOIN temporada TE ON TE.id_temporada = P.id_temporada LEFT JOIN talla TA ON TA.id_talla = P.id_talla LEFT JOIN descuento D on D.id_descuento = DD.id_descuento LEFT JOIN color C on C.id_color = P.id_color WHERE P.id_producto = %s", (id_producto))
        producto = cursor.fetchone()
    conexion.close()
    return producto


def actualizar_producto(nombre, precio, id_tipo, vigencia, stock, descripcion, id_color, id_temporada, imagen, id_producto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE producto SET nombre = %s, precio = %s, id_tipo = %s, vigencia = %s, stock = %s, descripcion = %s, id_color = %s, id_temporada = %s, imagen = %s where id_producto = %s ",
                       ( nombre, precio, id_tipo, vigencia, stock, descripcion, id_color, id_temporada, imagen, id_producto))
    conexion.commit()
    conexion.close()