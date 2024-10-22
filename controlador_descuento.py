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