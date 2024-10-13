//validacion
const nombresC = document.querySelector('#nombres');
const apellidosC = document.querySelector('#apellidos');
const emailC = document.querySelector('#email');
const passwordC = document.querySelector('#password');
const confirmC = document.querySelector('#confirm-password');

const form = document.querySelector('#signup');


const Req = value => value === '' ? false : true;

const limite = (length, min, max) => length < min || length > max ? false : true;

const nomb_valido = (nombres) => {
    const nomb = /^[A-Za-zÀ-ÖØ-öø-ÿ' -]+$/;
    return nomb.test(nombres);
}

const ap_valido = (apellidos) => {
    const nomb = /^[A-Za-zÀ-ÖØ-öø-ÿ' -]+$/;
    return nomb.test(apellidos);
}

const email_valido = (email) => {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@(gmail\.com|hotmail\.com)$/;

    return re.test(email);
};

const contraseña_valida = (password) => {
    const re = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
    return re.test(password);
};

const showError = (input, message) => {
    // get the form-field element
    const formField = input.parentElement;
    // add the error class
    formField.classList.remove('success');
    formField.classList.add('error');

    // show the error message
    const error = formField.querySelector('small');
    error.textContent = message;
};

const showSuccess = (input) => {
    // get the form-field element
    const formField = input.parentElement;

    // remove the error class
    formField.classList.remove('error');
    formField.classList.add('success');

    // hide the error message
    const error = formField.querySelector('small');
    error.textContent = '';
}

const check_nombre = () => {

    let valid = false;
    const min = 3,
        max = 50;
    const nombres = nombresC.value.trim();

    if (!Req(nombres)) {
        showError(nombresC, '*Campo obligatorio');
    } else if (!limite(nombres.length, min, max)) {
        showError(nombresC, `Debe ingresar un nombre válido de ${min} y ${max} caracteres`);
    } else if (!nomb_valido(nombres)) {
        showError(nombresC, `Debe ingresar un nombre válido`);
    }
    else {
        showSuccess(nombresC);
        valid = true;
    }
    return valid;
}
const check_apellidos = () => {

    let valid = false;
    const min = 3,
        max = 50;
    const apellidos = apellidosC.value.trim();

    if (!Req(apellidos)) {
        showError(apellidosC, '*Campo obligatorio');
    } else if (!limite(apellidos.length, min, max)) {
        showError(apellidosC, `Debe ingresar un apellido válido de ${min} y ${max} caracteres`);
    } else if (!ap_valido(apellidos)) {
        showError(apellidosC, `Debe ingresar un apellido válido de ${min} y ${max} caracteres`);
    } else {
        showSuccess(apellidosC);
        valid = true;
    }
    return valid;
}


const check_email = () => {
    let valid = false;
    const email = emailC.value.trim();
    if (!Req(email)) {
        showError(emailC, '*Campo obligatorio');
    } else if (!email_valido(email)) {
        showError(emailC, 'Debe ingresar un email válido');
    } else {
        showSuccess(emailC);
        valid = true;
    }
    return valid;
}

const check_password = () => {
    let valid = false;
    const password = passwordC.value.trim();
    if (!Req(password)) {
        showError(passwordC, '*Campo obligatorio');
    } else if (!contraseña_valida(password)) {
        showError(passwordC, 'Debe ingresar una contraseña válida de mínimo: 8 carácteres, 1 mayúscula, 1 minúscula y 1 carácter especial (!@#$%^&*)');
    } else {
        showSuccess(passwordC);
        valid = true;
    }
    return valid;
}

const check_confirm = () => {
    let valid = false;
    // check confirm password
    const confirmPassword = confirmC.value.trim();
    const password = passwordC.value.trim();

    if (!Req(confirmPassword)) {
        showError(confirmC, '*Por favor ingrese su contraseña otra vez*');
    } else if (password !== confirmPassword) {
        showError(confirmC, 'Su contraseña no concuerda');
    } else {
        showSuccess(confirmC);
        valid = true;
    }

    return valid;
};

form.addEventListener('submit', function (e) {
    // prevent the form from submitting
    e.preventDefault();

    // validate forms
    let nombreValido = check_nombre(),
        apellidoValido = check_apellidos(),
        emailValido = check_email(),
        passwordValido = check_password(),
        confirmValido = check_confirm();

    let isFormValid = nombreValido &&
        apellidoValido &&
        emailValido &&
        passwordValido && confirmValido;

    // submit to the server if the form is valid
    if (isFormValid) {

    }
});

const debounce = (fn, delay = 500) => {
    let timeoutId;
    return (...args) => {
        // cancel the previous timer
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        // setup a new timer
        timeoutId = setTimeout(() => {
            fn.apply(null, args)
        }, delay);
    };
};

form.addEventListener('input', debounce(function (e) {
    switch (e.target.id) {
        case 'nombres':
            check_nombre();
            break;
        case 'apellidos':
            check_apellidos();
            break;
        case 'email':
            check_email();
            break;
        case 'password':
            check_password();
            break;
        case 'confirm-password':
            check_confirm();
            break;
    }
}));