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