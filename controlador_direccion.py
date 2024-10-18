# controlador_direccion.py

from flask import jsonify
from bd import obtener_conexion

def obtener_direcciones():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_direccion, detalle, id_ubigeo FROM direccion")
        direcciones = cursor.fetchall()
    conexion.close()
    return direcciones
