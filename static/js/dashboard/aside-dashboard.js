document.addEventListener('DOMContentLoaded', function() {
    var buttons = document.querySelectorAll('.toggle-button');
    
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            var content = this.nextElementSibling;
            content.style.display = content.style.display === 'block' ? 'none' : 'block';
            
            // Alternar clase 'open' para la rotación de la flecha
            this.classList.toggle('open');
        });
    });
});


