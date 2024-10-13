// Función para agregar un producto a los favoritos
function addToFav(event) {
    const button = event.target;
    const productElement = button.closest('.descrip');
    const productId = productElement.getAttribute('data-id');
    const productName = productElement.getAttribute('data-name');
    const productPrice = parseFloat(productElement.getAttribute('data-price'));
    const productImage = document.getElementById('main-image').src;

    let fav = JSON.parse(localStorage.getItem('fav')) || [];

    let productIndex = fav.findIndex(item => item.id === productId);

    if (productIndex !== -1) {
        // Si el producto ya está en favoritos, eliminarlo
        fav.splice(productIndex, 1);
        alert('Producto eliminado de Favoritos');
    } else {
        // Si el producto no está en favoritos, agregarlo
        fav.push({
            id: productId,
            name: productName,
            price: productPrice,
            image: productImage,
            quantity: 1
        });
        alert('Producto agregado a Favoritos');
    }

    localStorage.setItem('fav', JSON.stringify(fav));
    renderFav();
}

// Función para renderizar la lista de favoritos en la página de favoritos
function renderFav() {
    const favContainer = document.getElementById('lista-favoritos');
    let fav = JSON.parse(localStorage.getItem('fav')) || [];
    favContainer.innerHTML = '';

    if (fav.length === 0) {
        document.getElementById('mensaje').style.display = 'block';
        return;
    } else {
        document.getElementById('mensaje').style.display = 'none';
    }

    fav.forEach((product, index) => {
        const div = document.createElement('div');
        div.className = 'col-lg-4 col-md-4 col-sm-6 col-6';
        div.id='bloquecitos';
        div.innerHTML = `
            <div class="cont_pro" data-id="${product.id}" data-name="${product.name}" data-price="${product.price}">
                <img src="${product.image}" class="card-img-top" alt="${product.name}">
                <div class="g-2">
                    <h6>${product.name}</h6>
                    <div class= "precio"> 
                    <p>S/${product.price}</p>
                    </div> 
                    <button type="button" class="botones agregar-carrito" id = "anadir-car">Añadir al carrito</button>
                    <button type="button" class="botones quitar-favorito" onclick="removeFromFav(${index})" id ="remover-fav">Quitar de favoritos</button>
                </div>
            </div>
        `;
        favContainer.appendChild(div);
    });
}

// Función para quitar un producto de los favoritos
function removeFromFav(index) {
    let fav = JSON.parse(localStorage.getItem('fav')) || [];
    fav.splice(index, 1);
    localStorage.setItem('fav', JSON.stringify(fav));
    renderFav();
}

// Evento para agregar a favoritos en la página del producto
document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('producto')) {
        const button = document.getElementById('favoritos');
        button.addEventListener('click', addToFav);
    }
    renderFav();
});

// Escuchar el evento de cambio en localStorage para actualizar automáticamente la lista de favoritos
window.addEventListener('storage', function(event) {
    if (event.key === 'fav') {
        renderFav();
    }
});
