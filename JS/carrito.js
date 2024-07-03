function addToCart(event) {
    const button = event.target;
    const productElement = button.closest('.cont_pro');
    const productId = productElement.getAttribute('data-id');
    const productName = productElement.getAttribute('data-name');
    const productPrice = parseFloat(productElement.getAttribute('data-price'));
    const productImage = productElement.querySelector('img').src;

    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    let productInCart = cart.find(item => item.id === productId);

    if (productInCart) {
        productInCart.quantity++;
    } else {
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

        subtotal += product.price * product.quantity; 
    });
   
    subtotalInput.value = subtotal.toFixed(2);
    totalInput.value = subtotal.toFixed(2); 

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
function updateQuantity(productId, change) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let product = cart.find(item => item.id === productId);

    if (product) {
        product.quantity += change;

        if (product.quantity < 1) {
            product.quantity = 1; 
        }

        localStorage.setItem('cart', JSON.stringify(cart));
        renderCart(); 
    }
}

function removeFromCart(index) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.splice(index, 1);
    localStorage.setItem('cart', JSON.stringify(cart));
    renderCart();
}

document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('lista-cursos')) {
        const buttons = document.querySelectorAll('.agregar-carrito');
        buttons.forEach(button => button.addEventListener('click', addToCart));
    } else if (document.getElementById('cart')) {
        renderCart();
    }
});

