

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

