$(document).ready(function(){
    $(".btn-dark").click(function(){
        if($(this).text() === "Pagar"){
            if(articulosCarrito.length === 0){
                alert("El carrito está vacío. Por favor agregue productos.");
                return;
            }

            let total = parseFloat($("#total").text());
            let descuento = 0;

            $("#descuento").text("Descuento: $" + descuento.toFixed(2));
            $("#total").text("Total a Pagar: $" + total.toFixed(2));
        } 
    });
});

const carrito = document.getElementById("carrito"),
      listaCursos = document.getElementById("lista-cursos"),
      contenedorCarrito = document.querySelector('#carrito');

let articulosCarrito = [];

registrarEventsListeners();

function registrarEventsListeners() {
    listaCursos.addEventListener('click', agregarCurso);
    carrito.addEventListener('click', eliminarCurso);

    // Asegúrate de definir el elemento vaciarCarritoBtn antes de usarlo
    const vaciarCarritoBtn = document.getElementById('vaciar-carrito-btn');
    if (vaciarCarritoBtn) {
        vaciarCarritoBtn.addEventListener('click', () => {
            articulosCarrito = [];
            limpiarHTML();
            actualizarTotal();
        });
    }
}

function agregarCurso(e) {
    if (e.target.classList.contains("agregar-carrito")) {
        const cursoSeleccionado = e.target.parentElement.parentElement;
        leerInfo(cursoSeleccionado);
    }
}

function eliminarCurso(e) {
    if (e.target.classList.contains("borrar-curso")) {
        const cursoId = e.target.getAttribute('data-id');
        articulosCarrito = articulosCarrito.filter(curso => curso.id !== cursoId);
        carritoHTML();
        actualizarTotal();
    }
}

function leerInfo(curso) {
    const infoCurso = {
        imagen: curso.querySelector('img').src,
        titulo: curso.querySelector('h6').textContent,
        precio: parseFloat(curso.querySelector('.precio p').textContent.replace('S/', '')),
        id: curso.querySelector('button').getAttribute('data-id'),
        cantidad: 1
    };

    const existe = articulosCarrito.some(curso => curso.id === infoCurso.id);
    if (existe) {
        articulosCarrito = articulosCarrito.map(curso => {
            if (curso.id === infoCurso.id) {
                curso.cantidad++;
                return curso;
            } else {
                return curso;
            }
        });
    } else {
        articulosCarrito = [...articulosCarrito, infoCurso];
    }
    carritoHTML();
    actualizarTotal();
}

function registrarEventosCantidad() {
    const decrementarBotones = document.querySelectorAll('.decrementar-cantidad');
    const incrementarBotones = document.querySelectorAll('.incrementar-cantidad');

    decrementarBotones.forEach(btn => {
        btn.addEventListener('click', decrementarCantidad);
    });

    incrementarBotones.forEach(btn => {
        btn.addEventListener('click', incrementarCantidad);
    });
}

function decrementarCantidad(e) {
    const cursoId = e.target.getAttribute('data-id');
    const cursoEnCarrito = articulosCarrito.find(curso => curso.id === cursoId);

    if (cursoEnCarrito.cantidad > 1) {
        cursoEnCarrito.cantidad--;
        carritoHTML();
        actualizarTotal();
    }
}

function incrementarCantidad(e) {
    const cursoId = e.target.getAttribute('data-id');
    const cursoEnCarrito = articulosCarrito.find(curso => curso.id === cursoId);

    cursoEnCarrito.cantidad++;
    carritoHTML();
    actualizarTotal();
}

function carritoHTML() {
    limpiarHTML();
    articulosCarrito.forEach(curso => {
        const fila = document.createElement('tr');
        fila.innerHTML = `
            <td><img id="peque" src="${curso.imagen}"></td>
            <td>${curso.titulo}</td>
            <td>S/${curso.precio.toFixed(2)}</td>
            <td>
                <button class="btn btn-sm btn-secondary decrementar-cantidad" data-id="${curso.id}">-</button>
                <span class="cantidad">${curso.cantidad}</span>
                <button class="btn btn-sm btn-primary incrementar-cantidad" data-id="${curso.id}">+</button>
            </td>
            <td>S/${(curso.precio * curso.cantidad).toFixed(2)}</td>
            <td><button type="button" class="btn-close borrar-curso" data-id="${curso.id}" aria-label="Close"></button></td>
        `;
        contenedorCarrito.appendChild(fila);
    });

    registrarEventosCantidad();
}

function limpiarHTML() {
    while (contenedorCarrito.firstChild) {
        contenedorCarrito.removeChild(contenedorCarrito.firstChild);
    }
}

function actualizarTotal() {
    const total = articulosCarrito.reduce((acc, curso) => acc + (curso.precio * curso.cantidad), 0);
    document.getElementById('total').textContent = total.toFixed(2);
}
