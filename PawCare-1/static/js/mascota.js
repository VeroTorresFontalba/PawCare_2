$( document ).ready(function(){
     console.log("hola")}
    );

// window.addEventListener("onclick", function(event) {
//     $('#edicion').delay(400).fadeOut(500);
//     // Do what you want, the window is entirely loaded and ready to use.
//     });

//var $ = jQuery.noConflict();
function abrir_modal_edicion(url){
  console.log(url)

  $('#edicion').load(url, function(){
    $('#edicion').modal('show');
  });
}