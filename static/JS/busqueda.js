function buscarProducto(event) {
    if (event.key === "Enter") {
        // Obtén el valor del input
        var terminoBusqueda = document.getElementById('busqueda').value;

        if (terminoBusqueda.trim() !== "") {
            // Redirige a la página de navegación de productos con el término de búsqueda
            window.location.href = "Navegacion_productos.html?search=" + encodeURIComponent(terminoBusqueda);
        }
    }
}
window.addEventListener("DOMContentLoaded", function () {
    // Obtener el parámetro de búsqueda de la URL
    const params = new URLSearchParams(window.location.search);
    const searchQuery = params.get("search");

    if (searchQuery) {
        // Llama a la función para filtrar los productos
        filtrarProductos(searchQuery);
    }
});

function filtrarProductos(query) {
    const productos = document.querySelectorAll(".cont_pro"); // Selecciona todos los productos
    query = query.toLowerCase();

    productos.forEach(producto => {
        const nombreProducto = producto.getAttribute("data-name").toLowerCase();
        if (nombreProducto.includes(query)) {
            producto.style.display = "block"; // Mostrar producto si coincide con la búsqueda
        } else {
            producto.style.display = "none"; // Ocultar producto si no coincide
        }
    });
}