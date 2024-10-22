# controlador_direccion.py

from flask import jsonify
from bd import obtener_conexion

def obtener_direcciones():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_direccion, detalle FROM direccion")
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

def obtener_provincias_por_departamento(id_departamento):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_provincia, nombre FROM provincia WHERE id_departamento = %s", (id_departamento,))
        provincias = cursor.fetchall()
    conexion.close()
    return provincias

def obtener_distritos_por_provincia(id_provincia):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_distrito, nombre FROM distrito WHERE id_provincia = %s", (id_provincia,))
        distritos = cursor.fetchall()
    conexion.close()
    return distritos

