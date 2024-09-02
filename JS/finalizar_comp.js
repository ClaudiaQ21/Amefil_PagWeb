window.onload = function () {
    const total = localStorage.getItem('totalAmount');

    if (total !== null) {
        document.getElementById('totalInput').value = total;
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const nombreEl = document.querySelector('#nombre');
    const dniEl = document.querySelector('#dni');

    const isRequired = value => value === '' ? false : true;

    const showError = (input, message) => {
        const formField = input.parentElement;
        formField.classList.remove('success');
        formField.classList.add('error');
        const error = formField.querySelector('small');
        error.textContent = message;
    };

    const showSuccess = (input) => {
        const formField = input.parentElement;
        formField.classList.remove('error');
        formField.classList.add('success');
        const error = formField.querySelector('small');
        error.textContent = '';
    };

    const isNameValid = (nombre) => {
        const re = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+(\s[a-zA-ZáéíóúÁÉÍÓÚñÑ]+)*$/;
        return re.test(nombre);
    };

    const isDniNumberValid = (dni) => {
        const re = /^\d{8}$/;
        return re.test(dni);
    };

    const checkName = () => {
        let valid = false;
        const nombre = nombreEl.value.trim();
        if (!isRequired(nombre)) {
            showError(nombreEl, 'El nombre no puede estar vacío.');
        } else if (!isNameValid(nombre)) {
            showError(nombreEl, 'El nombre no es válido.');
        } else {
            showSuccess(nombreEl);
            valid = true;
        }
        return valid;
    };

    const checkDni = () => {
        let valid = false;
        const dni = dniEl.value.trim();
        if (!isRequired(dni)) {
            showError(dniEl, 'DNI no puede estar vacío.');
        } else if (!isDniNumberValid(dni)) {
            showError(dniEl, 'DNI debe tener exactamente 8 dígitos.');
        } else {
            showSuccess(dniEl);
            valid = true;
        }
        return valid;
    };

    document.querySelector('#miFormulario').addEventListener('submit', function (e) {
        e.preventDefault(); 
        const isNameValid = checkName(); 
        const isDniValid = checkDni(); 
        if (isNameValid && isDniValid) {
            alert('Formulario válido');
        }
    });

    nombreEl.addEventListener('input', function () {
        checkName(); 
    });

    dniEl.addEventListener('input', function () {
        checkDni(); 
    });
});
