document.addEventListener('DOMContentLoaded', function () {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', filterProducts);
    });

    function filterProducts() {
        const selectedCategories = Array.from(checkboxes)
            .filter(checkbox => checkbox.checked)
            .map(checkbox => checkbox.value);

        const products = document.querySelectorAll('.cont_pro');

        products.forEach(product => {
            const category = product.getAttribute('data-category');
            if (selectedCategories.length === 0 || selectedCategories.includes(category)) {
                product.parentElement.style.display = '';
            } else {
                product.parentElement.style.display = 'none';
            }
        });
    }
});