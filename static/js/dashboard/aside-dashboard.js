

// funcion para manejar los botones
document.addEventListener('DOMContentLoaded', function() {
    var buttons = document.querySelectorAll('.toggle-button');
    
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            var content = this.nextElementSibling;
            if (content.style.display === 'block') {
                content.style.display = 'none';
            } else {
                content.style.display = 'block';
            }
        });
    });
});

document.querySelectorAll('.toggle-button').forEach(button => {
    button.addEventListener('click', function() {
        this.classList.toggle('open');
    });
});

// mostrar datos en el main dash
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.load-content').forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault();

            const url = this.href;

            fetch(url)
                .then(response => response.text())
                .then(html => {
                    document.getElementById('main-content').innerHTML = html;
                })
                .catch(error => {
                    console.error('Error al cargar el contenido:', error);
                });
        });
    });
});
