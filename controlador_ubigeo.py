from flask import jsonify
from bd import obtener_conexion

def obtener_departamentos():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("select DISTINCT departamento from ubigeo")
        departamentos = cursor.fetchall()
    conexion.close()    
    return departamentos

def obtener_provincias(departamento):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("select DISTINCT provincia from ubigeo where ubigeo.departamento = %s", departamento)
        provincias = cursor.fetchall()
    conexion.close()
    return provincias

def obtener_distritos(departamento, provincias):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("select DISTINCT provincia from ubigeo where ubigeo.departamento = %s and ubigeo.provincia=%s ", (departamento, provincias))
        provincias = cursor.fetchall()
    conexion.close()
    return provincias