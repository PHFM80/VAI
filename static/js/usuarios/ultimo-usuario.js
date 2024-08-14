// ultimo-usuario.js
function generatePDF() {
    // Extraer los datos del HTML
    const nombre = document.querySelector('p').innerText.split(': ')[1];
    const apellido = document.querySelector('p:nth-of-type(2)').innerText.split(': ')[1];
    const email = document.querySelector('p:nth-of-type(3)').innerText.split(': ')[1];
    const telefono = document.querySelector('p:nth-of-type(4)').innerText.split(': ')[1];
    const cargo = document.querySelector('p:nth-of-type(5)').innerText.split(': ')[1];
    const username = document.querySelector('p:nth-of-type(6)').innerText.split(': ')[1];


    // Crear el documento PDF
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    // Agregar contenido al PDF

    doc.text(`Fecha: ${new Date().toLocaleDateString()}`, 60, 10);
    doc.text(`Datos del Usuario`, 10, 20);
    doc.text(`Nombre: ${nombre}`, 10, 30);
    doc.text(`Apellido: ${apellido}`, 10, 40);
    doc.text(`Email: ${email}`, 10, 50);
    doc.text(`Teléfono: ${telefono}`, 10, 60);
    doc.text(`Cargo: ${cargo}`, 10, 70);
    doc.text(`Nombre de Usuario: ${username}`, 10, 80);
    doc.text(`Password: vaiprocess2024`, 10, 90);
    doc.text(`Por su seguridad recuerde cambiar el password.`, 10, 100);
    doc.text(`Fin de los Datos`, 10, 110);

    // Guardar el archivo PDF
    doc.save(`${username}-datos.pdf`);
}
