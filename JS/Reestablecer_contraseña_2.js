const passwordC = document.querySelector('#new-password');
const confirmC = document.querySelector('#confirm-password');

const form = document.querySelector('#signup');

const Req = value => value === '' ? false : true;

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
    let 
        passwordValido = check_password(),
        confirmValido = check_confirm();

    let isFormValid = 
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
        
        case 'new-password':
            check_password();
            break;
        case 'confirm-password':
            check_confirm();
            break;
    }
}));