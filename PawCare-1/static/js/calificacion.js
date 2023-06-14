
function generarEstrellas(promediocalificacion) {
  var estrellasHTML = '';

  var entero = Math.floor(promediocalificacion); // Parte entera
  var decimal = promediocalificacion - entero; // Parte decimal

  // Generar estrellas completas
  for (var i = 0; i < entero; i++) {
    estrellasHTML += '<span class="fa-solid fa-star estrella"></span>';
  }

  // Generar media estrella si corresponde
  if (decimal >= 0.5 && decimal <= 0.9) {
    estrellasHTML += '<span class="fas fa-star-half-alt checked estrella"></span>';
  }

  return estrellasHTML;
}
