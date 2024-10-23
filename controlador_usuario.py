from bd import obtener_conexion
import base64


def insertar_usuario(nombre, apellido_p, apellido_m, correo, contrasena, telefono, genero, nacimiento, id_tipo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "INSERT INTO usuario (nombre, apellido_p, apellido_m, correo, contrasena, telefono, genero, nacimiento, id_tipo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (nombre, apellido_p, apellido_m, correo, contrasena, telefono, genero, nacimiento, id_tipo)
        )
    conexion.commit()
    conexion.close()

def insertar_usuario_cliente(nombre, apellido_p, apellido_m, correo, contrasena, telefono, genero, nacimiento):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuario ( nombre, apellido_p, apellido_m, correo, contrasena, telefono, genero, nacimiento, id_tipo,estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,1,0)",
                       (nombre, apellido_p, apellido_m, correo, contrasena, telefono, genero, nacimiento))
    conexion.commit()
    conexion.close()
 
def obtener_usuarios():
    conexion = obtener_conexion()
    usuarios = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "select us.id_usuario, CONCAT(us.nombre, ' ', us.apellido_p, ' ', us.apellido_m) as nombrescompletos, us.correo, us.telefono, us.genero, us.nacimiento,tu.nombre from usuario us inner join tipo_usuario tu on us.id_tipo=tu.id_tipo")
        usuarios = cursor.fetchall()            
    conexion.close()
    return usuarios

def eliminar_usuario(id_usuario):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuario WHERE id_usuario = %s", (id_usuario))
    conexion.commit()
    conexion.close()

def obtener_usuario_por_id(id_usuario):
    conexion = obtener_conexion()
    producto = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT us.id_usuario, CONCAT(us.nombre, ' ', us.apellido_p, ' ', us.apellido_m) as nombrescompleto, us.correo, us.contrasena, us.telefono, us.genero, us.nacimiento, us.id_tipo from usuario us inner join tipo_usuario tu on us.id_tipo=tu.id_tipo WHERE id_usuario = %s", (id_usuario))
        producto = cursor.fetchone()
    conexion.close()
    return producto

def obtener_usuario_por_correo(correo):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_usuario, nombre, apellido_p, apellido_m, correo, telefono, genero, nacimiento, contrasena FROM usuario WHERE correo = %s", (correo))
        resultado = cursor.fetchone()
        if resultado:
            usuario = {
                'id_usuario': resultado[0],
                'nombre': resultado[1],
                'apellido_p': resultado[2],
                'apellido_m': resultado[3],
                'correo': resultado[4],
                'telefono': resultado[5],
                'genero': resultado[6],
                'nacimiento': resultado[7],
                'contrasena': resultado[8]
            }
    conexion.close()
    return usuario


def obtener_usuarios_por_tipo(id_tipo):
    conexion = obtener_conexion()
    user_tipo = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "select  us.id_usuario, CONCAT(us.nombre, ' ', us.apellido_p, ' ', us.apellido_m) as nombrescompletos, us.correo, us.telefono, us.genero, us.nacimiento,tu.nombre from usuario us inner join tipo_usuario tu on us.id_tipo=tu.id_tipo where tu.id_tipo = %s", 
            (id_tipo)
        )
        user_tipo = cursor.fetchall()
    conexion.close()
    return user_tipo

def actualizar_usuario(nombre, apellido_p, apellido_m, correo, contrasena, telefono, genero, nacimiento, id_tipo, id_direccion, id_usuario):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE usuario SET nombre = %s, apellido_p = %s, apellido_m = %s, correo = %s, contrasena=%s, telefono = %s, genero = %s, nacimiento = %s, id_tipo = %s WHERE id_usuario = %s",
            (nombre, apellido_p, apellido_m, correo, contrasena, telefono, genero, nacimiento, id_tipo, id_usuario)
        )
    conexion.commit()
    conexion.close()

#TIPO
def obtener_tipo_usuario():
    conexion = obtener_conexion()
    tipo_usuarios = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_tipo, nombre from tipo_usuario")
        tipo_usuarios = cursor.fetchall()
    conexion.close()
    return tipo_usuarios

#DIRECCIONES
def obtener_direccion():
    conexion = obtener_conexion()
    direcciones = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_direccion, detalle, id_ubigeo from direccion")
        direcciones = cursor.fetchall()
    conexion.close()
    return direcciones

def dar_baja_usuario(id_usuario):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario SET estado = 1 WHERE id_usuario = %s", (id_usuario))
    conexion.commit()
    conexion.close()

def contarclientes():
    conexion = obtener_conexion()
    contadorc = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(id_usuario) FROM usuario where id_tipo=1")
        contadorc = cursor.fetchone()
    conexion.close()
    return contadorc

def contaradmins():
    conexion = obtener_conexion()
    contadora = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(id_usuario) FROM usuario where id_tipo=3")
        contadora = cursor.fetchone()
    conexion.close()
    return contadora

def contarusuarios():
    conexion = obtener_conexion()
    contadoru = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(id_usuario) FROM usuario")
        contadoru = cursor.fetchone()
    conexion.close()
    return contadoru