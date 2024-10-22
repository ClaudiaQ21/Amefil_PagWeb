from bd import obtener_conexion
from flask import Flask, render_template, request, redirect, flash, jsonify, session, url_for
from datetime import datetime
import base64

def insertar_pedido_cesta(id_usuario, monto_total=0):
    conexion = obtener_conexion()
    fecha_actual = datetime.now().date()  
    hora_actual = datetime.now().time() 
    estado = 0 
    with conexion.cursor() as cursor:
        cursor.execute("""
            INSERT INTO pedido_cesta (estado, monto_total, fecha_registro, hora_registro, id_direccion, id_usuario) 
            VALUES (%s, %s, %s, %s, NULL, %s)
        """, (estado, monto_total, fecha_actual, hora_actual, id_usuario))
        id_pedido = cursor.lastrowid 
    conexion.commit()
    conexion.close()
    return id_pedido

def obtener_pedidoCliente(id_usuario):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT p.id_producto, p.nombre, p.precio, dc.cantidad, pc.monto_total, pc.id_pedido, p.imagen
                FROM pedido_cesta pc
                INNER JOIN detalle_cesta dc ON dc.id_pedido = pc.id_pedido
                INNER JOIN producto p ON p.id_producto = dc.id_producto
                WHERE pc.id_usuario = %s AND pc.estado = 0
            """, (id_usuario,))
            resultados = cursor.fetchall()
        
        detpedidos = []
        for resultado in resultados:
            imagen_base64 = base64.b64encode(resultado[6]).decode('utf-8') if resultado[6] else None
            detpedidos.append((
                resultado[0], 
                resultado[1], 
                resultado[2],  
                resultado[3],  
                resultado[2] * resultado[3], 
                resultado[5],  
                imagen_base64
            ))
        return detpedidos
    except Exception as e:
        print(f"Error al obtener pedido del cliente: {e}")
        return []
    finally:
        conexion.close()

def obtener_Montopedido(id_usuario):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT SUM(dc.cantidad * dc.precio) AS monto_total
                FROM detalle_cesta dc
                INNER JOIN pedido_cesta pc ON dc.id_pedido = pc.id_pedido
                WHERE pc.id_usuario = %s AND pc.estado = 0
            """, (id_usuario,))
            resultado = cursor.fetchone()
        return resultado[0] if resultado else 0
    except Exception as e:
        print(f"Error al obtener monto del pedido: {e}")
        return 0
    finally:
        conexion.close()

def obtener_monto_total(id_usuario):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("select monto_total from pedido_cesta where id_usuario = %s and estado = 0", (id_usuario))
        monto = cursor.fetchone()
    conexion.close()
    return monto

def eliminar_productoPedido(id_producto, id_pedido, id_usuario):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("call eliminardetallecesta(%s, %s, %s)", (id_producto, id_pedido, id_usuario))
            conexion.commit()
            print(f"Producto {id_producto} del pedido {id_pedido} eliminado exitosamente.")
    except Exception as e:
        print(f"Error al eliminar producto del pedido: {e}")
        raise e
    finally:
        conexion.close()



def buscar_pedidoCliente(id_usuario): 
    conexion = obtener_conexion()
    pedido_cesta = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_pedido FROM pedido_cesta WHERE estado = 0 and id_usuario=%s",(id_usuario))
        pedido_cesta = cursor.fetchone()  
    conexion.close()
    return pedido_cesta

def insertar_detalleCesta(id_producto, id_usuario, cantidad=1, descuento=0):
    print("Iniciando la inserción de detalle cesta...")
    conexion = obtener_conexion()
    pedido = buscar_pedidoCliente(id_usuario)

    if pedido:
        id_pedido = pedido[0]
    else:
        print("No se encontró pedido existente, insertando nuevo pedido...")
        id_pedido = insertar_pedido_cesta(id_usuario)

    with conexion.cursor() as cursor:
        cursor.execute("SELECT precio FROM producto WHERE id_producto = %s", (id_producto,))
        resultado_precio = cursor.fetchone()

        if resultado_precio:
            precio = resultado_precio[0]  
            print(f"Precio obtenido de la base de datos: {precio}")
        else:
            print("No se encontró el producto en la base de datos.")
            return False

        cursor.execute("SELECT * FROM detalle_cesta WHERE id_pedido = %s AND id_producto = %s", (id_pedido, id_producto))
        detalle_existente = cursor.fetchone()
        
        if not detalle_existente:
            cursor.execute("""
                INSERT INTO detalle_cesta (id_producto, id_pedido, cantidad, precio, descuento) 
                VALUES (%s, %s, %s, %s, %s)
            """, (id_producto, id_pedido, cantidad, precio, descuento))
            print(f"Producto añadido al carrito con precio {precio}.")
        else:
            print("El producto ya existe en el carrito, puedes incrementar la cantidad aquí si es necesario.")
        
        cursor.execute("""
            UPDATE pedido_cesta 
            SET monto_total = (
                SELECT SUM(dc.cantidad * dc.precio) 
                FROM detalle_cesta dc 
                WHERE dc.id_pedido = %s
            ) 
            WHERE id_pedido = %s
        """, (id_pedido, id_pedido))
        
    conexion.commit()
    conexion.close()
    return True


def actualizar_detalle_pedido(id_producto, nueva_cantidad, id_usuario):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                UPDATE detalle_cesta
                SET cantidad = %s
                WHERE id_producto = %s AND id_pedido = (
                    SELECT id_pedido FROM pedido_cesta 
                    WHERE id_usuario = %s 
                    AND estado = 0
                    ORDER BY fecha_registro DESC 
                    LIMIT 1
                );
            """, (nueva_cantidad, id_producto, id_usuario))

            cursor.execute("""
                UPDATE pedido_cesta
                SET monto_total = (
                    SELECT SUM(cantidad * precio) FROM detalle_cesta
                    WHERE id_pedido = (
                        SELECT id_pedido FROM pedido_cesta 
                        WHERE id_usuario = %s 
                        AND estado = 0
                        ORDER BY fecha_registro DESC 
                        LIMIT 1
                    )
                )
                WHERE id_usuario = %s 
                AND estado = 0
                ORDER BY fecha_registro DESC 
                LIMIT 1;
            """, (id_usuario, id_usuario))

            print(f"Actualizando producto {id_producto} con cantidad {nueva_cantidad} para usuario {id_usuario}")
        
        conexion.commit()
    except Exception as e:
        print(f"Error al actualizar detalle_pedido: {str(e)}")
    finally:
        conexion.close()

def finalizar_pedido(id_usuario, id_direccion):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT id_pedido 
                FROM pedido_cesta 
                WHERE id_usuario = %s AND estado = 0
            """, (id_usuario,))
            resultado = cursor.fetchone()
            
            if resultado:
                id_pedido = resultado[0]
                cursor.execute("""
                    UPDATE pedido_cesta 
                    SET estado = False, id_direccion = %s 
                    WHERE id_pedido = %s
                """, (id_direccion, id_pedido))
                conexion.commit()
                return True
            else:
                return False
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        conexion.close()




