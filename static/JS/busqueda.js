function buscarProducto(event) {
    if (event.key === "Enter") {
        event.preventDefault();

        // Determinar qué campo de búsqueda se está usando
        let query = "";
        const inputMovil = document.getElementById("busqueda-movil");
        const inputGrande = document.getElementById("busqueda-grande");

        if (inputMovil && inputMovil.offsetParent !== null) {
            // Si el campo de búsqueda móvil está visible
            query = inputMovil.value;
        } else if (inputGrande && inputGrande.offsetParent !== null) {
            // Si el campo de búsqueda para pantallas más grandes está visible
            query = inputGrande.value;
        }

        if (query) {
            // Redirigir con la consulta de búsqueda
            window.location.href = `/navegacionproductos?busqueda=${encodeURIComponent(query)}`;
        }
    }
}
