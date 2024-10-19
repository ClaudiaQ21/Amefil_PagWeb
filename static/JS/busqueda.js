function buscarProducto(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        var busqueda = document.getElementById('busqueda').value;
        window.location.href = 'Navegación productos.html?busqueda=' + encodeURIComponent(busqueda);
    }
}