document.addEventListener('DOMContentLoaded', function() {
    const enUsoSwitch = document.getElementById('id_en_uso');
    const labelEnUso = document.querySelector('label[for="id_en_uso"]');

    function toggleLabel() {
        if (enUsoSwitch.checked) {
            labelEnUso.textContent = 'En uso';
        } else {
            labelEnUso.textContent = 'Sin usar';
        }
    }

    enUsoSwitch.addEventListener('change', toggleLabel);

    // Inicializa el estado del label al cargar la página
    toggleLabel();
});

function generarQRCode() {
    // Obtén los valores del formulario que necesitas para generar el QR
    const tipo = document.querySelector('[name="tipo"]').value;
    const descripcion = document.querySelector('[name="descripcion"]').value;
    
    // Envía la solicitud al backend para generar el QR
    fetch('/generate-qr/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({
            tipo: tipo,
            descripcion: descripcion
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.qr_image) {
            const qrImage = document.getElementById('qr_image');
            qrImage.src = `data:image/png;base64,${data.qr_image}`;
            qrImage.style.display = 'block';
        }
    })
    .catch(error => console.error('Error:', error));
}

function guardarQRCode() {
    const qrImage = document.getElementById('qr_image');
    if (qrImage.src) {
        const a = document.createElement('a');
        a.href = qrImage.src;
        a.download = 'codigo_qr.png';
        a.click();
    }
}
