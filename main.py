from flask import Flask, render_template, request, redirect, flash, jsonify, session
import controlador_producto
import controlador_filtros
import controlador_usuario
import controlador_color
import controlador_temporada
import controlador_tipo_producto
import controlador_descuento
import controlador_roles
import controlador_direccion

app = Flask(__name__)
app.secret_key = 'alguna_clave_secreta'

@app.route("/")
@app.route("/amefil")
def amefil():
    return render_template("Index.html")

@app.context_processor
def inject_tipos():
    tipos = controlador_tipo_producto.obtener_tipo_productos()
    return dict(tipos=tipos)

## MENU

@app.route("/novedades")
def novedades():
    return render_template("Menu_novedades.html")

@app.route("/crea")
def crea():
    return render_template("Menu_crea.html")

@app.route("/descuentos")
def descuentos():
    return render_template("Menu_descuentos.html")

### AMEFIL

@app.route("/contacto")
def contacto():
    return render_template('Contacto.html')

@app.route("/sobrenosotros")
def sobrenosotros():
    return render_template('Amefil.html')

### PRODUCTO

@app.route("/navegacionproductos")
def navegacionproductos():
    productos_con_imagen = controlador_producto.obtener_productos()
    color = controlador_filtros.obtener_colores()
    tipo_pro = controlador_filtros.obtener_tipo_producto()
    temporada = controlador_filtros.obtener_temporadas()
    return render_template("Navegacion_productos.html", productos_con_imagen = productos_con_imagen, color = color, tipo_pro = tipo_pro, temporada=temporada)

@app.route("/producto")
def producto():
    return render_template("Producto.html")

@app.route("/guardar_producto", methods=["POST"])
def guardar_producto():
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    id_tipo_producto = request.form["id_tipo_producto"]
    vigencia = request.form["vigencia"]
    stock = request.form["stock"]
    descripcion = request.form["descripcion"]
    id_color = request.form["id_color"]
    id_temporada = request.form["id_temporada"]
    imagen = request.files['imagen'].read() 
    controlador_producto.insertar_producto(nombre, precio, id_tipo_producto, vigencia, stock, descripcion, id_color, id_temporada, imagen)
    return redirect("/navegacionproductos")

@app.route("/eliminar_producto", methods=["POST"])
def eliminar_producto():
    controlador_producto.eliminar_producto(request.form["id_producto"])
    return redirect("/navegacionproductos")


@app.route("/editar_producto/<int:id>")
def formulario_editar_producto(id):
    # Obtener el disco por ID
    color = controlador_filtros.obtener_colores()
    tipo_pro = controlador_filtros.obtener_tipo_producto()
    temporada = controlador_filtros.obtener_temporadas()
    producto = controlador_producto.obtener_producto_por_id(id)
    return render_template("Editar_Producto.html", producto=producto, color = color, tipo_pro = tipo_pro, temporada=temporada)


@app.route("/actualizar_producto", methods=["POST"])
def actualizar_producto():
    id_producto= request.form["id_producto"]
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    id_tipo_producto = request.form["id_tipo_producto"]
    vigencia = request.form["vigencia"]
    stock = request.form["stock"]
    descripcion = request.form["descripcion"]
    id_color = request.form["id_color"]
    id_temporada = request.form["id_temporada"]
    id_talla = request.form["id_talla"]
    imagen = request.files['imagen'].read() 
    controlador_producto.actualizar_producto(nombre, precio, id_tipo_producto, vigencia, stock, descripcion, id_color, id_temporada, id_talla, imagen, id_producto)
    return redirect("/navegacionproductos")

@app.route("/colecciones")
def colecciones():
    return render_template("Colecciones.html")

@app.route("/novedades")
def navegacionproductosnovedades():
    productos_nuevos = controlador_producto.obtener_novedades()
    color = controlador_filtros.obtener_colores()
    tipo_pro = controlador_filtros.obtener_tipo_producto()
    temporada = controlador_filtros.obtener_temporadas()
    return render_template("Navegacion_productos.html", productos_nuevos = productos_nuevos, color = color, tipo_pro = tipo_pro, temporada=temporada)



### PERFIL
@app.route("/perfil")
def perfil():
    return render_template("Perfil.html")

@app.route("/editardatos")
def editardatos():
    return render_template("Perfil_editar.html")

# @app.route("/editardatos/<int:id>")
# def editardatos(id):
#     usuario = controlador_usuario.obtener_usuario_por_id(id)
#     return render_template("Perfil_editar.html", usuario=usuario)

# @app.route("/actualizardatosusuario")
# def actualizarUsuario():
#     id = request.form["id"]
#     nombre = request.form["nombre"]
#     return redirect("/perfil")

### >>>> DIRECCIONES
@app.route("/editardireccion")
def editardireccion():
    return render_template("Direccion_editar.html")

@app.route("/agregardireccion")
def agregardireccion():
    return render_template("Direccion_nueva.html")

@app.route("/listadirecciones")
def listadirecciones():
    return render_template("Direccion_lista.html")

### >>>> PEDIDOS
@app.route("/listapedidos")
def listapedidos():
    return render_template("Pedidos_lista.html")

@app.route("/detallepedidos")
def detallepedidos():
    return render_template("Pedidos_detalle.html")

### >>>> FAVORITOS
@app.route("/listafavoritos")
def listafavoritos():
    return render_template("Favoritos_lista.html")



### CARRITO
@app.route("/carrito")
def carrito():
    return render_template("carrito.html")

@app.route("/finalizarCompra")
def carrito_finalizar():
    return render_template("Finalizar_compra.html")



### INICIAR SESION
@app.route("/iniciarsesion")
def iniciarsesion():
    return render_template("Iniciar_sesion.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['email']
        contrasena = request.form['password']

        usuario = controlador_usuario.obtener_usuario_por_correo(correo)

        if usuario and usuario['contrasena'] == contrasena:
            # Autenticación exitosa, almacenar información en la sesión
            session['usuario_id'] = usuario['id_usuario']
            session['nombre'] = usuario['nombre']
            return redirect("/amefil")  # Redirigir a la página del usuario

        else:
            # Mostrar mensaje de error en caso de credenciales inválidas
            error = 'Correo o contraseña incorrectos'
            return render_template('Iniciar_sesion.html', error=error)

    return render_template('Iniciar_sesion.html')  # Mostrar el formulario de inicio de sesión

@app.route("/registrar")
def registrar():
    return render_template("Registro_usuario.html")

@app.route('/registro', methods=['POST'])
def registro():
    nombre = request.form['nombre']
    apellido_p = request.form['apellido_p']
    apellido_m = request.form['apellido_m']
    contrasena = request.form['contrasena']
    correo = request.form['correo']
    telefono = request.form['telefono']
    genero = request.form['genero']
    nacimiento = request.form['nacimiento']
    
    
    controlador_usuario.insertar_usuario_cliente(nombre, apellido_p, apellido_m, correo, contrasena, telefono,genero, nacimiento)

    return redirect('/amefil')

@app.route("/eliminar_usuario", methods=["POST"])
def eliminar_usuario():
    controlador_usuario.eliminar_usuario(request.form["id_usuario"])
    return redirect("/usuariosdash")

@app.route('/reestablecer')
def reestablecer_contraseña():
    return render_template('Reestablecer_contraseña.html')
@app.route('/reestablecer_2')
def reestablecer_contraseña_2():
    return render_template('Reestablecer_contraseña_2.html')


### POLITICAS
@app.route("/terminosycondiciones")
def terminosycondiciones():
    return render_template

@app.route("/politicaprivacidad")
def politicaprivacidad():
    return render_template("PoliticaPrivacidad.html")

@app.route("/politicacookies")
def politicacookies():
    return render_template("PoliticaCookies.html")

@app.route("/librodereclamaciones")
def librodereclamaciones():
    return render_template("LibroReclamo.html")

@app.route("/formasdepago")
def formasdepago():
    return render_template("FormasPago.html")

@app.route("/tallaspulseras")
def tallaspulseras():
    return render_template("TallaPulseras.html")


###ADMIN
@app.route("/dashboardadmin")
def dashboardadmin():
    return render_template("DashboardAdmin.html")

@app.route("/dashboardmantenedor")
def dashboardmantenedor():
    return render_template("DashboardMantenedor.html")

###PRODUCTO DASH

@app.route("/productoadmin")
def productoadmin():
    productos_con_imagen = controlador_producto.obtener_productos()
    return render_template("ProductoLME.html", productos_con_imagen=productos_con_imagen)

@app.route("/agregar_producto")
def formulario_agregar_producto():
    tipos_productos = controlador_tipo_producto.obtener_tipo_productos()
    colores = controlador_color.obtener_colores()
    temporadas = controlador_temporada.obtener_temporadas()
    descuentos = controlador_descuento.obtener_descuentos()
    return render_template("Agregar_Prod.html", tipos_productos=tipos_productos, colores=colores, temporadas=temporadas, descuentos=descuentos)


###USUARIO DASH

@app.route("/usuarioadmin")
def usuarioadmin():
    usuariost=controlador_usuario.obtener_usuarios_por_tipo(3)
    return render_template("UsuarioAdmLME.html", usuarios=usuariost)

@app.route("/usuariosdash")
def usuariosdash():
    usuarios=controlador_usuario.obtener_usuarios()
    return render_template("UsuarioLME.html", usuarios=usuarios)
   
@app.route("/agregar_usuario")
def formulario_agregar_usuario():
    tipo_usuarios = controlador_roles.obtener_tipos_usuario()
    direcciones = controlador_direccion.obtener_direcciones()
    return render_template("Agregar_Usuario.html", tipo_usuarios=tipo_usuarios, direcciones=direcciones)

@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():
    nombre = request.form["nombre"]
    apellido_p = request.form["apellido_p"]
    apellido_m = request.form["apellido_m"]
    correo = request.form["correo"]
    contrasena = request.form["contrasena"]
    telefono = request.form["telefono"]
    genero = request.form["genero"]
    nacimiento = request.form["nacimiento"]
    id_tipo = request.form["id_tipo"]
    id_direccion = request.form["id_direccion"]

    controlador_usuario.insertar_usuario(nombre, apellido_p, apellido_m, correo, contrasena, telefono, genero, nacimiento, id_tipo, id_direccion)
    return redirect("/usuariosdash")

@app.route("/editar_usuario/<int:id>")
def formulario_editar_usuario(id):
    usuario = controlador_usuario.obtener_usuario_por_id(id)
    tipo_usuarios = controlador_roles.obtener_tipos_usuario()
    direcciones = controlador_direccion.obtener_direcciones()
    return render_template("Editar_Usuario.html", usuario=usuario, tipo_usuarios=tipo_usuarios, direcciones=direcciones)

@app.route("/actualizar_usuario", methods=["POST"])
def actualizar_usuario():
    id_usuario = request.form["id_usuario"]
    nombre = request.form["nombre"]
    apellido_p = request.form["apellido_p"]
    apellido_m = request.form["apellido_m"]
    correo = request.form["correo"]
    contrasena = request.form["contrasena"]
    telefono = request.form["telefono"]
    genero = request.form["genero"]
    nacimiento = request.form["nacimiento"]
    id_tipo = request.form["id_tipo"]
    id_direccion = request.form["id_direccion"]
    controlador_usuario.actualizar_usuario(nombre, apellido_p, apellido_m, correo, contrasena, telefono, genero, nacimiento, id_tipo, id_direccion, id_usuario)
    return redirect("/usuariosdash")

###ROLES

@app.route("/roladmin")
def roladmin():
    roles = controlador_roles.obtener_tipos_usuario()
    return render_template("RolLME.html", roles=roles)

@app.route("/agregar_rol")
def formulario_agregar_tipo_usuario():
    return render_template("Agregar_Rol.html")

@app.route("/guardar_tipo_usuario", methods=["POST"])
def guardar_tipo_usuario():
    nombre = request.form["nombre"]
    controlador_roles.insertar_tipo_usuario(nombre)
    return redirect("/roladmin")

@app.route("/eliminar_tipo_usuario", methods=["POST"])
def eliminar_tipo_usuario():
    controlador_roles.eliminar_tipo_usuario(request.form["id_tipo"])
    return redirect("/roladmin")

@app.route("/editar_tipo_usuario/<int:id>")
def formulario_editar_tipo_usuario(id):
    rol = controlador_roles.obtener_tipo_usuario_por_id(id)
    return render_template("Editar_Rol.html", rol=rol)

@app.route("/actualizar_tipo_usuario", methods=["POST"])
def actualizar_tipo_usuario():
    id_tipo = request.form["id_tipo"]
    nombre = request.form["nombre"]
    controlador_roles.actualizar_tipo_usuario(nombre, id_tipo)
    return redirect("/roladmin")


###DESCUENTO
@app.route("/descuentoadmin")
def descuentoadmin():
    descuentos = controlador_descuento.obtener_descuentos()
    return render_template ("DescuentoLME.html", descuentos = descuentos)

@app.route("/agregar_descuento")
def formulario_agregar_descuento():
    return render_template("Agregar_Descuento.html")

@app.route("/guardar_descuento", methods=["POST"])
def guardar_descuento():
    tasa = request.form["tasa"]
    fecha_inicio = request.form["fecha_inicio"]
    fecha_fin = request.form["fecha_fin"]
    vigencia = request.form["vigencia"]
    controlador_descuento.insertar_descuento(tasa, fecha_inicio, fecha_fin, vigencia)
    return redirect("/descuentoadmin")

@app.route("/eliminar_descuento", methods=["POST"])
def eliminar_descuento():
    controlador_descuento.eliminar_descuento(request.form["id_descuento"])
    return redirect("/descuentoadmin")

@app.route("/editar_descuento/<int:id>")
def formulario_editar_descuento(id):
    descuento = controlador_descuento.obtener_descuento_por_id(id)
    return render_template("Editar_Descuento.html", descuento=descuento)

@app.route("/actualizar_descuento", methods=["POST"])
def actualizar_descuento():
    id_descuento = request.form["id_descuento"]
    tasa = request.form["tasa"]
    fecha_inicio = request.form["fecha_inicio"]
    fecha_fin = request.form["fecha_fin"]
    vigencia = request.form["vigencia"]
    controlador_descuento.actualizar_descuento(tasa, fecha_inicio, fecha_fin, vigencia, id_descuento)
    return redirect("/descuentoadmin")

###COLECCIONES

@app.route("/coleccionadmin")
def coleccionadmin():
    tipos = controlador_tipo_producto.obtener_tipo_productos()
    return render_template("ColeccionLME.html", tipos=tipos)

@app.route("/agregar_tipo_producto")
def formulario_agregar_tipo_producto():
    return render_template("Agregar_Coleccion.html")

@app.route("/guardar_tipo_producto", methods=["POST"])
def guardar_tipo_producto():
    nombre = request.form["nombre"]
    controlador_tipo_producto.insertar_tipo_producto(nombre)
    return redirect("/coleccionadmin")

@app.route("/eliminar_tipo_producto", methods=["POST"])
def eliminar_tipo_producto():
    id_tipo = request.form["id_tipo"]
    controlador_tipo_producto.eliminar_tipo(id_tipo)
    return redirect("/coleccionadmin")

@app.route("/editar_tipo_producto/<int:id>")
def formulario_editar_tipo_producto(id):
    tipo = controlador_tipo_producto.obtener_tipo_por_id(id)
    return render_template("Editar_Coleccion.html", tipo=tipo)

@app.route("/actualizar_tipo_producto", methods=["POST"])
def actualizar_tipo_producto():
    id_tipo = request.form["id_tipo"]
    nombre = request.form["nombre"]
    controlador_tipo_producto.actualizar_tipo_producto(nombre, id_tipo)
    return redirect("/coleccionadmin")

# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)