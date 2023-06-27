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