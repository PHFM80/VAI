async function generatePDF() {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    // Obtener la fecha actual
    const now = new Date();
    const date = `${now.getDate()}/${now.getMonth() + 1}/${now.getFullYear()}`; // Formato dd/mm/yyyy

    var firstName = document.getElementById('id_first_name').value;
    var lastName = document.getElementById('id_last_name').value;
    var email = document.getElementById('id_email').value;
    var telefono = document.getElementById('id_telefono').value;
    var rol = document.getElementById('id_rol').options[document.getElementById('id_rol').selectedIndex].text;
    var cargo = document.getElementById('id_cargo').options[document.getElementById('id_cargo').selectedIndex].text;
    var username = document.getElementById('id_username').value;

    // Texto adicional al principio
    doc.text('Reporte de Usuario', 10, 10); // Título o texto introductorio

    // Agregar la fecha
    doc.text(`Fecha: ${date}`, 10, 20); // Mostrar la fecha en el documento

    // Datos del usuario
    doc.text(`Nombre: ${firstName}`, 10, 30);
    doc.text(`Apellido: ${lastName}`, 10, 40);
    doc.text(`Email: ${email}`, 10, 50);
    doc.text(`Teléfono: ${telefono}`, 10, 60);
    doc.text(`Rol: ${rol}`, 10, 70);
    doc.text(`Cargo: ${cargo}`, 10, 80);
    doc.text(`Username: ${username}`, 10, 90);
    doc.text(`Password: vaiprocess2024`, 10, 100);

    // Texto adicional al final
    doc.text('Gracias por utilizar nuestro sistema.', 10, 110); // Mensaje de cierre o nota final

    // Guardar el documento
    doc.save('user-data.pdf');
}

