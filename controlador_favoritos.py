
from bd import obtener_conexion
import base64


def insertar_favorito(id_producto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO favoritos (id_usuario,id_producto) VALUES (13, %s)",
                       (id_producto))
    conexion.commit()
    conexion.close()


def obtener_favoritos():
    conexion = obtener_conexion()
    favoritos = None
    with conexion.cursor() as cursor:
        cursor.execute("""
            SELECT F.id_usuario ,F.id_producto, P.nombre, P.precio, P.vigencia, P.stock, 
                    P.descripcion, P.imagen, TP.nombre AS tipo_producto, 
                    C.nombre as color, TE.nombre AS temporada, 
                    D.tasa AS tasa_descuento 
            FROM favoritos F inner join producto P  on F.id_producto = P.id_producto
            LEFT JOIN tipo_producto TP ON TP.id_tipo = P.id_tipo 
            LEFT JOIN detalle_descuento DD ON DD.id_producto = P.id_producto 
            LEFT JOIN temporada TE ON TE.id_temporada = P.id_temporada 
            LEFT JOIN descuento D ON D.id_descuento = DD.id_descuento 
            LEFT JOIN color C ON C.id_color = P.id_color where id_usuario = 13
        """)
    favoritos = cursor.fetchall()

    # Asegúrate de que favoritos no sea None
    if not favoritos:
        favoritos = []

    favoritos_con_imagen = []
    for producto in favoritos:
        imagen_base64 = base64.b64encode(producto[6]).decode('utf-8')
        tasa_descuento = producto[10] if producto[10] is not None else 0

        vigencia = "Vigente" if producto[3] == 0 else "No vigente" if producto[3] == 1 else "No especificado"

        favoritos_con_imagen.append((
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
    return favoritos_con_imagen

def eliminar_favorito(id_producto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM favoritos WHERE id_producto = %s, id_usuario = ", (id_producto))
    conexion.commit()
    conexion.close()

def alternar_favorito(id_producto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        # Verifica si el producto ya está en los favoritos
        cursor.execute("SELECT * FROM favoritos WHERE id_usuario = 13 AND id_producto = %s", (id_producto,))
        favorito = cursor.fetchone()

        if favorito:
            # Eliminar si ya está en favoritos
            cursor.execute("DELETE FROM favoritos WHERE id_usuario = 13 AND id_producto = %s", (id_producto,))
        else:
            # Insertar si no está en favoritos
            cursor.execute("INSERT INTO favoritos (id_usuario, id_producto) VALUES (13, %s)", (id_producto,))

    conexion.commit()
    conexion.close()