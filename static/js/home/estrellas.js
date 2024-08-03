document.addEventListener('DOMContentLoaded', function () {
    const portada = document.querySelector('.portada');
    const numberOfStars = 700; // Número de estrellas

    const colors = ['#ffffff', '#ffcc00', '#ff6699', '#66ccff', '#99ff99']; // define una lista de colores, para usarla debera estar deshabilitado el color en el css de star
    // Define un array de animaciones


    for (let i = 0; i < numberOfStars; i++) {
        const star = document.createElement('div');
        star.classList.add('star');
        
        // Generar posiciones aleatorias dentro de la sección portada
        const randomX = Math.random() * portada.clientWidth;
        const randomY = Math.random() * portada.clientHeight;
        const randomSize = Math.random() * 6 + 1; // Tamaño de 1 a x píxeles
        const randomDuration = Math.random() * 15 + 10; // Duración de 10 a 25 segundos
        //const randomColor = colors[Math.floor(Math.random() * colors.length)]; // Color aleatorio


        star.style.left = `${randomX}px`;
        star.style.top = `${randomY}px`;
        star.style.width = `${randomSize}px`;
        star.style.height = `${randomSize}px`;
        //star.style.backgroundColor = randomColor; // Color aleatorio
        star.style.animationDuration = `${randomDuration}s`;

        portada.appendChild(star);
    }
});
