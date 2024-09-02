window.onload = function () {
    const total = localStorage.getItem('totalAmount');
    const totalInput = document.getElementById('totalInput');
    const precioEnvioInput = document.getElementById('precioEnvio');

    function actualizarTotalConEnvio() {
        const envioTexto = precioEnvioInput.value;

        const envio = parseFloat(envioTexto.replace('S/. ', '')) || 0;
        const totalCarrito = parseFloat(total) || 0;

        if (!isNaN(envio) && !isNaN(totalCarrito)) {
            const totalConEnvio = totalCarrito + envio;
            totalInput.value = `S/. ${totalConEnvio.toFixed(2)}`; 
        }
    }

    if (total !== null) {
        totalInput.value = `S/. ${parseFloat(total).toFixed(2)}`; 
        actualizarTotalConEnvio();
    }

    document.getElementById('departamento').addEventListener('change', actualizarTotalConEnvio);
    document.getElementById('provincia').addEventListener('change', actualizarTotalConEnvio);
    document.getElementById('distrito').addEventListener('change', actualizarTotalConEnvio);
};

document.addEventListener('DOMContentLoaded', function () {
    const preciosEnvio = {
        Lima: {
            Lima: 5.00,
            Miraflores: 7.00
        },
        Arequipa: {
            Arequipa: 10.00,
            Yanahuara: 12.00
        },
        Cusco: {
            Cusco: 8.00,
            Santiago: 9.50
        }
    };

    const departamentoSelect = document.getElementById('departamento');
    const provinciaSelect = document.getElementById('provincia');
    const distritoSelect = document.getElementById('distrito');
    const precioEnvioInput = document.getElementById('precioEnvio');

    function actualizarPrecioEnvio() {
        const departamento = departamentoSelect.value;
        const distrito = distritoSelect.value;

        if (preciosEnvio[departamento] && preciosEnvio[departamento][distrito]) {
            precioEnvioInput.value = `S/. ${preciosEnvio[departamento][distrito].toFixed(2)}`;
        } else {
            precioEnvioInput.value = `S/. 0.00`;
        }
        actualizarTotalConEnvio();
    }

    departamentoSelect.addEventListener('change', actualizarPrecioEnvio);
    provinciaSelect.addEventListener('change', actualizarPrecioEnvio);
    distritoSelect.addEventListener('change', actualizarPrecioEnvio);
});


document.addEventListener('DOMContentLoaded', function () {
    const nombreEl = document.querySelector('#nombre');
    const dniEl = document.querySelector('#dni');
    const telefonoEl = document.querySelector('#telefono');
    const addressEl = document.querySelector('#direccion');
    const referenceEl = document.querySelector('#referencia');
    const tarjetaEl = document.querySelector('#tarjeta');
    const titularEl = document.querySelector('#titular');
    const codigoEl = document.querySelector('#codigo');

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
    const isPhoneNumberValid = (telefono) => {
        const re = /^\d{9}$/;
        return re.test(telefono);
    };
    const isAddressValid = (address) => {
        const re = /^[a-zA-Z0-9\s,.'-]{5,}$/;
        return re.test(address);
    };
    const isReferenceValid = (reference) => {
        const re = /^[a-zA-Z0-9\s,.'-]{5,}$/;
        return re.test(reference);
    };
    const isCardNumberValid = (tarjeta) => {
        const re = /^(\d{4}[- ]?){3}\d{4}$/;
        return re.test(tarjeta);
    };
    const isCardHolderValid = (titular) => {
        const re = /^[a-zA-Z\s]+$/;
        return re.test(titular);
    };
    const isCvvValid = (codigo) => {
        const re = /^\d{3}$/;
        return re.test(codigo);
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
    const checkPhoneNumber = () => {
        let valid = false;
        const telefono = telefonoEl.value.trim();
        if (!isRequired(telefono)) {
            showError(telefonoEl, 'El número de teléfono no puede estar vacío.');
        } else if (!isPhoneNumberValid(telefono)) {
            showError(telefonoEl, 'El número de teléfono debe tener 9 dígitos numéricos.');
        } else {
            showSuccess(telefonoEl);
            valid = true;
        }
        return valid;
    };
    const checkAddress = () => {
        let valid = false;
        const address = addressEl.value.trim();
        if (!isRequired(address)) {
            showError(addressEl, 'La dirección no puede estar vacía.');
        } else if (!isAddressValid(address)) {
            showError(addressEl, 'La dirección no es válida.');
        } else {
            showSuccess(addressEl);
            valid = true;
        }
        return valid;
    };
    const checkReference = () => {
        let valid = false;
        const reference = referenceEl.value.trim();
        if (!isRequired(reference)) {
            showError(referenceEl, 'La referencia no puede estar vacía.');
        } else if (!isReferenceValid(reference)) {
            showError(referenceEl, 'La referencia no es válida.');
        } else {
            showSuccess(referenceEl);
            valid = true;
        }
        return valid;
    };
    const checkCardNumber = () => {
        let valid = false;
        const tarjeta = tarjetaEl.value.trim();
        if (!isRequired(tarjeta)) {
            showError(tarjetaEl, 'El número de tarjeta no puede estar vacío.');
        } else if (!isCardNumberValid(tarjeta)) {
            showError(tarjetaEl, 'El número de tarjeta no es válido.');
        } else {
            showSuccess(tarjetaEl);
            valid = true;
        }
        return valid;
    };
    const checkCardHolder = () => {
        let valid = false;
        const titular = titularEl.value.trim();
        if (!isRequired(titular)) {
            showError(titularEl, 'El titular de la tarjeta no puede estar vacío.');
        } else if (!isCardHolderValid(titular)) {
            showError(titularEl, 'El titular de la tarjeta no es válido.');
        } else {
            showSuccess(titularEl);
            valid = true;
        }
        return valid;
    };
    const checkCvv = () => {
        let valid = false;
        const codigo = codigoEl.value.trim();
        if (!isRequired(codigo)) {
            showError(codigoEl, 'El código de seguridad no puede estar vacío.');
        } else if (!isCvvValid(codigo)) {
            showError(codigoEl, 'El código de seguridad debe tener 3.');
        } else {
            showSuccess(codigoEl);
            valid = true;
        }
        return valid;
    };

    document.querySelector('#miFormulario').addEventListener('submit', function (e) {
        e.preventDefault();
        const isNameValid = checkName();
        const isDniValid = checkDni();
        const isPhoneValid = checkPhoneNumber();
        const isAddressValid = checkAddress();
        const isReferenceValid = checkReference();
        const isCardNumberValid = checkCardNumber();
        const isCardHolderValid = checkCardHolder();
        const isCvvValid = checkCvv();
        if (isNameValid && isDniValid && isPhoneValid && isAddressValid && isReferenceValid && isCardNumberValid && isCardHolderValid && isCvvValid) {
            alert('Formulario válido');
            formulario.reset();
        }
    });

    nombreEl.addEventListener('input', function () {
        checkName();
    });

    dniEl.addEventListener('input', function () {
        checkDni();
    });

    telefonoEl.addEventListener('input', function () {
        checkPhoneNumber();
    });

    addressEl.addEventListener('input', function () {
        checkAddress();
    });

    referenceEl.addEventListener('input', function () {
        checkReference();
    });
    tarjetaEl.addEventListener('input', function () {
        checkCardNumber();
    });

    titularEl.addEventListener('input', function () {
        checkCardHolder();
    });

    codigoEl.addEventListener('input', function () {
        checkCvv();
    });

    const resetValidation = () => {
        const formFields = [
            nombreEl, dniEl, telefonoEl, addressEl, referenceEl, tarjetaEl, titularEl, codigoEl
        ];

        formFields.forEach(field => {
            const formField = field.parentElement;
            formField.classList.remove('success', 'error');
            const error = formField.querySelector('small');
            error.textContent = '';
        });
    };

    document.querySelector('#compraModal .btn-primary').addEventListener('click', function () {
        document.querySelector('#miFormulario').reset(); 
        resetValidation(); 

        localStorage.removeItem('totalAmount'); 

        document.getElementById('totalInput').value = 'S/. 0.00';
        document.getElementById('precioEnvio').value = 'S/. 0.00';
    });
});
