from bd import obtener_conexion

def insertar_tipo_producto(nombre):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO tipo_producto (nombre) VALUES (%s)", (nombre))
    conexion.commit()
    conexion.close()

def obtener_tipo_productos():
    conexion = obtener_conexion()
    tipos = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_tipo, nombre from tipo_producto")
        tipos = cursor.fetchall()            
    conexion.close()
    return tipos

def obtener_tipo_productos_vigentes(): ### CBOX
    conexion = obtener_conexion()
    tipos = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_tipo, nombre from tipo_producto where estado=0")
        tipos = cursor.fetchall()            
    conexion.close()
    return tipos

def eliminar_tipo(id_tipo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM tipo_producto WHERE id_tipo = %s", (id_tipo))
    conexion.commit()
    conexion.close()

def obtener_tipo_por_id(id_tipo):
    conexion = obtener_conexion()
    tipo = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_tipo, nombre from tipo_producto WHERE id_tipo = %s", (id_tipo))
        tipo = cursor.fetchone()
    conexion.close()
    return tipo

def actualizar_tipo_producto(nombre, id_tipo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE tipo_producto SET nombre = %s WHERE id_tipo = %s", (nombre, id_tipo))
    conexion.commit()
    conexion.close()

def contartipo():
    conexion = obtener_conexion()
    contadort = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(id_tipo) from tipo_producto")
        contadort = cursor.fetchone()            
    conexion.close()
    return contadort