document.addEventListener('DOMContentLoaded', () => {
    const carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    const carritoBody = document.querySelector('#carrito tbody');

    carrito.forEach(producto => {
        const filaCarrito = document.createElement('tr');
        filaCarrito.innerHTML = `
            <td><img src="${producto.imagen}" style="width: 50px; height: 50px;"></td>
            <td>${producto.nombre}</td>
            <td>S/${producto.precio.toFixed(2)}</td>
            <td>1</td>
            <td>S/${producto.total.toFixed(2)}</td>
            <td><button class="btn btn-danger btn-sm eliminar-item">Eliminar</button></td>
        `;
        carritoBody.appendChild(filaCarrito);
    });

    actualizarTotales();

    // Agregar funcionalidad a los botones de eliminar
    const eliminarButtons = document.querySelectorAll('.eliminar-item');
    eliminarButtons.forEach(button => {
        button.addEventListener('click', eliminarItem);
    });
});

function actualizarTotales() {
    const precios = document.querySelectorAll('#carrito tbody tr td:nth-child(5)');
    let subtotal = 0;

    precios.forEach(precio => {
        subtotal += parseFloat(precio.innerText.replace('S/', ''));
    });

    document.getElementById('subtotal').value = S/${subtotal.toFixed(2)};
    document.getElementById('total').value = S/${subtotal.toFixed(2)};
}

function eliminarItem(event) {
    const button = event.target;
    const fila = button.parentElement.parentElement;
    const nombreProducto = fila.querySelector('td:nth-child(2)').innerText;

    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    carrito = carrito.filter(producto => producto.nombre !== nombreProducto);

    localStorage.setItem('carrito', JSON.stringify(carrito));
    fila.remove();
    actualizarTotales();
}