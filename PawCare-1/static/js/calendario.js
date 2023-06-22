$( document ).ready(function(){
    console.log("hola")}
);
function abrir_modal_creacion(url) {
    // activarBoton();
  //  var data = new FormData($('#form_creacion').get(0));
    $.ajax({        
        url: url,
        // type: $('#form_creacion').attr('method'), 
        // data: data,
        // cache: false,
        // processData: false,
        // contentType: false, 
        success: function (data) {
          $("#hora").html(data);
          $('#myModalCreateHora').modal('show');
          console.log(data)
        },
        error: function () {
          console.log("Abrir modal error ")
            // notificacionError(error.responseJSON.mensaje);
            // mostrarErroresCreacion(error);
            // activarBoton();
        }
    });
  }

