
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
        $("#creacion").html(data);
        $('#myModalCreate').modal('show');
        console.log(data)
      },
      error: function (error) {
        console.log("Abrir modal error ")
          // notificacionError(error.responseJSON.mensaje);
          // mostrarErroresCreacion(error);
          // activarBoton();
      }
  });
}

function abrir_modal_edicion2(url){
  console.log("estoy en abrir modal 2")



    $.ajax({
      url: url,
      success: function(data){
        $("#edicion").html(data);
        $('#myModalEdit').modal('show');
        console.log(data)
      },
      error: function(){
        alert("No se cargó el modal")
      }
    });

}

function abrir_modal_eliminar(url){
  console.log("estoy en abrir modal eliminar")
    $.ajax({
      url: url,
      success: function(data){
        $("#eliminar").html(data);
        $('#myModalDelete').modal('show');
        console.log(data)
      },
      error: function(){
        alert("No se cargó el modal")
      }
    });

}

function editar() {
  activarBoton();
  var data = new FormData($('#form_edicion').get(0));
  $.ajax({        
      url: $('#form_edicion').attr('action'),
      type: $('#form_edicion').attr('method'), 
      data: data,
      cache: false,
      processData: false,
      contentType: false, 
      success: function (response) {
          notificacionSuccess(response.mensaje);
          listadoLibros();
          cerrar_modal_edicion();
      },
      error: function (error) {
          notificacionError(error.responseJSON.mensaje);
          mostrarErroresEdicion(error);
          activarBoton();
      },        
  });
}

function eliminar(pk) {
  $.ajax({
      data: {
          csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
      },
      url: 'users_app:libro:mascota_eliminar/' + pk + '/',
      type: 'post',
      success: function (response) {
          notificacionSuccess(response.mensaje);
          listadoLibros();
          cerrar_modal_eliminacion();
      },
      error: function (error) {
          notificacionError(error.responseJSON.mensaje);
      }
  });
}