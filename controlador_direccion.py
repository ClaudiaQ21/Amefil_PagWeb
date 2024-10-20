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
        cursor.execute("select dir.id_direccion, dir.detalle, ubi.departamento, ubi.provincia, ubi.distrito from direccion dir inner join ubigeo ubi on dir.id_ubigeo = ubi.id_ubigeo")
        direcciones = cursor.fetchall()
    conexion.close()
    return direcciones

# def agregar_direccion():
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("insert into direccion values ()")
