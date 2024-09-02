const emailC = document.querySelector('#email');
const form = document.querySelector('#signup');

const Req = value => value === '' ? false : true;

const email_valido = (email) => {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@(gmail\.com|hotmail\.com)$/;

    return re.test(email);
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

form.addEventListener('submit', function (e) {
    // prevent the form from submitting
    e.preventDefault();

    // validate forms
    let emailValido = check_email();

    let isFormValid = 
        emailValido;

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
        
        case 'email':
            check_email();
            break;
    }
}));