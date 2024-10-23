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
import controlador_finalizar_compra
import controlador_favoritos
import controlador_pedido

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
    
    busqueda = request.args.get('busqueda')
    productos_con_imagen = controlador_producto.obtener_productos(busqueda)
    if productos_con_imagen is None:
        productos_con_imagen = []  # Evita que sea None

    color = controlador_filtros.obtener_colores()
    tipo_pro = controlador_filtros.obtener_tipo_producto()
    temporada = controlador_filtros.obtener_temporadas()

    return render_template('Navegacion_productos.html',
        productos_con_imagen=productos_con_imagen,
        color=color,
        tipo_pro=tipo_pro,
        temporada=temporada
        )

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
    colores = controlador_filtros.obtener_colores()
    tipos_productos = controlador_filtros.obtener_tipo_producto()
    temporadas = controlador_filtros.obtener_temporadas()
    descuentos = controlador_descuento.obtener_descuentos()
    producto = controlador_producto.obtener_producto_por_id(id)
    return render_template("Editar_Producto.html", producto=producto, colores = colores, tipos_productos = tipos_productos, temporadas=temporadas, descuentos = descuentos)

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

    producto = controlador_producto.obtener_producto_por_id(id_producto)

    if request.files['imagen'].filename!='':
        imagen = request.files['imagen'].read()
    else:
        imagen = producto[6]
    controlador_producto.actualizar_producto(nombre, precio, id_tipo_producto, vigencia, stock, descripcion, id_color, id_temporada, imagen, id_producto)
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
    return render_template("Menu_novedades.html", productos_nuevos = productos_nuevos, color = color, tipo_pro = tipo_pro, temporada=temporada)





### PERFIL
@app.route("/perfil")
def perfil():
    return render_template("Perfil.html")

@app.route("/editardatos")
def editardatos():
    return render_template("Perfil_editar.html")

### >>>> DIRECCIONES
@app.route("/listadirecciones")
def listadirecciones():
    direcciones = controlador_direccion.obtener_direccion_completa()
    return render_template("Direccion_lista.html", direcciones = direcciones)


@app.route("/agregardireccion")
def agregardireccion():
    departamentos = controlador_direccion.obtener_departamentos()
    return render_template("Direccion_nueva.html", departamentos = departamentos)


@app.route("/guardar_direccion", methods=["POST"])
def guardar_direccion():
    distrito = request.form["id_distrito"]
    nombre = request.form["nombre"]
    referencia = request.form["referencia"]
    controlador_direccion.guardar_direccion(nombre, referencia, distrito)
    return redirect("/listadirecciones")

@app.route('/get_provincias/<int:departamento_id>')
def get_provincias(departamento_id):
    provincias = controlador_direccion.obtener_provincia_por_departamento(departamento_id)
    return jsonify(provincias)

@app.route('/get_distritos/<int:provincia_id>')
def get_distritos(provincia_id):
    distritos = controlador_direccion.obtener_distritos_por_provincia(provincia_id)
    return jsonify(distritos)



@app.route("/form_editar_direccion/<int:id>")
def form_editar_direccion(id):
    direccion = controlador_direccion.obtener_direccion_por_id(id)
    departamentos = controlador_direccion.obtener_departamentos()
    return render_template("Direccion_editar.html", direccion=direccion, departamentos=departamentos)

@app.route("/editar_direccion", methods=["POST"])
def editar_direccion():
    nombre = request.form["nombre"]
    referencia = request.form["referencia"]
    id_distrito = request.form["id_distrito"]
    id_direccion = request.form["id_direccion"]

    controlador_direccion.editar_direccion(nombre, referencia, id_distrito, id_direccion)

    return redirect("/listadirecciones")






### >>>> PEDIDOS
@app.route("/listapedidos")
def listapedidos():
    pedidos = controlador_pedido.listar_pedido_por_idUsuario(1)

    imagenes = []
    for pedido in pedidos:
        imagen = controlador_pedido.obtener_imagen_pedido(1, pedido[0])
        imagenes.append(imagen)

    return render_template("Pedidos_lista.html", pedidos=pedidos, imagenes=imagenes)

@app.route("/detallepedidos/<int:id>")
def detallepedidos(id):
    detalles_con_imagen = controlador_pedido.obtener_detalle_pedido(1, id)
    return render_template("Pedidos_detalle.html", detalles_con_imagen = detalles_con_imagen)




### >>>> FAVORITOS
@app.route("/listafavoritos")
def listafavoritos():
    return render_template("Favoritos_lista.html")

@app.route("/agregar_eliminar_favorito", methods=["POST"])
def agregar_eliminar_favorito():
    id_producto = request.form.get("data-id")
    
    verificacion = controlador_favoritos.verificar_favorito(id_producto)
    
    if verificacion == 1:
        controlador_favoritos.insertar_favorito(id_producto)
    elif verificacion == 0:
        controlador_favoritos.eliminar_favorito(id_producto)
    return redirect("/productovista")



### CARRITO
@app.route('/carrito')
def carrito():
    id_usuario = 1
    detpedidos = controlador_finalizar_compra.obtener_pedidoCliente(id_usuario)
    monto_total = controlador_finalizar_compra.obtener_Montopedido(id_usuario)
    return render_template('carrito.html', detpedidos=detpedidos, monto_total=monto_total)

@app.route("/carritoInsertar", methods=["POST"])
def carritoInsertar():
    try:
        print("Solicitud recibida para agregar al carrito")
        id_producto = request.form["id"]
        id_usuario = 1
        controlador_finalizar_compra.insertar_detalleCesta(id_producto, id_usuario)
        return jsonify({"success": True})

    except Exception as e:
        print("Error al insertar en el carrito:", e)
        return jsonify({"success": False, "error": str(e)}), 500
    
@app.route('/actualizar_cantidad', methods=['POST'])
def actualizar_cantidad():
    data = request.json
    id_producto = data['id_producto']
    nueva_cantidad = data['cantidad']
    id_usuario = 1
    try:
        controlador_finalizar_compra.actualizar_detalle_pedido(id_producto, nueva_cantidad, id_usuario)
        return jsonify({"mensaje": "Cantidad actualizada exitosamente"}), 200
    except Exception as e:
        return jsonify({"mensaje": "Error al actualizar la cantidad", "error": str(e)}), 500

@app.route('/eliminarProductoCarrito', methods=['POST'])
def eliminarProductoCarrito():
    data = request.get_json()
    id_producto = data.get('idProducto')
    id_pedido = data.get('idPedido')
    id_usuario = 1

    if not id_producto or not id_pedido:
        return jsonify({'error': 'Datos inválidos'}), 400

    try:
        controlador_finalizar_compra.eliminar_productoPedido(id_producto, id_pedido, id_usuario)
        return jsonify({'success': True}), 200
    except Exception as e:
        print(f"Error al eliminar el producto: {e}")
        return jsonify({'error': str(e)}), 500

@app.route("/finalizarCompra")
def carrito_finalizar():
    direcciones = controlador_direccion.obtener_direccion_usuario(1)
    departamentos = controlador_direccion.obtener_departamentos()
    usuario = controlador_usuario.obtener_usuario_por_id(1)
    carrito = controlador_finalizar_compra.obtener_monto_total(1)
    pedido = controlador_finalizar_compra.obtener_id_pedido_pago(1)
    return render_template("Finalizar_compra.html", departamentos = departamentos, direcciones = direcciones, usuario = usuario, carrito = carrito, pedido = pedido)

@app.route("/procesar_pago", methods=['POST'])
def procesar_pago():
    id_pedido = request.form.get("id_pedido")
    id_usuario = 1 
    select = request.form.get("selectAddress")  

    try:
        if select == "existente":
            id_direccion = request.form.get("id_direccion")
            if not id_direccion:  
                flash("Debe seleccionar una dirección válida", "error")
                return redirect("/finalizarCompra")
        else:  
            direccion = request.form.get("direccion")
            referencia = request.form.get("referencia")
            id_distrito = request.form.get("id_distrito")
            guardardireccion = request.form.get("guardardireccion")
            
            if guardardireccion == "guardar":
                estado = 0  
            else:
                estado = 1  

            id_direccion = controlador_direccion.registrar_direccion_retornable(direccion, referencia, id_distrito, id_usuario, estado)

            if not id_direccion:
                flash("No se pudo registrar la dirección", "error")
                return redirect("/listadirecciones")

        controlador_finalizar_compra.finalizar_pedido(id_pedido, id_direccion, id_usuario)
        flash("Compra realizada con éxito!", "success")
        return redirect("/amefil")
    
    except Exception as e:
        flash(f"Error al finalizar el pedido: {e}", "error")
        return redirect("/finalizarCompra")












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
    contador=controlador_descuento.contardescuento()
    contadort=controlador_tipo_producto.contartipo()
    contadorc=controlador_usuario.contarclientes()
    contadora=controlador_usuario.contaradmins()
    contadoru=controlador_usuario.contarusuarios()
    return render_template("DashboardAdmin.html", contador = contador, contadort=contadort, contadorc=contadorc, contadora=contadora, contadoru=contadoru)

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
    return render_template("Agregar_Usuario.html", tipo_usuarios=tipo_usuarios)

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
    controlador_usuario.insertar_usuario(nombre, apellido_p, apellido_m, correo, contrasena, telefono, genero, nacimiento, id_tipo)
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

@app.route("/usuariocliente")
def usuariocliente():
    usuariosc=controlador_usuario.obtener_usuarios_por_tipo(1)
    return render_template("ClienteLME.html", usuarios=usuariosc)


###DESCUENTO
@app.route("/descuentoadmin")
def descuentoadmin():
    descuentos = controlador_descuento.obtener_descuentos()
    productos_con_imagen = controlador_producto.obtener_productos()
    return render_template ("DescuentoLME.html", descuentos = descuentos, productos_con_imagen=productos_con_imagen)

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

@app.route("/asignardescuento/<int:id>")
def formulario_asignar_descuento(id):
    producto = controlador_producto.obtener_producto_por_id(id)
    descuentos = controlador_descuento.obtener_descuentos_vigentes()
    return render_template("Agregar_AsigDcto.html", producto = producto, descuentos=descuentos)

@app.route("/guardarasignardcto", methods=["POST"])
def guardarasignardcto():
    id_producto = request.form["id_producto"]
    id_descuento = request.form["id_descuento"]
    controlador_descuento.asignardescuento(id_producto, id_descuento)
    return redirect("/descuentoadmin")

@app.route("/editarasignardescuento/<int:id>")
def formulario_editar_asignar_descuento(id):
    producto = controlador_producto.obtener_producto_por_id(id)
    descuentos = controlador_descuento.obtener_descuentos_vigentes()
    return render_template("Editar_AsigDcto.html", producto = producto, descuentos=descuentos)

@app.route("/editarasignardcto", methods=["POST"])
def editarasignardcto():
    id_producto = request.form["id_producto"]
    id_descuento = request.form["id_descuento"]
    controlador_descuento.editarasignar(id_producto, id_descuento)
    return redirect("/descuentoadmin")

@app.route("/eliminarasignardcto", methods=["POST"])
def eliminarasignardcto():
    controlador_descuento.eliminarasignar(request.form["id_producto"])
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
    flash("Tipo de producto agregado correctamente.", "success")
    return redirect("/coleccionadmin")

@app.route("/eliminar_tipo_producto", methods=["POST"])
def eliminar_tipo_producto():
    id_tipo = request.form["id_tipo"]
    controlador_tipo_producto.eliminar_tipo(id_tipo)
    flash("Tipo de producto eliminado correctamente.", "success")
    return redirect("/coleccionadmin")

@app.route("/editar_tipo_producto/<int:id>")
def formulario_editar_tipo_producto(id):
    tipo = controlador_tipo_producto.obtener_tipo_por_id(id)
    return render_template("Editar_Coleccion.html", tipo=tipo)

@app.route("/actualizar_tipo_producto", methods=["POST"])
def actualizar_tipo_producto():
    id_tipo = request.form["id_tipo"]
    nombre = request.form["nombre"]
    estado = request.form["vigencia"]
    controlador_tipo_producto.actualizar_tipo_producto(nombre, estado, id_tipo)
    flash("Tipo de producto actualizado correctamente.", "success")
    return redirect("/coleccionadmin")

#Producto click
@app.route("/vista_producto/<int:id>")
def productovista(id):
    producto_imagen = controlador_producto.obtener_producto_por_id(id)
    return render_template("ProductoVista.html", producto_imagen=producto_imagen)


@app.route('/navegacion-productos')
def navegacion_productos():
    busqueda = request.args.get('busqueda', None)
    productos = controlador_producto.obtener_productos(busqueda)
    return render_template('Navegación productos.html', productos=productos)

# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)