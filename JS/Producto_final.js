$(document).ready(function() {
    $('#mas').click(function() {
        let currentValue = parseInt($('#counter-value').val());
        $('#counter-value').val(currentValue + 1);
    });

    $('#menos').click(function() {
        let currentValue = parseInt($('#counter-value').val());
        if (currentValue > 1) {
            $('#counter-value').val(currentValue - 1);
        }
    });

    let currentIndex = 0;
    const reseña = $('.reseña');
    const total = reseña.length;

    $('#next').click(function() {
        if (currentIndex < total- 1) {
            $(reseña[currentIndex]).hide();
            currentIndex++;
            $(reseña[currentIndex]).show();
        }
        updateButtons();
    });

    $('#prev').click(function() {
        if (currentIndex > 0) {
            $(reseña[currentIndex]).hide();
            currentIndex--;
            $(reseña[currentIndex]).show();
        }
        updateButtons();
    });

    function updateButtons() {
        $('#prev').prop('disabled', currentIndex === 0);
        $('#next').prop('disabled', currentIndex === total - 1);
    }

    updateButtons();

    const mainImage = document.getElementById('main-image');
    const thumbnails = document.querySelectorAll('.thumbnail');

    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function() {
            const newMainImageSrc = this.src;

            // Actualizar la imagen principal
            mainImage.src = newMainImageSrc;

            // Ajustar las miniaturas
            thumbnails.forEach(thumb => {
                thumb.style.width = '15%';
                thumb.style.height = '65%';
                thumb.removeAttribute('data-main');
            });

            this.style.width = '25%';
            this.style.height = '85%';
            this.setAttribute('data-main', 'true');

            // Reordenar las miniaturas para mantener la nueva miniatura principal en el centro
                const imgSec = document.querySelector('.img_sec');
                imgSec.innerHTML = '';  // Vaciar el contenedor de miniaturas

                // Nuevo orden: miniatura principal en el medio
                const newThumbnails = Array.from(thumbnails).filter(thumb => !thumb.dataset.main);
                const mainThumbnail = this.cloneNode(true);
                imgSec.appendChild(newThumbnails[0]);
                imgSec.appendChild(mainThumbnail);
                imgSec.appendChild(newThumbnails[1]);

                // Actualizar la referencia de thumbnails
                newThumbnails[0].addEventListener('click', updateMainImage);
                mainThumbnail.addEventListener('click', updateMainImage);
                newThumbnails[1].addEventListener('click', updateMainImage);
            
        });
    });

    const favButton = document.getElementById('favoritos');

    favButton.addEventListener('click', function() {
        if (this.classList.contains('far')) {
            this.classList.remove('far');
            this.classList.add('fas');
        } else {
            this.classList.remove('fas');
            this.classList.add('far');
        }
    });
    

    $('#mas_carr').click(function() {
        if ($(this).text() === 'Añadir al carrito') {
            $(this).text('Quitar del carrito');
        } else {
            $(this).text('Añadir al carrito');
        }
    });

    
});
