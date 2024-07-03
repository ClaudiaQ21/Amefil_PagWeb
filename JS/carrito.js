// Función para agregar productos al carrito
function addToCart(event) {
    const button = event.target;
    const productElement = button.closest('.cont_pro');
    const productId = productElement.getAttribute('data-id');
    const productName = productElement.getAttribute('data-name');
    const productPrice = parseFloat(productElement.getAttribute('data-price'));
    const productImage = productElement.querySelector('img').src;

    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    // Verificar si el producto ya está en el carrito
    let productInCart = cart.find(item => item.id === productId);

    if (productInCart) {
        // Si el producto ya está en el carrito, incrementar su cantidad
        productInCart.quantity++;
    } else {
        // Si no está en el carrito, agregarlo con cantidad inicial 1
        cart.push({
            id: productId,
            name: productName,
            price: productPrice,
            image: productImage,
            quantity: 1
        });
    }

    localStorage.setItem('cart', JSON.stringify(cart));
    alert('Producto agregado al carrito');
    renderCart();
}

// Función para renderizar los productos en la página del carrito
function renderCart() {
    const cartContainer = document.getElementById('cart');
    const subtotalInput = document.getElementById('subtotal');
    const totalInput = document.getElementById('total');
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cartContainer.innerHTML = '';
    let subtotal = 0;

    cart.forEach((product, index) => {
        const cartItem = document.createElement('tr');
        cartItem.className = 'cart-item';
        cartItem.innerHTML = `
            <td><img id="peque" src="${product.image}"></td>
            <td>${product.name}</td>
            <td>S/${product.price.toFixed(2)}</td>
            <td>
                <button class=" btn-sm botones_increde decrementar-cantidad" data-id="${product.id}">-</button>
                <span class="cantidad">${product.quantity}</span> <!-- Mostrar la cantidad actual del producto -->
                <button class=" btn-sm botones_increde incrementar-cantidad" data-id="${product.id}">+</button>
            </td>
            <td>S/${(product.price * product.quantity).toFixed(2)}</td>
            <td><button type="button" class="botones_increde borrar-curso" onclick="removeFromCart(${index})" data-id="${product.id}" aria-label="Close">X</button></td>
        `;
        cartContainer.appendChild(cartItem);

        subtotal += product.price * product.quantity; // Calcular subtotal sumando el precio por la cantidad de cada producto
    });

    subtotalInput.value = subtotal.toFixed(2);
    totalInput.value = subtotal.toFixed(2); // Total inicial igual al subtotal

    // Event listeners para los botones de incrementar y decrementar cantidad
    document.querySelectorAll('.incrementar-cantidad').forEach(button => {
        button.addEventListener('click', () => {
            const productId = button.getAttribute('data-id');
            updateQuantity(productId, 1);
        });
    });

    document.querySelectorAll('.decrementar-cantidad').forEach(button => {
        button.addEventListener('click', () => {
            const productId = button.getAttribute('data-id');
            updateQuantity(productId, -1);
        });
    });
}

// Función para actualizar la cantidad de productos en el carrito
function updateQuantity(productId, change) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let product = cart.find(item => item.id === productId);

    if (product) {
        product.quantity += change;

        if (product.quantity < 1) {
            product.quantity = 1; // Evitar que la cantidad sea menor que 1
        }

        localStorage.setItem('cart', JSON.stringify(cart));
        renderCart(); // Renderizar de nuevo el carrito con la cantidad actualizada
    }
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
    if (document.getElementById('lista-cursos')) {
        const buttons = document.querySelectorAll('.agregar-carrito');
        buttons.forEach(button => button.addEventListener('click', addToCart));
    } else if (document.getElementById('cart')) {
        renderCart();
    }
});