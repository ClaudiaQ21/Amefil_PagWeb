from bd import obtener_conexion
import base64


def insertar_usuario(nombre, apellido_p, apellido_m, correo, contrasena, telefono,genero, nacimiento):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuario ( nombre, apellido_p, apellido_m, correo, contrasena, telefono,genero, nacimiento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (nombre, apellido_p, apellido_m, correo, contrasena, telefono,genero, nacimiento))
    conexion.commit()
    conexion.close()

def insertar_usuario_cliente(nombre, apellido_p, apellido_m, correo, contrasena, telefono,genero, nacimiento):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuario ( nombre, apellido_p, apellido_m, correo, contrasena, telefono,genero, nacimiento, id_tipo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,1)",
                       (nombre, apellido_p, apellido_m, correo, contrasena, telefono,genero, nacimiento))
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

def obtener_usuarios_por_tipo(id_tipo):
    conexion = obtener_conexion()
    user_tipo = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "select CONCAT(us.nombre, ' ', us.apellido_p, ' ', us.apellido_m) as nombrescompletos, us.correo, us.telefono, us.genero, us.nacimiento, dir.detalle from usuario us inner join tipo_usuario tu on us.id_tipo=tu.id_tipo inner join direccion dir on dir.id_direccion = us.id_direccion where tu.id_tipo = %s", 
            (id_tipo)
        )
        user_tipo = cursor.fetchall()
    conexion.close()
    return user_tipo

def actualizar_usuario(nombre, apellido_p, apellido_m, correo, telefono, genero, nacimiento, contrasena, id_usuario):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario SET nombre = %s, apellido_p = %s, apellido_m = %s, correo = %s, telefono = %s, genero = %s, nacimiento = %s, contraseña = %s WHERE id_usuario = %s",
                       ( nombre, apellido_p, apellido_m, correo, telefono, genero, nacimiento, contrasena, id_usuario))
    conexion.commit()
    conexion.close()

