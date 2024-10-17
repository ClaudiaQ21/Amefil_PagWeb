//validacion
const nombresC = document.querySelector('#nombre');
const apellidospaC = document.querySelector('#apellido_p');
const apellidosmaC = document.querySelector('#apellido_m');
const emailC = document.querySelector('#correo');
const telefonoC = document.querySelector('#telefono');
const errorDisplay2 = document.getElementById('#genero-error'); // Usar el <small> para mostrar el mensaje de error
const fecha = document.getElementById('nacimiento');
const passwordC = document.querySelector('#contrasena');
const confirmC = document.querySelector('#confirm-password');
const checkbox = document.getElementById('term');
const errorDisplay = document.getElementById('checkbox-error'); // Usar el id del <small>
// const errorDisplay3 = document.getElementById('fecha-error'); // Usar el <small> para mostrar el mensaje de error



const form = document.querySelector('#signup');


const Req = value => value === '' ? false : true;

const limite = (length, min, max) => length < min || length > max ? false : true;

const nomb_valido = (nombres) => {
    const nomb = /^[A-Za-zÀ-ÖØ-öø-ÿ' -]+$/;
    return nomb.test(nombres);
};

const ap_valido_pa = (apellidos) => {
    const nomb = /^[A-Za-zÀ-ÖØ-öø-ÿ' -]+$/;
    return nomb.test(apellidos);
};

const ap_valido_ma = (apellidos) => {
    const nomb = /^[A-Za-zÀ-ÖØ-öø-ÿ' -]+$/;
    return nomb.test(apellidos);
};
const email_valido = (email) => {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@(gmail\.com|hotmail\.com)$/;

    return re.test(email);
};

const telefono_valido = (telefono) => {
    const nomb = /^9[0-9]{8}$/;
    return nomb.test(telefono);
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
};

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
};
const check_apellidos_pa = () => {

    let valid = false;
    const min = 3,
        max = 50;
    const apellidos = apellidospaC.value.trim();

    if (!Req(apellidos)) {
        showError(apellidospaC, '*Campo obligatorio');
    } else if (!limite(apellidos.length, min, max)) {
        showError(apellidospaC, `Debe ingresar un apellido válido de ${min} y ${max} caracteres`);
    } else if (!ap_valido_pa(apellidos)) {
        showError(apellidospaC, `Debe ingresar un apellido válido de ${min} y ${max} caracteres`);
    } else {
        showSuccess(apellidospaC);
        valid = true;
    }
    return valid;
};

const check_apellidos_ma = () => {

    let valid = false;
    const min = 3,
        max = 50;
    const apellidos = apellidosmaC.value.trim();

    if (!Req(apellidos)) {
        showError(apellidosmaC, '*Campo obligatorio');
    } else if (!limite(apellidos.length, min, max)) {
        showError(apellidosmaC, `Debe ingresar un apellido válido de ${min} y ${max} caracteres`);
    } else if (!ap_valido_ma(apellidos)) {
        showError(apellidosmaC, `Debe ingresar un apellido válido de ${min} y ${max} caracteres`);
    } else {
        showSuccess(apellidosmaC);
        valid = true;
    }
    return valid;
};

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
};

const check_telefono = () => {
    let valid = false;
    const telefono = telefonoC.value.trim();
    if (!Req(telefono)) {
        showError(telefonoC, '*Campo obligatorio');
    } else if (!telefono_valido(telefono)) {
        showError(telefonoC, 'Debe ingresar un teléfono válido');
    } else {
        showSuccess(telefonoC);
        valid = true;
    }
    return valid;
};



const validateGenero = () => {
    let valid = false;
    const genero = document.getElementById('genero');
    const selectedValue = genero.value;

    if (selectedValue === "seleccionar") {
        showError(genero, '*Debe seleccionar un género');
    } else {
        showSuccess(genero);
        valid = true;
    }

    return valid;
};







const check_fechaNacimiento = () => {
        let valid = false;
        const fechaValue = fecha.value.trim(); // Obtener el valor del campo de fecha
    
        if (!Req(fechaValue)) {
            showError(fecha, '*Debe ingresar su fecha de nacimiento*');
        } else {
            const fechaIngresada = new Date(fechaValue);
            const fechaActual = new Date();
            const edadMinima = 18; // Edad mínima requerida (opcional)
            const fechaLimite = new Date(
                fechaActual.getFullYear() - edadMinima,
                fechaActual.getMonth(),
                fechaActual.getDate()
            );
    
            // Verificar que la fecha no sea futura
            if (fechaIngresada >= fechaActual) {
                showError(fecha, '*La fecha de nacimiento no puede ser futura*');
            } 
            // Verificar que el usuario tenga al menos 18 años
            else if (fechaIngresada > fechaLimite) {
                showError(fecha, '*Debe tener al menos 18 años*');
            } 
            else {
                // Si la fecha es válida, mostrar mensaje de éxito
                showSuccess(fecha);
                valid = true;
            }
        }
    
        return valid;
    };
    


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

const checkbox_confirm = () => {
    let valid = false;


    // Verificar si el checkbox está marcado
    let checkboxValido = checkbox.checked;
    if (!checkboxValido) {
        showError(errorDisplay, '*Debe aceptar los Términos y Condiciones*');
    } else {
        showSuccess(errorDisplay);
        valid = true;
    }

    return valid;
};

form.addEventListener('submit', function (e) {
    e.preventDefault();

    // validar el formulario
    let nombreValido = check_nombre(),
        apellidoPaValido = check_apellidos_pa(),
        apellidoMaValido = check_apellidos_ma(),
        emailValido = check_email(),
        telefonoValido = check_telefono(),
        generoValido = validateGenero(),
        fechaValida = check_fechaNacimiento(),
        passwordValido = check_password(),
        confirmValido = check_confirm(),
        checkboxValid = checkbox_confirm();

    let isFormValid = nombreValido &&
        apellidoPaValido &&
        apellidoMaValido &&
        emailValido &&
        telefonoValido &&
        generoValido &&
        fechaValida &&
        passwordValido &&
        confirmValido &&
        checkboxValid;

    if (isFormValid) {
        form.submit(); // Envía el formulario si es válido
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
        case 'nombre':
            check_nombre();
            break;
        case 'apellido_p':
            check_apellidos_pa();
            break;
        case 'apellido_m':
            check_apellidos_ma();
            break;
        case 'correo':
            check_email();
            break;
        case 'telefono':
            check_telefono();
            break;
        case 'genero':
            validateGenero();
            break;
        case 'nacimiento':
            check_fechaNacimiento();
            break;
        case 'contrasena':
            check_password();
            break;
        case 'confirm-password':
            check_confirm();
            break;
        case 'term':
            checkbox_confirm();
            break;
    }
}));

