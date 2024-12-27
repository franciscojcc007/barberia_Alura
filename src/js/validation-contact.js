document.querySelector("form").addEventListener("submit", function (e) {
  const $firsName = document.getElementById("first-name-surname").value.trim();
  const $message = document.getElementById("mensaje").value.trim();

  if (!$firsName) {
    alert("Por favor, complete el campo de Nombre y Apellido.");
    e.preventDefault();
  }

  if (!$message) {
    alert("El campo Mensaje no puede estar vacío.");
    e.preventDefault();
  }
});

const radios = document.querySelectorAll('input[name="contact"]');
document.querySelector("form").addEventListener("submit", function (e) {
  let selected = false;
  radios.forEach((radio) => {
    if (radio.checked) selected = true;
  });

  if (!selected) {
    alert("Seleccione un método de contact.");
    e.preventDefault();
  }
});

document.querySelector("form").addEventListener("submit", function (e) {
  if (!this.checkValidity()) {
    alert("Por favor, complete todos los campos correctamente.");
    e.preventDefault();
  }
});
