document.querySelectorAll('.toggle-password').forEach(toggle => {
    toggle.addEventListener('click', function() {
        const passwordField = this.previousElementSibling;
        const closedEye = this.querySelector('.closed-eye');
        const openEye = this.querySelector('.open-eye');

        if (passwordField.getAttribute('type') === 'password') {
            passwordField.setAttribute('type', 'text');
            closedEye.classList.add('hidden');
            openEye.classList.remove('hidden');
        } else {
            passwordField.setAttribute('type', 'password');
            closedEye.classList.remove('hidden');
            openEye.classList.add('hidden');
        }
    });
});