# controlador_direccion.py

from flask import jsonify
from bd import obtener_conexion

def obtener_direcciones():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_direccion, nombre, referencia FROM direccion")
        direcciones = cursor.fetchall()
    conexion.close()
    return direcciones

def obtener_direccion_completa():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("select dir.id_direccion, dir.nombre, dir.referencia, dis.id_distrito, dis.nombre, pro.id_provincia, pro.nombre, depa.id_departamento, depa.nombre from direccion dir inner join distrito dis on dir.id_distrito = dis.id_distrito inner join provincia pro on dis.id_provincia = pro.id_provincia inner join departamento depa on pro.id_departamento = depa.id_departamento")
        direcciones = cursor.fetchall()
    conexion.close()
    return direcciones

def obtener_direccion_por_id(id_direccion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("select dir.id_direccion, dir.nombre, dir.referencia, dis.id_distrito, dis.nombre, pro.id_provincia, pro.nombre, depa.id_departamento, depa.nombre from direccion dir inner join distrito dis on dir.id_distrito = dis.id_distrito inner join provincia pro on dis.id_provincia = pro.id_provincia inner join departamento depa on pro.id_departamento = depa.id_departamento where dir.id_direccion = %s", (id_direccion))
        direcciones = cursor.fetchall()
    conexion.close()
    return direcciones

def obtener_direccion_por_idUsuario(id_usuario):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("select dir.id_direccion, dir.nombre, dir.referencia, dis.id_distrito, dis.nombre, pro.id_provincia, pro.nombre, depa.id_departamento, depa.nombre from direccion dir inner join direccion_usuario dus on dus.id_direccion = dir.id_direccion inner join distrito dis on dir.id_distrito = dis.id_distrito inner join provincia pro on dis.id_provincia = pro.id_provincia inner join departamento depa on pro.id_departamento = depa.id_departamento where dus.id_usuario=%s and dus.estado=0", (id_usuario))
        direcciones = cursor.fetchall()
    conexion.close()
    return direcciones

def obtener_departamentos():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("select id_departamento, nombre from departamento")
        departamentos = cursor.fetchall()
    conexion.close()
    return departamentos

def obtener_provincia_por_departamento(id_departamento):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT pro.id_provincia, pro.nombre FROM departamento depa INNER JOIN provincia pro ON pro.id_departamento = depa.id_departamento WHERE depa.id_departamento = %s", (id_departamento,))
        provincia = cursor.fetchall()
    conexion.close()
    return provincia

def obtener_distritos_por_provincia(id_provincia):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("select dis.id_distrito, dis.nombre from provincia pro inner join distrito dis on dis.id_provincia = pro.id_provincia where pro.id_provincia = %s", (id_provincia))
        distritos = cursor.fetchall()
    conexion.close()
    return distritos

def guardar_direccion(nombre, referencia, id_distrito):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO direccion (nombre, referencia, id_distrito) VALUES (%s, %s, %s)", (nombre, referencia, id_distrito))
    conexion.commit()
    conexion.close()

def editar_direccion(nombre, referencia, id_distrito, id_direccion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("update direccion set nombre = %s, referencia = %s, id_distrito = %s where id_direccion = %s", (nombre, referencia, id_distrito, id_direccion))
    conexion.commit()
    conexion.close()

def darbaja_direccion(id_direccion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("update direccion set estado = 1 where id_direccion = %s", (id_direccion))
    conexion.commit()
    conexion.close()

def obtener_direccion_usuario(id_usuario):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("select dir.id_direccion, dir.nombre from direccion_usuario du inner join direccion dir on du.id_direccion=dir.id_direccion inner join usuario us on us.id_usuario=du.id_usuario where du.estado=0 and us.id_usuario = %s", (id_usuario))
        direcciones_usuario = cursor.fetchall()
    conexion.close()
    return direcciones_usuario

def registrar_direccion_retornable(nombre, referencia, id_distrito, id_usuario, estado):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            # Creamos una lista con los parámetros de entrada y salida
            parametros = [nombre, referencia, id_distrito, id_usuario, estado, 0]  # El último es el parámetro de salida

            # Llamamos al procedimiento almacenado
            cursor.callproc('registrarDireccion', parametros)
            
            # Recuperar el valor del parámetro de salida (último parámetro)
            cursor.execute("SELECT @_registrarDireccion_5")  # Aquí "_5" porque es el sexto parámetro (el parámetro de salida)
            id_direccion = cursor.fetchone()[0]

            # Confirmar los cambios en la base de datos
            conexion.commit()

            print(f"ID Dirección retornado: {id_direccion}")
        
    except Exception as e:
        print(f"Error al registrar dirección: {e}")
        id_direccion = None
    finally:
        conexion.close()  # Cerrar la conexión

    return id_direccion

 
 
