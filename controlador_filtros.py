from bd import obtener_conexion

def obtener_tipo_producto ():
    conexion = obtener_conexion()
    tipo_pro = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * from tipo_producto")
        tipo_pro = cursor.fetchall()
    conexion.close()
    return tipo_pro

def obtener_temporadas():
    conexion = obtener_conexion()
    temporada = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * from temporada")
        temporada = cursor.fetchall()
    conexion.close()
    return temporada

def obtener_colores():
    conexion = obtener_conexion()
    color =[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * from color")
        color = cursor.fetchall()
    conexion.close()
    return color