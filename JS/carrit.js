// Seleccionar todos los botones "Añadir al carrito"
const agregarCarritoButtons = document.querySelectorAll('.agregar-carrito');

// Agregar listener a cada botón
agregarCarritoButtons.forEach(button => {
    button.addEventListener('click', agregarAlCarrito);
});

function agregarAlCarrito(event) {
    const button = event.target;
    const producto = button.parentElement.parentElement; // div.cont_pro

    // Obtener datos del producto
    const imagen = producto.querySelector('img').src;
    const nombre = producto.querySelector('h6').innerText;
    const precio = parseFloat(producto.querySelector('p').innerText.replace('S/', ''));

    // Crear fila para el carrito
    const filaCarrito = document.createElement('tr');
    filaCarrito.innerHTML = `
        <td><img src="${imagen}" style="width: 50px; height: 50px;"></td>
        <td>${nombre}</td>
        <td>S/${precio.toFixed(2)}</td>
        <td>1</td>
        <td>S/${precio.toFixed(2)}</td>
        <td><button class="btn btn-danger btn-sm eliminar-item">Eliminar</button></td>
    `;

    // Agregar fila al cuerpo de la tabla del carrito
    const carrito = document.getElementById('carrito');
    const carritoBody = carrito.querySelector('tbody');
    carritoBody.appendChild(filaCarrito);

    // Actualizar subtotal y total
    actualizarTotales();
}

function actualizarTotales() {
    const precios = document.querySelectorAll('#carrito tbody tr td:nth-child(5)');
    let subtotal = 0;

    precios.forEach(precio => {
        subtotal += parseFloat(precio.innerText.replace('S/', ''));
    });

    // Mostrar subtotal y total
    document.getElementById('subtotal').value = `S/${subtotal.toFixed(2)}`;
    document.getElementById('total').value = `S/${subtotal.toFixed(2)}`;
}
