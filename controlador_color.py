from bd import obtener_conexion

def insertar_color(nombre):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO color (nombre) VALUES (%s)",
                       (nombre))
    conexion.commit()
    conexion.close()


def obtener_colores():
    conexion = obtener_conexion()
    colores = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_color, nombre from color")
        colores = cursor.fetchall()            
    conexion.close()
    return colores

def eliminar_color(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM color WHERE id_color = %s", (id))
    conexion.commit()
    conexion.close()


def obtener_color_por_id(id_color):
    conexion = obtener_conexion()
    color = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * from color WHERE id_color = %s", (id_color))
        color = cursor.fetchone()
    conexion.close()
    return color


def actualizar_color(nombre, id_color):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE color SET nombre = %s where id_color = %s ",
                       ( nombre, id_color))
    conexion.commit()
    conexion.close()