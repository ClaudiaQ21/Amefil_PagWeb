from flask import Flask, render_template, request, redirect, flash, jsonify
import controlador_producto

app = Flask(__name__)

@app.route("/")
@app.route("/amefil")
def amefil():
    return render_template("Index.html")


@app.route("/navegacionproductos")
def navegacionproductos():
    productos_con_imagen = controlador_producto.obtener_productos()
    return render_template("Navegacion_productos.html", productos_con_imagen = productos_con_imagen)

@app.route("/contacto")
def contacto():
    return render_template('Contacto.html')

@app.route("/sobreNosotros")
def sobreNosotros():
    return render_template('Amefil.html')

@app.route("/carrito")
def carrito():
    return render_template("carrito.html")

@app.route("/finalizarCompra")
def carrito():
    return render_template("Finalizar_compra.html")

# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)