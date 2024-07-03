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

    // Obtener carrito de localStorage o inicializarlo
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

    // Agregar producto al carrito
    const nuevoProducto = {
        imagen,
        nombre,
        precio,
        cantidad: 1,
        total: precio
    };

    carrito.push(nuevoProducto);
    
    // Guardar carrito actualizado en localStorage
    localStorage.setItem('carrito', JSON.stringify(carrito));

    // (Opcional) Mostrar una notificación o actualizar el estado del botón
    alert(`${nombre} añadido al carrito`);
}
