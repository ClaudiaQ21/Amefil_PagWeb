from bd import obtener_conexion

def insertar_descuento(tasa, fecha_inicio, fecha_fin, vigencia):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO descuento (tasa, fecha_inicio, fecha_fin, vigencia) VALUES (%s, %s, %s, %s)",
                       (tasa, fecha_inicio, fecha_fin, vigencia))
    conexion.commit()
    conexion.close()


def obtener_descuentos():
    conexion = obtener_conexion()
    descuentos = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_descuento, tasa, fecha_inicio, fecha_fin, vigencia FROM descuento")
        descuentos = cursor.fetchall()
    conexion.close()
    return descuentos


def obtener_descuentos_vigentes(): ### CBOX
    conexion = obtener_conexion()
    descuentos = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_descuento, tasa FROM descuento where vigencia=0")
        descuentos = cursor.fetchall()
    conexion.close()
    return descuentos


def eliminar_descuento(id_descuento):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM descuento WHERE id_descuento = %s", (id_descuento))
    conexion.commit()
    conexion.close()


def obtener_descuento_por_id(id_descuento):
    conexion = obtener_conexion()
    descuento = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM descuento WHERE id_descuento = %s", (id_descuento))
        descuento = cursor.fetchone()
    conexion.close()
    return descuento


def actualizar_descuento(tasa, fecha_inicio, fecha_fin, vigencia, id_descuento):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE descuento SET tasa = %s, fecha_inicio = %s, fecha_fin = %s, vigencia = %s WHERE id_descuento = %s",
                       (tasa, fecha_inicio, fecha_fin, vigencia, id_descuento))
    conexion.commit()
    conexion.close()

def contardescuento():
    conexion = obtener_conexion()
    contador = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(id_descuento) FROM descuento")
        contador = cursor.fetchone()
    conexion.close()
    return contador

def asignardescuento(id_producto,id_descuento):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO detalle_descuento (id_producto, id_descuento) VALUES (%s, %s)", (id_producto, id_descuento))
    conexion.commit()
    conexion.close()

def editarasignar(id_producto, id_descuento):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE detalle_descuento SET id_descuento=%s WHERE id_producto=%s", (id_descuento, id_producto))
    conexion.commit()
    conexion.close()

def eliminarasignar(id_producto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM detalle_descuento WHERE id_producto=%s", (id_producto))
    conexion.commit()
    conexion.close()