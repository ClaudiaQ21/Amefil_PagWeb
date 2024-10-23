from bd import obtener_conexion
from flask import Flask, render_template, request, redirect, flash, jsonify, session, url_for
from datetime import datetime
import base64

def listar_pedido_por_idUsuario(id_usuario):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("select * from pedido_cesta where id_usuario = %s", (id_usuario))
        pedidos = cursor.fetchall()
    conexion.close()
    return pedidos

def obtener_imagen_pedido(id_usuario, id_pedido):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            # Ajustamos la consulta para asegurarnos de que obtenemos la imagen
            cursor.execute("""
                SELECT p.imagen 
                FROM pedido_cesta pc 
                INNER JOIN detalle_cesta dc ON dc.id_pedido = pc.id_pedido 
                INNER JOIN producto p ON p.id_producto = dc.id_producto 
                WHERE pc.id_usuario = %s and pc.id_pedido = %s LIMIT 1
            """, (id_usuario, id_pedido,))
            resultado = cursor.fetchone()

            # Verificamos si realmente se obtuvo algo
            if resultado and resultado[0]:
                imagen = base64.b64encode(resultado[0]).decode('utf-8')
                print(f"Imagen encontrada para el pedido {id_pedido}")  # Depuración
            else:
                imagen = None
                print(f"No se encontró imagen para el pedido {id_pedido}")  # Depuración

            return imagen
    except Exception as e:
        print(f"Error al obtener la imagen del pedido: {e}")
        return None
    finally:
        conexion.close()


def obtener_detalle_pedido(id_usuario, id_pedido):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("select pc.*, dc.*, p.nombre, p.imagen from pedido_cesta pc inner join detalle_cesta dc on pc.id_pedido = dc.id_pedido INNER JOIN producto p ON p.id_producto = dc.id_producto where pc.id_usuario=%s and pc.id_pedido=%s", (id_usuario, id_pedido))
        detalles = cursor.fetchall()
    
    if not detalles:
        detalles = []

    detalles_con_imagen = []
    for detalle in detalles:
        imagen_base64 = base64.b64encode(detalle[13]).decode('utf-8')

        detalles_con_imagen.append((
            detalle[0],  # id_pedido
            detalle[2],  # monto_total
            detalle[3],  # fecha
            detalle[4],  # hora
            detalle[7],  # id_producto
            imagen_base64, # imagen convertida a Base64
            detalle[9],  # cantidad
            detalle[10],  # precio unitario
            detalle[12]  # nombre
        ))

    conexion.close()
    return detalles_con_imagen

def obtener_suma_total():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("select sum(monto_total) from pedido_cesta where estado = 1")
        total = cursor.fetchone()
    conexion.close()
    return total

def obtener_pedidos_totales():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("select CONCAT(us.nombre, " ", us.apellido_p, " ", us.apellido_m) as cliente, pc.monto_total, pc.fecha_registro from pedido_cesta pc inner join usuario us on pc.id_usuario=us.id_usuario")
        totalpedidos = cursor.fetchall()
    conexion.close()
    return totalpedidos   

def ranking_pedido_distritos():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT dis.nombre AS distrito, COUNT(*) AS cantidad_pedidos, SUM(ped.monto_total) AS monto_total FROM pedido_cesta ped INNER JOIN direccion_usuario dus ON ped.id_usuario = dus.id_usuario AND dus.id_direccion = ped.id_direccion INNER JOIN direccion dir ON dir.id_direccion = dus.id_direccion INNER JOIN distrito dis ON dis.id_distrito = dir.id_distrito GROUP BY dis.nombre ORDER BY monto_total DESC;")
        ranking = cursor.fetchall()
    conexion.close()
    return ranking 