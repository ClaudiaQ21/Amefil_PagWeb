const emailC = document.querySelector('#email');
const passwordC = document.querySelector('#password');
const form = document.querySelector('#signup');

const Req = value => value.trim() !== '';

const email_valido = (email) => {
    const re = /^[^\s@]+@(amefil\.com|gmail\.com|hotmail\.com)$/;
    return re.test(email);
};

const contraseña_valida = (password) => {
    const re = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\\$%\\^&\\*_:])(?=.{8,})");
    return re.test(password);
};

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

const validateEmail = () => {
    let valid = false;
    const email = emailC.value.trim();

    if (!Req(email)) {
        showError(emailC, '*Campo obligatorio');
    } else if (!email_valido(email)) {
        showError(emailC, 'Debe ingresar un correo válido');
    } else {
        showSuccess(emailC);
        valid = true;
    }

    return valid;
};

const check_password = () => {
    let valid = false;
    const password = passwordC.value.trim();

    if (!Req(password)) {
        showError(passwordC, '*Campo obligatorio');
    } else if (!contraseña_valida(password)) {
        showError(passwordC, 'Debe ingresar una contraseña válida');
    } else {
        showSuccess(passwordC);
        valid = true;
    }

    return valid;
};

form.addEventListener('submit', function (e) {
    e.preventDefault(); // Evita el envío del formulario

    let emailValido = validateEmail(),
        passwordValido = check_password();

    let isFormValid = emailValido && passwordValido;

    if (isFormValid) {
        form.submit(); // Enviar el formulario si es válido
    }
});

const debounce = (fn, delay = 500) => {
    let timeoutId;
    return (...args) => {
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        timeoutId = setTimeout(() => {
            fn.apply(null, args);
        }, delay);
    };
};

form.addEventListener('input', debounce(function (e) {
    switch (e.target.id) {
        case 'email':
            validateEmail();
            break;
        case 'password':
            check_password();
            break;
    }
}));
