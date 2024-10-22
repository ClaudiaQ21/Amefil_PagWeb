document.addEventListener('DOMContentLoaded', function() {
    const favoriteLink = document.getElementById('favorito');
    const heartIcon = document.getElementById('corazon');

    if (favoriteLink && heartIcon) {
        favoriteLink.addEventListener('click', function(e) {
            e.preventDefault();

            if (heartIcon.classList.contains('fa-light')) {
                heartIcon.classList.remove('fa-light');
                heartIcon.classList.add('fa-solid');
            } else {
                heartIcon.classList.remove('fa-solid');
                heartIcon.classList.add('fa-light');
            }
        });
    }
});