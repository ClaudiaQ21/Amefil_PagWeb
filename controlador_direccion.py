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
        cursor.execute("select id_direccion from direccion")
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
        cursor.execute("select pro.id_provincia, pro.nombre from departamento depa inner join provincia pro on pro.id_departamento = depa.id_departamento where depa.id_departamento = %s", (id_departamento))
        provincia = cursor.fetchall()
    conexion.close()
    return provincia

def obtener_distritos_por_provincia(id_departamento, id_provincia):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("select dis.id_distrito, dis.nombre from departamento depa inner join provincia pro on pro.id_departamento = depa.id_departamento inner join distrito dis on dis.id_provincia = pro.id_provincia where depa.id_departamento = %s and pro.id_provincia = %s", (id_departamento, id_provincia))
        distritos = cursor.fetchall()
    conexion.close()
    return distritos





