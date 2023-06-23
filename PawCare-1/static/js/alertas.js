$.ajax({
    type: 'POST',
    url: '' ,
    success: function() {
      // Estado de la reserva cambiado correctamente
      alert('¡Calificación guardada! La reserva ha sido marcada como Realizada.');
      // Redireccionar a la página actual
      window.location.reload();
    },
    error: function(xhr, textStatus, error) {
      console.log(xhr.statusText);
    }
  });