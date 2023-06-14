$( document ).ready(function(){
     console.log("hola")}
);

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

