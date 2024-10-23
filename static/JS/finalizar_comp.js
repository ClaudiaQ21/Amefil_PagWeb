function validateForm() {
    const validName = checkName();
    const validFechaNacimiento = check_fechaNacimiento();
    const validPhoneNumber = checkPhoneNumber();
    const validCardNumber = checkCardNumber();
    const validCardHolder = checkCardHolder();
    const validCvv = checkCvv();
   
    if (!validName || !validFechaNacimiento || !validPhoneNumber ||
        !validCardNumber || !validCardHolder ||
        !validCvv) {
        alert('Por favor, completa todos los campos correctamente.');
        return false;
    }
    return true;
}

// Validaciones
const nombreEl = document.querySelector('#nombre');
const fechaNacimientoEl = document.querySelector('#nacimiento');
const telefonoEl = document.querySelector('#telefono');
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
const isPhoneNumberValid = (telefono) => {
    const re = /^\d{9}$/;
    return re.test(telefono);
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

const check_fechaNacimiento = () => {
    let valid = false;
    const fechaValue = fechaNacimientoEl.value.trim();

    if (!isRequired(fechaValue)) {
        showError(fechaNacimientoEl, 'Debe ingresar su fecha de nacimiento');
    } else {
        const fechaIngresada = new Date(fechaValue);
        const fechaActual = new Date();
        const edadMinima = 18;
        const fechaLimite = new Date(
            fechaActual.getFullYear() - edadMinima,
            fechaActual.getMonth(),
            fechaActual.getDate()
        );

        if (isNaN(fechaIngresada.getTime())) {
            showError(fechaNacimientoEl, 'La fecha ingresada no es válida');
        } else if (fechaIngresada > fechaActual) {
            showError(fechaNacimientoEl, 'La fecha de nacimiento no puede ser futura');
        } else if (fechaIngresada > fechaLimite) {
            showError(fechaNacimientoEl, 'Debe tener al menos 18 años');
        } else {
            showSuccess(fechaNacimientoEl);
            valid = true;
        }
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
const checkCardNumber = () => {
    let valid = false;
    const tarjeta = tarjetaEl.value.trim();
    if (!isRequired(tarjeta)) {
        showError(tarjetaEl, 'El número de tarjeta no puede estar vacío.');
    } else if (!isCardNumberValid(tarjeta)) {
        showError(tarjetaEl, 'El número de tarjeta no es válido. Ejm: XXXX-XXXX-XXXX-XXXX');
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

nombreEl.addEventListener('input', function () {
    checkName();
});

fechaNacimientoEl.addEventListener('input', check_fechaNacimiento);

telefonoEl.addEventListener('input', function () {
    checkPhoneNumber();
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

