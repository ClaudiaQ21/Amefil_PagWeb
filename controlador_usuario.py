from bd import obtener_conexion
import base64


def insertar_usuario(nombre, apellido_p, apellido_m, correo, telefono, genero, nacimiento, contrasena):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuario ( nombre, apellido_p, apellido_m, correo, telefono, genero, nacimiento, contrasena) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (nombre, apellido_p, apellido_m, correo, telefono, genero, nacimiento, contrasena))
    conexion.commit()
    conexion.close()



def obtener_usuarios():
    conexion = obtener_conexion()
    usuario = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * from usuario")
        usuario = cursor.fetchall()
    
            
    conexion.close()
    return usuario

def eliminar_usuario(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuatio WHERE id_usuario = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_usuario_por_id(id):
    conexion = obtener_conexion()
    producto = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_usuario, nombre, apellido_p, apellido_m, correo, telefono, genero, nacimiento, contrasena FROM usuario WHERE id_usuario = %s", (id,))
        producto = cursor.fetchone()
    conexion.close()
    return producto

def obtener_usuario_por_correo(correo):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_usuario, nombre, apellido_p, apellido_m, correo, telefono, genero, nacimiento, contrasena FROM usuario WHERE correo = %s", (correo,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def actualizar_usuario(nombre, apellido_p, apellido_m, correo, telefono, genero, nacimiento, contrasena, id_usuario):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario SET nombre = %s, apellido_p = %s, apellido_m = %s, correo = %s, telefono = %s, genero = %s, nacimiento = %s, contraseña = %s WHERE id_usuario = %s",
                       ( nombre, apellido_p, apellido_m, correo, telefono, genero, nacimiento, contrasena, id_usuario))
    conexion.commit()
    conexion.close()