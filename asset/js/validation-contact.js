document.querySelector("form").addEventListener("submit", function (e) {
    const nombre = document.getElementById("nombreApellido").value.trim();
    const mensaje = document.getElementById("mensaje").value.trim();
    
    if (!nombre) {
        alert("Por favor, complete el campo de Nombre y Apellido.");
        e.preventDefault();
    }

    if (!mensaje) {
        alert("El campo Mensaje no puede estar vacío.");
        e.preventDefault();
    }
});

const radios = document.querySelectorAll('input[name="contacto"]');
document.querySelector("form").addEventListener("submit", function (e) {
    let selected = false;
    radios.forEach(radio => {
        if (radio.checked) selected = true;
    });

    if (!selected) {
        alert("Seleccione un método de contacto.");
        e.preventDefault();
    }
});

document.querySelector("form").addEventListener("submit", function (e) {
    if (!this.checkValidity()) {
        alert("Por favor, complete todos los campos correctamente.");
        e.preventDefault();
    }
});



const form = document.querySelector("form");
const tabla = document.getElementById("tabla-preferencias").querySelector("tbody");

form.addEventListener("submit", function (e) {
  e.preventDefault();


const nombreApellido = document.getElementById("nombreapellido").value;
// const correoElectronico = document.getElementById("correoelectronico").value;
// const telefono = document.getElementById("telefono").value;
const mensaje = document.getElementById("mensaje").value;
const diaPreferido = document.getElementById("dia-preferido").value;
const horarioPreferido = document.querySelector("select").value;

  // Crear una fila
const nuevaFila = document.createElement("tr");
nuevaFila.innerHTML = `
    <td>${nombreApellido}</td>
    <td>${mensaje}</td>
    <td>${diaPreferido}</td>
    <td>${horarioPreferido}</td>
    `;
    tabla.appendChild(nuevaFila);
    form.reset();
    alert("¡La preferencia ha sido registrada!");
});
