from bd import obtener_conexion

def insertar_temporada(nombre):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO temporada (nombre) VALUES (%s)",
                       (nombre))
    conexion.commit()
    conexion.close()


def obtener_temporadas():
    conexion = obtener_conexion()
    temporadas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * from temporada")
        temporadas = cursor.fetchall()            
    conexion.close()
    return temporadas

def eliminar_temporadas(id_temporada):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM temporada WHERE id_temporada = %s", (id_temporada))
    conexion.commit()
    conexion.close()


def obtener_temporada_por_id(id_temporada):
    conexion = obtener_conexion()
    temporada = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * from temporada WHERE id_temporada = %s", (id_temporada))
        temporada = cursor.fetchone()
    conexion.close()
    return temporada


def actualizar_temporada(nombre, id_temporada):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE temporada SET nombre = %s where id_temporada = %s ",
                       ( nombre, id_temporada))
    conexion.commit()
    conexion.close()