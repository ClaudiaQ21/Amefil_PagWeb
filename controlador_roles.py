from bd import obtener_conexion

def insertar_tipo_usuario(nombre):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO tipo_usuario (nombre) VALUES (%s)", (nombre,))
    conexion.commit()
    conexion.close()

def obtener_tipos_usuario():
    conexion = obtener_conexion()
    tipos = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_tipo, nombre from tipo_usuario")
        tipos = cursor.fetchall()            
    conexion.close()
    return tipos

def obtener_tipos_usuario_vigentes(): ### CBOX
    conexion = obtener_conexion()
    tipos = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_tipo, nombre from tipo_usuario where estado=0")
        tipos = cursor.fetchall()            
    conexion.close()
    return tipos

def eliminar_tipo_usuario(id_tipo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM tipo_usuario WHERE id_tipo = %s", (id_tipo,))
    conexion.commit()
    conexion.close()

def obtener_tipo_usuario_por_id(id_tipo):
    conexion = obtener_conexion()
    tipo = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_tipo, nombre from tipo_usuario WHERE id_tipo = %s", (id_tipo,))
        tipo = cursor.fetchone()
    conexion.close()
    return tipo

def actualizar_tipo_usuario(nombre, id_tipo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE tipo_usuario SET nombre = %s WHERE id_tipo = %s", (nombre, id_tipo))
    conexion.commit()
    conexion.close()
