// Función para agregar productos al carrito
function addToCart(event) {
    const button = event.target;
    const productElement = button.closest('.cont_pro');
    const product = {
        id: productElement.getAttribute('data-id'),
        name: productElement.getAttribute('data-name'),
        price: parseFloat(productElement.getAttribute('data-price')),
        image: productElement.querySelector('img').src
    };

    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.push(product);
    localStorage.setItem('cart', JSON.stringify(cart));
    alert('Producto agregado al carrito');
}

// Función para renderizar los productos en la página del carrito
function renderCart() {
    const cartContainer = document.getElementById('cart');
    const totalElement = document.getElementById('total');
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cartContainer.innerHTML = '';
    let total = 0;
    cart.forEach((product, index) => {
        const cartItem = document.createElement('div');
        cartItem.className = 'cart-item';
        cartItem.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <h2>${product.name}</h2>
            <p>$${product.price.toFixed(2)}</p>
            <button onclick="removeFromCart(${index})">Eliminar</button>
        `;
        cartContainer.appendChild(cartItem);
        total += product.price;
    });
    totalElement.innerText = total.toFixed(2);
}

// Función para eliminar productos del carrito
function removeFromCart(index) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.splice(index, 1);
    localStorage.setItem('cart', JSON.stringify(cart));
    renderCart();
}

// Inicializar la página de productos o la del carrito
document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('products')) {
        const buttons = document.querySelectorAll('.add-to-cart');
        buttons.forEach(button => button.addEventListener('click', addToCart));
    } else if (document.getElementById('cart')) {
        renderCart();
    }
});
