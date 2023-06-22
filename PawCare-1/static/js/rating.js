
/*function abrir_modal_ratings(url) {
  console.log("HOLAAA");
  console.log(url);
  $.ajax({        
    url: url,
    success: function (data) {
      $("#div_modal_rating").html(data);
      $('#myModalRatings').modal('show');

      var rating = 0; // Variable para almacenar la calificación seleccionada

      // Pintar estrellas al pasar el mouse sobre ellas
      function pintarEstrellas(rating) {
        $('.stars .star i').removeClass('fas').addClass('far');
        $('.stars .star').each(function () {
          if (parseInt($(this).attr('data-rating')) <= rating) {
            $(this).find('i').removeClass('far').addClass('fas');
          }
        });
      }

      $('.stars .star').on('mouseenter', function () {
        var newRating = parseInt($(this).attr('data-rating'));
        pintarEstrellas(newRating);
      });

      $('.stars .star').on('mouseleave', function () {
        pintarEstrellas(rating);
      });

      // Seleccionar estrella al hacer clic
      $('.stars .star').on('click', function () {
        rating = parseInt($(this).attr('data-rating'));
        pintarEstrellas(rating);
        $(this).addClass('selected');
      });

      // Mantener la selección de estrellas al pasar el mouse sobre ellas después de seleccionar
      $('.stars .star.selected').on('mouseenter', function () {
        pintarEstrellas(rating);
      });

      $('#save-rating').click(function () {
        console.log("Calificación:", rating);
        console.log("ID de la reserva:", reservaId);
        // Aquí puedes hacer lo que necesites con la calificación
      });

      

      // Realizar una solicitud AJAX para guardar la calificación en el servidor junto con el ID de la reserva
      $.ajax({
        url: '/finalizar_reserva/' + reservaId + '/',
        method: 'POST',
        data: {
            calificacion: rating
        },
        success: function (response) {
            console.log("Reserva finalizada con éxito:", response);
            $('#myModalRatings').modal('show');
        },
        error: function (error) {
            console.log("Error al finalizar la reserva:", error);
        }
      });
      

    },
    error: function (error) {
      console.log("Abrir modal error ");
    }
  });
}*/


/*function abrir_modal_ratings(url) {
  console.log("HOLAAA");
  console.log(url);
  $.ajax({        
    url: url,
    success: function (data) {
      $("#div_modal_rating").html(data);
      $('#myModalRatings').modal('show');

      var rating = 0; // Variable para almacenar la calificación seleccionada
      var reservaId = obtenerReservaId(); // Obtener el ID de la reserva desde alguna fuente

      // Pintar estrellas al pasar el mouse sobre ellas
      function pintarEstrellas(rating) {
        $('.stars .star i').removeClass('fas').addClass('far');
        $('.stars .star').each(function () {
          if (parseInt($(this).attr('data-rating')) <= rating) {
            $(this).find('i').removeClass('far').addClass('fas');
          }
        });
      }

      $('.stars .star').on('mouseenter', function () {
        var newRating = parseInt($(this).attr('data-rating'));
        pintarEstrellas(newRating);
      });

      $('.stars .star').on('mouseleave', function () {
        pintarEstrellas(rating);
      });

      // Seleccionar estrella al hacer clic
      $('.stars .star').on('click', function () {
        rating = parseInt($(this).attr('data-rating'));
        pintarEstrellas(rating);
        $(this).addClass('selected');
      });

      // Mantener la selección de estrellas al pasar el mouse sobre ellas después de seleccionar
      $('.stars .star.selected').on('mouseenter', function () {
        pintarEstrellas(rating);
      });

      $('#save-rating').click(function () {
        console.log("Calificación:", rating);
        console.log("ID de la reserva:", reservaId);

        // Realizar una solicitud AJAX para guardar la calificación en el servidor junto con el ID de la reserva
       /* $.ajax({
          url: '/finalizar_reserva/' + reservaId + '/',
          method: 'POST',
          data: {
            calificacion: rating
          },
          success: function (response) {
            console.log("Reserva finalizada con éxito:", response);
            $('#myModalRatings').modal('hide');
          },
          error: function (error) {
            console.log("Error al finalizar la reserva:", error);
          }
        });
      });
    },
    error: function (error) {
      console.log("Abrir modal error ");
    }
  });
}

function obtenerReservaId() {
  // Aquí debes implementar la lógica para obtener el ID de la reserva desde alguna fuente, como un atributo del elemento o una variable en el contexto de tu aplicación.
  // Puedes utilizar la misma lógica que tienes en el código original para obtener el ID de la reserva.
  // Retorna el ID de la reserva.
  var reservaId = $("#btn-realizado").data('reserva-id')
  return reservaId
}
*/
$(document).ready(function() {

  // Escucha el evento de clic del botón "Realizado"
  $('button[id^="realizadoBtn-"]').click(function() {
    
    var btnId = $(this).attr('id');// Obtener el id del botón actual
    var modalId = btnId.split('-')[1];// Extraer el número de id del botón
    var modalSelector = '#calificacionModal-' + modalId; // Construir el id del modal correspondiente

    $(modalSelector).modal('show');    // Abrir el modal correspondiente

    // Actualizar el ID del botón "Guardar Calificación" del modal con el ID de reserva correspondiente
    var saveBtnId = 'save-rating-' + modalId;
    $('#save-rating').attr('id', saveBtnId);
  });

  var rating = 0; // Variable para almacenar la calificación seleccionada

  // Pintar estrellas al pasar el mouse sobre ellas
  function pintarEstrellas(rating) {
    $('.stars .star i').removeClass('fas').addClass('far');
    $('.stars .star').each(function() {
      if (parseInt($(this).attr('data-rating')) <= rating) {
        $(this).find('i').removeClass('far').addClass('fas');
      }
    });
  }

  $('.stars .star').on('mouseenter', function() {
    var newRating = parseInt($(this).attr('data-rating'));
    pintarEstrellas(newRating);
  });

  $('.stars .star').on('mouseleave', function() {
    pintarEstrellas(rating);
  });

  // Seleccionar estrella al hacer clic
  $('.stars .star').on('click', function() {
    rating = parseInt($(this).attr('data-rating'));
    pintarEstrellas(rating);
    $(this).addClass('selected');
  });

  // Mantener la selección de estrellas al pasar el mouse sobre ellas después de seleccionar
  $('.stars .star.selected').on('mouseenter', function() {
    pintarEstrellas(rating);
  });

  $('button[id^="save-rating-"]').click(function() {
    var reservaId = $(this).data('reserva-id'); // Obtener el ID de reserva desde el botón
    var calificacion = rating; // Obtener la calificación seleccionada

    // Crear el objeto de datos para enviar en la solicitud AJAX
    var data = {
      reserva_id: reservaId,
      calificacion: calificacion
    };

    // Realizar la solicitud AJAX
    $.ajax({
      type: 'POST',
      url: '/guardar_calificacion/',
      data: JSON.stringify(data),
      contentType: 'application/json',
      dataType: 'json',
      success: function(response) {
        if (response.success) {
          // Calificación guardada correctamente
          $.ajax({
            type: 'POST',
            url: '/finalizar_reserva/' + reservaId + '/',
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
        } else {
          // Error al guardar la calificación
          alert('Error al guardar la calificación: ' + response.message);
        }
      },
      error: function(xhr, textStatus, error) {
        console.log(xhr.statusText);
      }
    });
  });


});
