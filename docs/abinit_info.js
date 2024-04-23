document.addEventListener('DOMContentLoaded', function() {
    const moreLink = document.querySelector('.more-link');
    const lessLink = document.querySelector('.less-link');
    const details = document.querySelector('.details');

    moreLink.addEventListener('click', function(event) {
        event.preventDefault();
        details.style.display = 'inline';
        moreLink.style.display = 'none';
        lessLink.style.display = 'inline';
    });

    lessLink.addEventListener('click', function(event) {
        event.preventDefault();
        details.style.display = 'none';
        moreLink.style.display = 'inline';
        lessLink.style.display = 'none';
    });
});
