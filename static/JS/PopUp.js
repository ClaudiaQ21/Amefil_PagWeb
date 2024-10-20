document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('editarProductoForm');
    const popup = document.getElementById('confirmPopup');
    const confirmBtn = document.getElementById('confirmBtn');
    const cancelBtn = document.getElementById('cancelBtn');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        popup.style.display = 'block';
    });

    confirmBtn.addEventListener('click', function() {
        form.submit();
    });

    cancelBtn.addEventListener('click', function() {
        popup.style.display = 'none';
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const popup = document.getElementById('confirmPopup');
    const confirmBtn = document.getElementById('confirmBtn');
    const cancelBtn = document.getElementById('cancelBtn');
    let formToSubmit = null;

    // Detecta cuando se hace clic en un botón de eliminar
    document.querySelectorAll('.delete-btn').forEach(button => {
        button.addEventListener('click', function() {
            const formId = this.getAttribute('data-form-id');
            formToSubmit = document.getElementById(formId);
            popup.style.display = 'block';
        });
    });

    // Si confirma, envía el formulario de eliminación
    confirmBtn.addEventListener('click', function() {
        if (formToSubmit) {
            formToSubmit.submit();
        }
    });

    // Si cancela, cierra el pop-up
    cancelBtn.addEventListener('click', function() {
        popup.style.display = 'none';
        formToSubmit = null;
    });
});
