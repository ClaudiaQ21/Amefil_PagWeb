from bd import obtener_conexion
import base64


def insertar_producto(nombre, precio, id_tipo, vigencia, stock, descripcion, id_color, id_temporada, imagen):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO producto ( nombre, precio, id_tipo, vigencia, stock, descripcion, id_color, id_temporada, imagen) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (nombre, precio, id_tipo, vigencia, stock, descripcion, id_color, id_temporada, imagen))
    conexion.commit()
    conexion.close()


def obtener_productos(busqueda=None):
    conexion = obtener_conexion()
    productos = None
    with conexion.cursor() as cursor:
        if busqueda is not None:
            cursor.execute("""
                SELECT P.id_producto, P.nombre, P.precio, P.vigencia, P.stock, 
                       P.descripcion, P.imagen, TP.nombre AS tipo_producto, 
                       C.nombre as color, TE.nombre AS temporada, 
                       D.tasa AS tasa_descuento 
                FROM producto P 
                INNER JOIN tipo_producto TP ON TP.id_tipo = P.id_tipo 
                LEFT JOIN detalle_descuento DD ON DD.id_producto = P.id_producto 
                INNER JOIN temporada TE ON TE.id_temporada = P.id_temporada 
                LEFT JOIN descuento D ON D.id_descuento = DD.id_descuento 
                INNER JOIN color C ON C.id_color = P.id_color 
                WHERE P.nombre LIKE %s
            """, ('%' + busqueda + '%',))
        else:
            cursor.execute("""
                SELECT P.id_producto, P.nombre, P.precio, P.vigencia, P.stock, 
                       P.descripcion, P.imagen, TP.nombre AS tipo_producto, 
                       C.nombre as color, TE.nombre AS temporada, 
                       D.tasa AS tasa_descuento 
                FROM producto P 
                INNER JOIN tipo_producto TP ON TP.id_tipo = P.id_tipo 
                LEFT JOIN detalle_descuento DD ON DD.id_producto = P.id_producto 
                INNER JOIN temporada TE ON TE.id_temporada = P.id_temporada 
                LEFT JOIN descuento D ON D.id_descuento = DD.id_descuento 
                INNER JOIN color C ON C.id_color = P.id_color
            """)
        productos = cursor.fetchall()

    if not productos:
        productos = []

    productos_con_imagen = []
    for producto in productos:
        imagen_base64 = base64.b64encode(producto[6]).decode('utf-8')
        tasa_descuento = producto[10] if producto[10] is not None else 0

        vigencia = "Vigente" if producto[3] == 0 else "No vigente" if producto[3] == 1 else "No especificado"

        productos_con_imagen.append((
            producto[0],  # id_producto
            producto[1],  # nombre
            producto[2],  # precio
            vigencia,     # vigencia
            producto[4],  # stock
            producto[5],  # descripcion
            imagen_base64, # imagen convertida a Base64
            producto[7],  # coleccion
            producto[8],  # color
            producto[9],  # temporada
            tasa_descuento  # descuento
        ))
    conexion.close()
    return productos_con_imagen

def contar_productos():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(id_producto) from producto")
        cantidad = cursor.fetchone()
    conexion.close
    return cantidad

def obtener_producto_segun_tipo(id_tipo):
    conexion = obtener_conexion()
    productos = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT P.id_producto, P.nombre, P.precio, P.vigencia, P.stock, P.descripcion, P.imagen, TP.nombre AS tipo_producto, C.nombre as color,TE.nombre AS temporada, D.tasa AS tasa_descuento, P.id_tipo FROM producto P INNER JOIN tipo_producto TP ON TP.id_tipo = P.id_tipo LEFT JOIN detalle_descuento DD ON DD.id_producto = P.id_producto INNER JOIN temporada TE ON TE.id_temporada = P.id_temporada LEFT JOIN descuento D on D.id_descuento = DD.id_descuento INNER JOIN color C on C.id_color = P.id_color WHERE P.id_tipo = %s", (id_tipo))
    productos = cursor.fetchall()

    if not productos:
        productos = []

    productos_tipo_imagen = []
    for producto in productos:
        imagen_base64 = base64.b64encode(producto[6]).decode('utf-8')
        tasa_descuento = producto[10] if producto[10] is not None else 0

        vigencia = "Vigente" if producto[3] == 0 else "No vigente" if producto[3] == 1 else "No especificado"

        productos_tipo_imagen.append((
            producto[0],  # id_producto
            producto[1],  # nombre
            producto[2],  # precio
            vigencia,     # vigencia
            producto[4],  # stock
            producto[5],  # descripcion
            imagen_base64, # imagen convertida a Base64
            producto[7],  # coleccion
            producto[8],  # color
            producto[9],  # temporada
            tasa_descuento,  # descuento
            producto[11] #id_tipo_producto
        ))
    conexion.close()
    return productos_tipo_imagen

def eliminar_producto(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM producto WHERE id_producto = %s", (id))
    conexion.commit()
    conexion.close()

def dar_baja_producto(id_producto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE producto SET vigencia = 1 WHERE id_producto = %s", (id))
    conexion.commit()
    conexion.close()


def obtener_producto_por_id(id_producto):
    conexion = obtener_conexion()
    producto = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT P.id_producto, P.nombre, P.precio, P.vigencia, P.stock, P.descripcion, P.imagen, TP.nombre AS tipo_producto, C.nombre as color,TE.nombre AS temporada, D.tasa AS tasa_descuento FROM producto P INNER JOIN tipo_producto TP ON TP.id_tipo = P.id_tipo LEFT JOIN detalle_descuento DD ON DD.id_producto = P.id_producto INNER JOIN temporada TE ON TE.id_temporada = P.id_temporada LEFT JOIN descuento D on D.id_descuento = DD.id_descuento INNER JOIN color C on C.id_color = P.id_color WHERE P.id_producto = %s", (id_producto))
        producto = cursor.fetchone()
    producto_imagen = []
    imagen_base64 = base64.b64encode(producto[6]).decode('utf-8')
    tasa_descuento = producto[10] if producto[10] is not None else 0

    vigencia = "Vigente" if producto[3] == 0 else "No vigente" if producto[3] == 1 else "No especificado"

    producto_imagen.append((
        producto[0],  # id_producto
        producto[1],  # nombre
        producto[2],  # precio
        vigencia,     # vigencia
        producto[4],  # stock
        producto[5],  # descripcion
        imagen_base64, # imagen convertida a Base64
        producto[7],  # coleccion
        producto[8],  # color
        producto[9],  # temporada
        tasa_descuento  # descuento
    ))

    conexion.close()
    return producto_imagen


def actualizar_producto(nombre, precio, id_tipo, vigencia, stock, descripcion, id_color, id_temporada, imagen, id_producto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE producto SET nombre = %s, precio = %s, id_tipo = %s, vigencia = %s, stock = %s, descripcion = %s, id_color = %s, id_temporada = %s, imagen = %s where id_producto = %s ",
                       ( nombre, precio, id_tipo, vigencia, stock, descripcion, id_color, id_temporada, imagen, id_producto))
    conexion.commit()
    conexion.close()

def obtener_novedades():
    conexion = obtener_conexion()
    productos = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT P.id_producto, P.nombre, P.precio, P.vigencia, P.stock, P.descripcion, P.imagen,DATEDIFF(CURDATE(), P.fecha_registro) AS dias_registro, TP.nombre AS tipo_producto, C.nombre as color,TE.nombre AS temporada, D.tasa AS tasa_descuento FROM producto P INNER JOIN tipo_producto TP ON TP.id_tipo = P.id_tipo LEFT JOIN detalle_descuento DD ON DD.id_producto = P.id_producto INNER JOIN temporada TE ON TE.id_temporada = P.id_temporada LEFT JOIN descuento D on D.id_descuento = DD.id_descuento INNER JOIN color C on C.id_color = P.id_color")
        productos = cursor.fetchall()
    productos_nuevos = []
    for producto in productos:
        imagen_base64 = base64.b64encode(producto[6]).decode('utf-8')

        tasa_descuento = producto[10] if producto[10] is not None else 0

        if producto[3] == 0:
            vigencia = "Vigente"
        elif producto[3] == 1:
            vigencia = "No vigente"
        else:
            vigencia = "No especificado"
        
        productos_nuevos.append((
            producto[0],  # id_producto
            producto[1],  # nombre
            producto[2],  # precio
            vigencia,  # vigencia
            producto[4],  # stock
            producto[5],  # descripcion
            imagen_base64,  # imagen convertida a Base64
            producto[7], #dias de registro
            producto[8],  # coleccion
            producto[9],  # color
            producto[10],  # temporada
            tasa_descuento  # descuento
        ))
            
    conexion.close()
    return productos_nuevos


def obtener_limit():
    conexion = obtener_conexion()
    productos = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_producto, imagen, vigencia FROM producto LIMIT 8")
        productos = cursor.fetchall()  # Lista de productos (tuplas)
    
    producto_limit = []
    
    for producto in productos:
        # Verificamos si la imagen (LONGBLOB) no es None o vacía
        if producto[1]:
            imagen_base64 = base64.b64encode(producto[1]).decode('utf-8')
        else:
            imagen_base64 = None  # Si no hay imagen, se asigna None

        # Manejamos la vigencia según el valor de producto[2]
        vigencia = "Vigente" if producto[2] == 0 else "No vigente" if producto[2] == 1 else "No especificado"

        # Añadimos los detalles del producto a la lista
        producto_limit.append((
            producto[0],  # id_producto
            imagen_base64,  # imagen codificada en base64
            vigencia,      # vigencia
        ))

    conexion.close()
    return producto_limit