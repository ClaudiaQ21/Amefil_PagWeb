document.addEventListener('DOMContentLoaded', function () {
    const botonesAgregarCarrito = document.querySelectorAll('.agregar-carrito');

    botonesAgregarCarrito.forEach(boton => {
        boton.addEventListener('click', function () {
            const idProducto = this.getAttribute('data-id');
            const nombreProducto = this.getAttribute('data-name');
            const precioProducto = this.getAttribute('data-price');

            const confirmacion = confirm(`¿Seguro que quieres añadir ${nombreProducto} por S/${precioProducto} al carrito?`);
            if (confirmacion) {
                const carrito = JSON.parse(localStorage.getItem('carrito')) || {};
                if (carrito[idProducto]) {
                    carrito[idProducto].cantidad += 1; // Incrementar cantidad si ya existe
                } else {
                    carrito[idProducto] = {
                        nombre: nombreProducto,
                        precio: parseFloat(precioProducto),
                        cantidad: 1
                    };
                }
                localStorage.setItem('carrito', JSON.stringify(carrito));

                // Enviar los datos al servidor (BD)
                fetch('/carritoInsertar', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: new URLSearchParams({ 'id': idProducto })
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            alert(`${nombreProducto} ha sido añadido al carrito.`);
                            calcularTotales();
                        } else {
                            alert('Error al añadir el producto al carrito: ' + (data.error || 'Error desconocido'));
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        alert('Error al añadir el producto al carrito. Verifica la consola para más detalles.');
                    });
            }
        });
    });

    const botonesCantidad = document.querySelectorAll('.btn-quantity');

    botonesCantidad.forEach(boton => {
        boton.addEventListener('click', function () {
            const idProducto = this.getAttribute('data-id');
            const cantidadElemento = document.getElementById(`cantidad-${idProducto}`);
            const totalElemento = document.getElementById(`total-${idProducto}`); 
            const stockElemento = document.querySelector(`[data-id="${idProducto}"]`); 
            const stockDisponible = parseInt(stockElemento.getAttribute('data-stock'));
            let cantidad = parseInt(cantidadElemento.textContent);

            const precioPorUnidad = parseFloat(totalElemento.textContent.replace('S/', '')) / (cantidad || 1); 

            if (this.classList.contains('mas')) {
                if (cantidad < stockDisponible) { 
                    cantidad += 1;
                } else {
                    alert("No hay más de esa cantidad disponible");
                }
            } else if (this.classList.contains('menos') && cantidad > 1) {
                cantidad -= 1;
            }
            cantidadElemento.textContent = cantidad;

            totalElemento.textContent = (precioPorUnidad * cantidad).toFixed(2); 

            const carrito = JSON.parse(localStorage.getItem('carrito'));
            if (carrito && carrito[idProducto]) {
                carrito[idProducto].cantidad = cantidad; 
                localStorage.setItem('carrito', JSON.stringify(carrito));
            }

            fetch('/actualizar_cantidad', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    id_producto: idProducto,
                    cantidad: cantidad
                })
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Error al actualizar la cantidad');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log(data.mensaje);
                    calcularTotales();
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    });


    document.querySelectorAll('.eliminar-producto').forEach(button => {
        button.addEventListener('click', function () {
            const idProducto = this.getAttribute('data-idProducto');
            const idPedido = this.getAttribute('data-idPedido');

            if (!idProducto || !idPedido) {
                alert('Error: Producto o pedido no válido');
                return;
            }
            const confirmacion = confirm('¿Estás seguro que quieres eliminar este producto?');
            if (!confirmacion) {
                return;
            }

            fetch('/eliminarProductoCarrito', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token() }}' 
                },
                body: JSON.stringify({
                    idProducto: idProducto,
                    idPedido: idPedido
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    this.closest('tr').remove();
                    calcularTotales();
                    alert('Producto eliminado con éxito');
                } else {
                    alert('Error al eliminar el producto: ' + (data.error || 'Error desconocido'));
                }
            })
            .catch(error => {
                console.error('Error al eliminar el producto:', error);
                alert('Ha ocurrido un error al eliminar el producto');
            });
        });
    });
    

    function calcularTotales() {
        const cartItems = document.querySelectorAll('#cart tr');
        let subtotal = 0;

        cartItems.forEach(item => {
            const precioElement = item.querySelector('td:nth-child(3)');
            const cantidadElement = item.querySelector('.cantidad');
            const totalElement = item.querySelector('.total'); // Asegúrate de que el selector es correcto

            if (precioElement && cantidadElement && totalElement) {
                const precio = parseFloat(precioElement.innerText.replace('S/', ''));
                const cantidad = parseInt(cantidadElement.innerText);
                const totalPorProducto = parseFloat(totalElement.innerText.replace('S/', ''));

                if (!isNaN(precio) && !isNaN(cantidad)) {
                    subtotal += totalPorProducto; // Usa el total por producto
                }
            }
        });

        const descuento = 0;
        const totalAPagar = subtotal - descuento;

        const inputSubtotal = document.getElementById('subtotal');
        const inputDescuento = document.getElementById('descuento');
        const inputTotal = document.getElementById('total');

        if (inputSubtotal && inputDescuento && inputTotal) {
            inputSubtotal.value = 'S/' + subtotal.toFixed(2);
            inputDescuento.value = 'S/' + descuento.toFixed(2);
            inputTotal.value = 'S/' + totalAPagar.toFixed(2);
        } else {
            console.error('No se encontraron los elementos de entrada para mostrar los totales.');
        }

        console.log('Subtotal:', subtotal);
        console.log('Descuento:', descuento);
        console.log('Total a pagar:', totalAPagar);
    }


    calcularTotales();
});

function finalizarCompra() {
    const mensajeVacio = document.getElementById('mensaje-vacio');
    const cart = document.getElementById('cart');
    const cartItems = cart ? cart.querySelectorAll('tr') : [];
    
    if (mensajeVacio || cartItems.length === 0) {
        alert('No puedes finalizar la compra si no hay productos en el carrito.');
    } else {
      
        window.location.href = "/finalizarCompra";  
    }
}





