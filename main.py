from flask import Flask, render_template, request, redirect, flash, jsonify, session
import controlador_producto
import controlador_filtros
import controlador_usuario

app = Flask(__name__)
app.secret_key = 'alguna_clave_secreta'

@app.route("/")
@app.route("/amefil")
def amefil():
    return render_template("Index.html")

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

@app.route("/colecciones")
def colecciones():
    return render_template("Colecciones.html")



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

@app.route("/productoadmin")
def productoadmin():
    return render_template("ProductoLME.html")

# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)