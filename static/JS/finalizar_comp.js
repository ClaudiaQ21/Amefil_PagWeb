    // // Funciones de validación
    // function checkDistrito() {
    //     const distrito = document.getElementById('id_distrito'); // Cambia 'distrito' por el ID real de tu input
    //     return distrito.value.trim() !== '';
    // }
    // function checkProvincia() {
    //     const provincia = document.getElementById('id_provincia'); // Cambia 'provincia' por el ID real de tu input
    //     return provincia.value.trim() !== '';
    // }

    // function checkDepartamento() {
    //     const departamento = document.getElementById('id_departamento'); // Cambia 'departamento' por el ID real de tu input
    //     return departamento.value.trim() !== '';
    // }
    // function validateForm() {
    //     const validName = checkName();
    //     const validFechaNacimiento = check_fechaNacimiento();
    //     const validDni = checkDni();
    //     const validPhoneNumber = checkPhoneNumber();
    //     const validAddress = checkAddress();
    //     const validReference = checkReference();
    //     const validCardNumber = checkCardNumber();
    //     const validCardHolder = checkCardHolder();
    //     const validCvv = checkCvv();
    //     const validDistrito = checkDistrito();
    //     const validProvincia = checkProvincia();
    //     const validDepartamento = checkDepartamento();
    //     // Retorna true solo si todos los campos son válidos
    //     // Verifica si todos los campos son válidos
    //     if (!validName || !validFechaNacimiento || !validDni || !validPhoneNumber ||
    //         !validAddress || !validReference || !validCardNumber || !validCardHolder ||
    //         !validCvv || !validDistrito || !validProvincia || !validDepartamento) {
    //         alert('Por favor, completa todos los campos correctamente.');
    //         return false;
    //     }
    //     // Retorna true solo si todos los campos son válidos
    //     return true;
    // }

//     // Validaciones
//     const nombreEl = document.querySelector('#nombre');
//     const fechaNacimientoEl = document.querySelector('#nacimiento');
//     const dniEl = document.querySelector('#dni');
//     const telefonoEl = document.querySelector('#telefono');
//     const addressEl = document.querySelector('#id_direccion');
//     const referenceEl = document.querySelector('#referencia');
//     const tarjetaEl = document.querySelector('#tarjeta');
//     const titularEl = document.querySelector('#titular');
//     const codigoEl = document.querySelector('#codigo');

//     const isRequired = value => value === '' ? false : true;

//     const showError = (input, message) => {
//         const formField = input.parentElement;
//         formField.classList.remove('success');
//         formField.classList.add('error');
//         const error = formField.querySelector('small');
//         error.textContent = message;
//     };

//     const showSuccess = (input) => {
//         const formField = input.parentElement;
//         formField.classList.remove('error');
//         formField.classList.add('success');
//         const error = formField.querySelector('small');
//         error.textContent = '';
//     };

//     const isNameValid = (nombre) => {
//         const re = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+(\s[a-zA-ZáéíóúÁÉÍÓÚñÑ]+)*$/;
//         return re.test(nombre);
//     };
//     const isDniNumberValid = (dni) => {
//         const re = /^\d{8}$/;
//         return re.test(dni);
//     };
//     const isPhoneNumberValid = (telefono) => {
//         const re = /^\d{9}$/;
//         return re.test(telefono);
//     };
//     const isAddressValid = (address) => {
//         const re = /^[a-zA-Z0-9\s,.'-]{5,}$/;
//         return re.test(address);
//     };
//     const isReferenceValid = (reference) => {
//         const re = /^[a-zA-Z0-9\s,.'-]{5,}$/;
//         return re.test(reference);
//     };
//     const isCardNumberValid = (tarjeta) => {
//         const re = /^(\d{4}[- ]?){3}\d{4}$/;
//         return re.test(tarjeta);
//     };
//     const isCardHolderValid = (titular) => {
//         const re = /^[a-zA-Z\s]+$/;
//         return re.test(titular);
//     };
//     const isCvvValid = (codigo) => {
//         const re = /^\d{3}$/;
//         return re.test(codigo);
//     };

//     const checkName = () => {
//         let valid = false;
//         const nombre = nombreEl.value.trim();
//         if (!isRequired(nombre)) {
//             showError(nombreEl, 'El nombre no puede estar vacío.');
//         } else if (!isNameValid(nombre)) {
//             showError(nombreEl, 'El nombre no es válido.');
//         } else {
//             showSuccess(nombreEl);
//             valid = true;
//         }
//         return valid;
//     };

//     const check_fechaNacimiento = () => {
//         let valid = false;
//         const fechaValue = fechaNacimientoEl.value.trim();

//         if (!isRequired(fechaValue)) {
//             showError(fechaNacimientoEl, 'Debe ingresar su fecha de nacimiento');
//         } else {
//             const fechaIngresada = new Date(fechaValue);
//             const fechaActual = new Date();
//             const edadMinima = 18;
//             const fechaLimite = new Date(
//                 fechaActual.getFullYear() - edadMinima,
//                 fechaActual.getMonth(),
//                 fechaActual.getDate()
//             );

//             if (isNaN(fechaIngresada.getTime())) {
//                 showError(fechaNacimientoEl, 'La fecha ingresada no es válida');
//             } else if (fechaIngresada > fechaActual) {
//                 showError(fechaNacimientoEl, 'La fecha de nacimiento no puede ser futura');
//             } else if (fechaIngresada > fechaLimite) {
//                 showError(fechaNacimientoEl, 'Debe tener al menos 18 años');
//             } else {
//                 showSuccess(fechaNacimientoEl);
//                 valid = true;
//             }
//         }
//         return valid;
//     };

//     const checkDni = () => {
//         let valid = false;
//         const dni = dniEl.value.trim();
//         if (!isRequired(dni)) {
//             showError(dniEl, 'DNI no puede estar vacío.');
//         } else if (!isDniNumberValid(dni)) {
//             showError(dniEl, 'DNI debe tener exactamente 8 dígitos.');
//         } else {
//             showSuccess(dniEl);
//             valid = true;
//         }
//         return valid;
//     };
//     const checkPhoneNumber = () => {
//         let valid = false;
//         const telefono = telefonoEl.value.trim();
//         if (!isRequired(telefono)) {
//             showError(telefonoEl, 'El número de teléfono no puede estar vacío.');
//         } else if (!isPhoneNumberValid(telefono)) {
//             showError(telefonoEl, 'El número de teléfono debe tener 9 dígitos numéricos.');
//         } else {
//             showSuccess(telefonoEl);
//             valid = true;
//         }
//         return valid;
//     };
//     const checkAddress = () => {
//         let valid = false;
//         const address = addressEl.value.trim();
//         if (!isRequired(address)) {
//             showError(addressEl, 'La dirección no puede estar vacía.');
//         } else if (!isAddressValid(address)) {
//             showError(addressEl, 'La dirección no es válida.');
//         } else {
//             showSuccess(addressEl);
//             valid = true;
//         }
//         return valid;
//     };
//     const checkReference = () => {
//         let valid = false;
//         const reference = referenceEl.value.trim();
//         if (!isRequired(reference)) {
//             showError(referenceEl, 'La referencia no puede estar vacía.');
//         } else if (!isReferenceValid(reference)) {
//             showError(referenceEl, 'La referencia no es válida.');
//         } else {
//             showSuccess(referenceEl);
//             valid = true;
//         }
//         return valid;
//     };
//     const checkCardNumber = () => {
//         let valid = false;
//         const tarjeta = tarjetaEl.value.trim();
//         if (!isRequired(tarjeta)) {
//             showError(tarjetaEl, 'El número de tarjeta no puede estar vacío.');
//         } else if (!isCardNumberValid(tarjeta)) {
//             showError(tarjetaEl, 'El número de tarjeta no es válido. Ejm: XXXX-XXXX-XXXX-XXXX');
//         } else {
//             showSuccess(tarjetaEl);
//             valid = true;
//         }
//         return valid;
//     };
//     const checkCardHolder = () => {
//         let valid = false;
//         const titular = titularEl.value.trim();
//         if (!isRequired(titular)) {
//             showError(titularEl, 'El titular de la tarjeta no puede estar vacío.');
//         } else if (!isCardHolderValid(titular)) {
//             showError(titularEl, 'El titular de la tarjeta no es válido.');
//         } else {
//             showSuccess(titularEl);
//             valid = true;
//         }
//         return valid;
//     };
//     const checkCvv = () => {
//         let valid = false;
//         const codigo = codigoEl.value.trim();
//         if (!isRequired(codigo)) {
//             showError(codigoEl, 'El código de seguridad no puede estar vacío.');
//         } else if (!isCvvValid(codigo)) {
//             showError(codigoEl, 'El código de seguridad debe tener 3.');
//         } else {
//             showSuccess(codigoEl);
//             valid = true;
//         }
//         return valid;
//     };

//     nombreEl.addEventListener('input', function () {
//         checkName();
//     });

//     fechaNacimientoEl.addEventListener('input', check_fechaNacimiento);

//     dniEl.addEventListener('input', function () {
//         checkDni();
//     });

//     telefonoEl.addEventListener('input', function () {
//         checkPhoneNumber();
//     });

//     addressEl.addEventListener('input', function () {
//         checkAddress();
//     });

//     referenceEl.addEventListener('input', function () {
//         checkReference();
//     });
//     tarjetaEl.addEventListener('input', function () {
//         checkCardNumber();
//     });

//     titularEl.addEventListener('input', function () {
//         checkCardHolder();
//     });

//     codigoEl.addEventListener('input', function () {
//         checkCvv();
//     });

