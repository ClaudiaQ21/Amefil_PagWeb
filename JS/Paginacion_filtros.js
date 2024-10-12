document.addEventListener("DOMContentLoaded", function() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    const itemsPerPage = 8; // Número de productos por página
    let items = document.querySelectorAll('.cont_pro'); // Todos los productos
    let numPages = Math.ceil(items.length / itemsPerPage); // Número inicial de páginas
    const paginationContainer = document.querySelector('.paginacion'); // Contenedor de los botones de paginación

    // Función para filtrar productos
    function filterProducts() {
        const selectedCategories = Array.from(checkboxes)
            .filter(checkbox => checkbox.checked)
            .reduce((filters, checkbox) => {
                const filterType = checkbox.getAttribute('name');
                if (!filters[filterType]) {
                    filters[filterType] = [];
                }
                filters[filterType].push(checkbox.value);
                return filters;
            }, {});

        // Contador de productos visibles
        let visibleCount = 0;

        items.forEach(product => {
            const colecc = product.getAttribute('data-colecc');
            const color = product.getAttribute('data-color');
            const temp = product.getAttribute('data-temp');

            const matchesCategory = !selectedCategories.colecc || selectedCategories.colecc.includes(colecc);
            const matchesColor = !selectedCategories.color || selectedCategories.color.includes(color);
            const matchesTemp = !selectedCategories.temp || selectedCategories.temp.includes(temp);

            // Mostrar solo si cumple con todas las opciones de los filtros seleccionados
            if (matchesCategory && matchesColor && matchesTemp) {
                product.parentElement.style.display = 'block';
                product.classList.add('product_visible');
                visibleCount++;
            } else {
                product.parentElement.style.display = 'none';
                product.classList.remove('product_visible');
            }
        });


        // Actualizar número de páginas y paginación
        numPages = Math.ceil(visibleCount / itemsPerPage);
        createPagination();
        showPage(1); // Mostrar la primera página
    }

    // Función para mostrar los productos de una página específica
    function showPage(page) {
        const visibleItems = document.querySelectorAll('.product_visible');
        const start = (page - 1) * itemsPerPage;
        const end = start + itemsPerPage;

        visibleItems.forEach((item, index) => {
            if (index >= start && index < end) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    }

    // Función para crear los botones de paginación
    function createPagination() {
        paginationContainer.innerHTML = ''; // Limpiar contenedor de paginación

        for (let i = 1; i <= numPages; i++) {
            const button = document.createElement('button');
            button.classList.add('pag_btn');
            button.innerText = i;
            button.addEventListener('click', () => showPage(i));
            paginationContainer.appendChild(button);
        }
    }

    // Inicializar la paginación y filtrar productos al cargar
    filterProducts(); // Inicializar con el filtro por defecto
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', filterProducts);
    });
});
