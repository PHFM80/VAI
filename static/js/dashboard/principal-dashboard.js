document.addEventListener("DOMContentLoaded", function() {
    const loadContentLinks = document.querySelectorAll('.load-content');

    loadContentLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const url = this.href;

            fetch(url)
                .then(response => response.text())
                .then(html => {
                    document.getElementById('main-content').innerHTML = html;
                })
                .catch(error => console.error('Error al cargar el contenido:', error));
        });
    });
});