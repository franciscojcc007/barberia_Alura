const phoneInput = document.querySelector("#phone");

// Inicializar intl-tel-input
const iti = window.intlTelInput(phoneInput, {
  initialCountry: "auto", // Detecta automáticamente el país
  geoIpLookup: (callback) => {
    fetch("https://ipinfo.io?token=<TU_TOKEN_AQUÍ>") // Reemplaza con tu token
      .then((response) => response.json())
      .then((data) => callback(data.country))
      .catch(() => callback("us")); // Por defecto, USA
  },
  utilsScript:
    "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.19/js/utils.js",
});

// // Validar el número de teléfono al salir del input
// phoneInput.addEventListener("blur", () => {
//   if (iti.isValidNumber()) {
//     console.log("Número válido:", iti.getNumber());
//   } else {
//     console.log("Por favor, ingrese un número válido.");
//   }
// });
